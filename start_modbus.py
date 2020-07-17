import minimalmodbus
import json
import threading
import serial
import statistics
from time import sleep
import datetime
import configparser
import struct
import sys
import wx

from temp_sql_module import TempQuerySQL
from onrun_ui import OnRunUis


class Modbus_Mod(OnRunUis):
    def __init__(self):

        self._modbus_activity = {}
        self._modbus_read_schedule = {}
        self._DeviceValues_Filtered = {}

        self._DirectDB = TempQuerySQL()
        # self._modbus_devices =  = {
        #     ##-----------------------------------
        #     ##EXAMPLES
        #     ##-----------------------------------
        #     # "#deviceattachid":{
        #     #     "comm_type":"MODBUS",
        #     #     "comm_type":"A",
        #     #     "decimal_point":0,
        #     #     "modbusslaveid":1,
        #     #     "slave_id":1,
        #     #     "port":COM1,
        #     #     "register_data":{
        #     #         "#sequence":{
        #     #             "modbusregisterid":3,
        #     #             "register_address":1,
        #     #             "register_alias":"PH"
        #     #         }
        #     #     }
        #     # }
        # }

        #SETTINGS
        self._config = configparser.ConfigParser()
        self._config.read_file(open("modb_conf.cfg"))
        

        with open("ui\db\data_main.json", "r") as jsonfile:
            self._modbus_devices = json.load(jsonfile)

        try:
            ##WX
            #=================================
            wx_devicelist = []
            #=================================

            existed_instrument = {}
            for deviceattachdetailid in self._modbus_devices:

                ##CREATE an Activity for every deviceattachdetailid
                device_activity_data = {}
                device_activity_data = self._modbus_devices[
                    deviceattachdetailid]

                #Create Instrument
                serial_port = device_activity_data['port']
                slave_id = device_activity_data['slave_id']


                ## Data Scheduler
                ##=========================================================
                if self._modbus_read_schedule.get(serial_port) == None:
                    self._modbus_read_schedule.update({serial_port:{}})
                
                if self._modbus_read_schedule[serial_port].get(slave_id) == None:
                    self._modbus_read_schedule[serial_port].update({slave_id:{}})
                
                if self._modbus_read_schedule[serial_port][slave_id].get("register_list") == None:
                    self._modbus_read_schedule[serial_port][slave_id].update({"register_list":[]})
                    self._modbus_read_schedule[serial_port][slave_id].update({"register_owner":{}})

                #ADD OWNER
                self._modbus_read_schedule[serial_port][slave_id]["register_owner"].update(
                    {deviceattachdetailid:device_activity_data['register_data']}
                )

                #ADD REGISTER TO LIST
                for sequence in device_activity_data['register_data']:
                    reg_data = device_activity_data['register_data'][sequence]
                    self._modbus_read_schedule[serial_port][slave_id]["register_list"].append(
                        reg_data["register_address"])
                    

                client_ok, result = self.CreateInstrument(slave_id=slave_id,port=serial_port)
                # client_ok = True
                # result = {}

                if client_ok:

                    #Add Insrument to Data
                    device_activity_data['instrument'] = result
                    self._modbus_read_schedule[serial_port][slave_id]["instrument"] = result

                    #Create Data Read Container
                    device_activity_data['read_data'] = {
                        'raw_data': [],
                        'raw_lenght': 20
                    }

                    #Put Slave Task to Activity
                    self._modbus_activity[
                        deviceattachdetailid] = device_activity_data

                    #Add filtered
                    self._DeviceValues_Filtered[deviceattachdetailid] = None

                    ##WX
                    #=================================
                    wx_devicelist.append(device_activity_data["devicename"])
                    #=================================

                else:
                    raise Exception("Failed to Create Instrument")

        except Exception as e:
            print(e)
        else:
            
            # print(json.dumps(self._modbus_read_schedule, indent=4))
            # sys.exit(0)

            ## WX PYTHON
            #===========================================
            OnRunUis.__init__(self)
            self.SetDvItem(wx_devicelist)
            #===========================================
            

            self.DataReader()                
            # self.DataRecorder()
            

            ## WX PYTHON
            #===========================================
            self.OpenForms()
            #===========================================

    def threaded(fn):
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
            thread.setDaemon(True)
            thread.start()
            sleep(0.1)
            return (thread)

        return (wrapper)

    def CreateInstrument(self, slave_id, port, baudrate=38400):
        try:
            instrument = minimalmodbus.Instrument(
                port=str(port),
                slaveaddress=int(slave_id))  # port name, slave address (in decimal)

            instrument.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
            instrument.clear_buffers_before_each_transaction = True

            instrument.serial.baudrate = baudrate  # Baud
            instrument.serial.bytesize = int(self._config.get("MOBUS_GENERAL","bytesize"))
            instrument.serial.parity = serial.PARITY_NONE
            instrument.serial.stopbits = int(self._config.get("MOBUS_GENERAL","stopbits"))
            instrument.serial.timeout = float(self._config.get("MOBUS_GENERAL","timeout"))
            
        except Exception as e:
            print(f'Create Modbus Master ERROR :: {e}')
            return (False, e)
        else:
            # print(instrument)
            return (True, instrument)

    def ReadRegister(self, registeraddress, instrument):
        try:
            data = instrument.read_register(
                registeraddress=int(registeraddress),
                number_of_decimals=0,
                functioncode=3)
        except Exception as e:
            print(f'Read Register {registeraddress} ERROR :: {e}')
            return (False, e)
        else:
            return (True, data)

    def ReadRegisters(self, start, end, instrument):
        try:
            data = instrument.read_registers(registeraddress=int(start),
            number_of_registers=int(end)-int(start)+1, functioncode=3)
            #note max number registers is 125 , bug for the future
        except Exception as e:
            print(f'Read Registers {start} -> {end} :: {int(end)-int(start)} ERROR :: {e}')
            return (False, e)
        else:
            # Convert to Hex
            print(f'Read Registers {start} -> {end} :: {int(end)-int(start)} OK ')
            return (True, data)


    def ReadJob(self, serial_port, slave_id):

        job_data = self._modbus_read_schedule[serial_port][slave_id]

        instrument = job_data["instrument"]
        ownerlist = job_data["register_owner"]

        #Well this for convenienve
        register_address_list = [ int(x) for x in job_data["register_list"] ]
        register_address_list.sort()
        
        #order it up, and do some math
        min_reg = min(register_address_list)
        max_reg = max(register_address_list)
        reg_range = max_reg-min_reg + 1

        read_ok, data = self.ReadRegisters(start=min_reg,
                                            end=max_reg,
                                            instrument=instrument)
        # print(data)

        if read_ok:
            #Pickup only the used data and by owner
            read_result = {}
            for deviceattachdetailid in ownerlist.keys():
                owner_data = ownerlist[deviceattachdetailid]
                read_result.update({deviceattachdetailid:[]})

                #Get Data for this owner
                for seq in owner_data:
                    register_data = owner_data[seq]
                    register_addr = register_data['register_address']

                    #Get Specified data per sequence
                    data_for_you = data[int(register_addr)-int(min_reg)]
                    read_result[deviceattachdetailid].append(data_for_you)


            # print(read_result)

            #Reform Data
            formated_data = self.ReformData(read_data=read_result)

            #Data Filter
            self.DataFilter(read_data=formated_data)

            return (True, formated_data)
    
        else:
            return (False, None)

        
        

    def ReformData(self, read_data):

        result_container = {}
        for deviceattachdetailid in read_data.keys():
            read_content = read_data[deviceattachdetailid]
            read_type = self._modbus_activity[deviceattachdetailid]["comm_type"]
            decimal_point = self._modbus_activity[deviceattachdetailid]['decimal_point']

            # A to B Filter
            if str(read_type).upper() == "A":
                # print(f"========== {read_content}")
                result = float(read_content[0])
                if decimal_point != 0:
                    result = result / (10 ** int(decimal_point))
                
                #Append Result
                result_container.update({deviceattachdetailid:result})

            elif str(read_type).upper() == "B":

                #convert Hex
                read_content = [hex(x)[2:] for x in read_content]
                
                result = ''

                #New 
                lenght_data = len(read_content)
                for i in range(lenght_data):
                    result += read_content[(lenght_data-1)-i]

                result = float(struct.unpack('!f', bytes.fromhex(str(result)))[0])
                if decimal_point != 0:
                    result = float(result) / (10 ** int(decimal_point))
                
                #Append Result
                result_container.update({deviceattachdetailid:result})

        return (result_container)

    def DataFilter(self, read_data):

        for deviceattachdetailid in read_data.keys():
            value = read_data[deviceattachdetailid]
            decimal_point = self._modbus_activity[deviceattachdetailid]['decimal_point']
            
            
            #Collect data and filter
            if len(self._modbus_activity[deviceattachdetailid]['read_data']
                ['raw_data']) >= self._modbus_activity[deviceattachdetailid][
                    'read_data']['raw_lenght']:
                del self._modbus_activity[deviceattachdetailid]['read_data'][
                    'raw_data'][:len(self._modbus_activity[deviceattachdetailid]
                                    ['read_data']['raw_data']) - 20]

                self._modbus_activity[deviceattachdetailid]['read_data'][
                    'raw_data'].append(value)

            else:
                self._modbus_activity[deviceattachdetailid]['read_data'][
                    'raw_data'].append(value)

            #Set Filtered
            dev_name = self._modbus_activity[deviceattachdetailid]["devicename"]
            avg_val = statistics.mean(self._modbus_activity[deviceattachdetailid]['read_data']['raw_data'])
            avg_val = round(avg_val,int(decimal_point))
            self.UpdateDvItem(dev_name, str(avg_val))

            # self._DeviceValues_Filtered[deviceattachdetailid] = statistics.mean(
            #     self._modbus_activity[deviceattachdetailid]['read_data']
            #     ['raw_data'])

    @threaded
    def DataReader(self):

        while True:
            for serial_port in self._modbus_read_schedule:
                port_data = self._modbus_read_schedule[serial_port]
                slave_list = list(port_data.keys())
                for slave_id in slave_list:
                    self.ReadThread(serial_port=serial_port, slave_id=slave_id)
                    sleep(1)


    # @threaded            
    def ReadThread(self, serial_port, slave_id):
        print(f"START DATA READER FOR COM-PORT {serial_port} SLAVE-ID {slave_id} ")
        # while True:
            # try:
        read_ok, read_data = self.ReadJob(serial_port=serial_port, slave_id=slave_id)        

        if read_ok:
            for deviceattachdetailid in read_data.keys():
                devicename = self._modbus_activity[deviceattachdetailid]["devicename"]
                data = read_data[deviceattachdetailid]
                ##WX
                #==========================
                self.AddItemToLb(f"{devicename} :: {data}")
                #==========================
                print(f"from :: {devicename} : is : {data}")
        else:
            ##WX
            #==========================
            self.AddItemToLb(f"COM-SLAVE {serial_port} - {slave_id} ::ERROR")
            #==========================

        # except Exception as e:
        #     print(e)

        
        # interval_read = float(self._config.get("MOBUS_GENERAL","interval_read"))
        # sleep(interval_read)


    @threaded
    def DataRecorder(self):
        print("START DATA RECORDER")
        while True:

            #save to DB
            list_act = self._modbus_activity.keys()
            time_record = str(datetime.datetime.now())
            for item in list_act:
                item_data = self._modbus_activity[item]
                devicename = item_data["devicename"]
                values = self._DeviceValues_Filtered[item]
                print(f"{devicename} :: {values}")
                # if values != None:
                #     self._DirectDB.InsertDataSample(devicename,time_record,values)

            interval_read = float(self._config.get("MOBUS_GENERAL","interval_record"))
            sleep(interval_read)


if __name__ == "__main__":
    APPS = wx.App(False)
    a = Modbus_Mod()
    APPS.MainLoop()