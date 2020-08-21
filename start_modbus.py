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
import locale
import os

from temp_sql_module import TempQuerySQL
from onrun_ui import OnRunUis

import logging

#Logger
# Create a custom logger
logger = logging.getLogger(__name__)
folders = "log_files"
f_handler = logging.FileHandler(f'.\{folders}\{__name__}.log', 'a+')
f_handler.setLevel(logging.ERROR)
 
# Create formatters and add it to handlers
f_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
 
# Add handlers to the logger
logger.addHandler(f_handler)




class Modbus_Mod(OnRunUis):
    def __init__(self):
        
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

        ##JSON Save
        self._TempDataJson = {}
        #=========================
        
        self._stoppedo_call = False
        self._stoppedo_confirm = {}
        self._stoppedo_confirm_record = False

        self._startedo = False
        self._startedo_record = False
        self._startedo_record2 = False

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
            logger.error(e, exc_info=True)
            error_type = "PROGRAM"
            devicename = "NONE"
            recordtime = str(datetime.datetime.now())
            detailed_error = f"INITIALIZE MODBUS READING ERROR :: {e}"
            self._DirectDB.InsertError(error_type, devicename, recordtime, detailed_error)
            
            print(e)
        else:

            ## WX PYTHON
            #===========================================
            OnRunUis.__init__(self)
            self.SetDvItem(wx_devicelist)
            #===========================================
            

            # self.DataReader()                
            # self.DataRecorder()
            # self.SaveJSONLoop()
            

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
            logger.error(e, exc_info=True)
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
            logger.error(e, exc_info=True)
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
            logger.error(e, exc_info=True)
            print(f'Read Registers {start} -> {end} :: {int(end)-int(start)} ERROR :: {e}')
            return (False, e)
        else:
            # Convert to Hex
            print(f'Read Registers {start} -> {end} :: {int(end)-int(start)} OK ')
            return (True, data)


    def ReadJob(self, serial_port, slave_id):

        try:
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
                error_type = "SYSTEM"
                devicename = str(ownerlist)
                recordtime = str(datetime.datetime.now())
                detailed_error = f"READ REGISTERS {start} to {end} ERROR :: {data}"
                self._DirectDB.InsertError(error_type, devicename, recordtime, detailed_error)
                

                return (False, None)
        except Exception as e:
            logger.error(e, exc_info=True)

            error_type = "PROGRAM"
            devicename = "NONE"
            recordtime = str(datetime.datetime.now())
            detailed_error = f"READ JOB ERROR :: {e}"
            self._DirectDB.InsertError(error_type, devicename, recordtime, detailed_error)

            print(e)
            return(False, None)
        
        

    def ReformData(self, read_data):

        result_container = {}
        for deviceattachdetailid in read_data.keys():
            read_content = read_data[deviceattachdetailid]
            read_type = self._modbus_activity[deviceattachdetailid]["comm_type"]
            decimal_point = self._modbus_activity[deviceattachdetailid]['decimal_point']

            # A to B Filter
            if str(read_type).upper() == "A":
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

                #No Decimal Point for B
                # if decimal_point != 0:
                #     result = float(result) / (10 ** int(decimal_point))
                
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
            self._DeviceValues_Filtered[deviceattachdetailid] = avg_val

    # @threaded
    def DataReader(self):
        self._startedo = True

        for serial_port in self._modbus_read_schedule:
            port_data = self._modbus_read_schedule[serial_port]
            slave_list = list(port_data.keys())

            #Port Read Thread
            self.PortReadThread(serial_port=serial_port, slave_list=slave_list)

    @threaded
    def PortReadThread(self, serial_port, slave_list):
        print(f"START PORT READ ON {serial_port} and {slave_list}")
        self._stoppedo_confirm.update({serial_port:False})
        while True:
            for slave_id in slave_list:

                #STOP
                if self._stoppedo_call:
                    self._stoppedo_confirm.update({serial_port:True})
                    return

                self.SlaveRead(serial_port=serial_port, slave_id=slave_id)
                interval_read = float(self._config.get("MOBUS_GENERAL","interval_read"))
                sleep(interval_read)


    # @threaded            
    def SlaveRead(self, serial_port, slave_id):
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


    @threaded
    def DataRecorder(self):
        print("START DATA RECORDER")
        
        self._startedo_record = True

        #PRELOAD LOCAL DB
        datenow = str(datetime.date.today())
        self._TempDataJson[str(datenow)] = self.LoadJSON(datenow)

        while True:
            try:
                #STOP
                if self._stoppedo_call:
                    self._stoppedo_confirm_record = True
                    self._startedo_record = False
                    return

                #Check if Required To Save Record
                if bool(int(self._config.get("MOBUS_GENERAL","save_db"))):

                    datenow = str(datetime.date.today())
                    time_record = str(datetime.datetime.now())

                    #save to DB
                    list_act = self._modbus_activity.keys()
                    for item in list_act:
                        item_data = self._modbus_activity[item]
                        devicename = item_data["devicename"]
                        values = self._DeviceValues_Filtered[item]
                        print(f"RECORD {devicename} :: {values}")
                        if values != None:
                            #Local
                            if self._TempDataJson[str(datenow)].get(devicename) == None:
                                self._TempDataJson[str(datenow)][devicename] = {}

                            self._TempDataJson[str(datenow)][devicename].update({str(time_record):values})

                            #DB
                            self._DirectDB.InsertDataSample(devicename,time_record,values)

                interval_read = float(self._config.get("MOBUS_GENERAL","interval_record"))
                sleep(interval_read)
            except Exception as e:
                logger.error(e, exc_info=True)

                try:
                    error_type = "PROGRAM"
                    devicename = "NONE"
                    recordtime = str(datetime.datetime.now())
                    detailed_error = f"MODBUS RECORDING ERROR :: {e}"
                    self._DirectDB.InsertError(error_type, devicename, recordtime, detailed_error)
                except Exception:
                    pass

                print(e)
                # sleep(60)
                for i in range(int(60/6)):
                    #STOP
                    if self._stoppedo_call:
                        self._stoppedo_confirm_record = True
                        self._startedo_record = False
                        return
                    sleep(10)
        
        self._startedo_record = False


    def SaveJSON(self, dates, jsondata):
        with open(f'offline_db\\{dates}.json', 'w+') as jsonfile:
            json.dump(jsondata, jsonfile, indent=4)

    def LoadJSON(self, dates):
        if os.path.exists(f'offline_db\\{dates}.csv'):
            with open(f'{dates}.json', 'r') as jsonfile:
                jsondata = json.load(jsonfile)
                return(jsondata)
        else:
            with open(f'offline_db\\{dates}.json', 'w+') as jsonfile:
                json.dump({}, jsonfile, indent=4)

            return({})


    @threaded
    def SaveJSONLoop(self):
        
        sleep(10)

        self._startedo_record2 = True

        print("START JSON LOOP SAVE")
        datebefore = datetime.date.today()
        while True:

            #STOP
            if self._stoppedo_call:
                self._stoppedo_confirm_record2 = True
                self._startedo_record2 = False
                return

            try:
                datenow = datetime.date.today()

                dategap = (datenow - datebefore).days
                if dategap > 0:
                    #SAVE DATEBEFORE
                    looped = dategap
                    for i in range(looped):
                        date_is = datetime.timedelta(days=dategap)
                        data = self._TempDataJson[str(datenow)]
                        for device_name in data.keys():
                            data_dev = data[device_name]
                            data[device_name] = {} #Empty 'ed
                            self.SaveJSON(date_is, data_dev)
                        
                        dategap -= 1
                    
                    #DELETE
                    backup = self._TempDataJson[str(datenow)]
                    self._TempDataJson = {str(datenow):backup}

                    #SET DATE BEFORE
                    datebefore = datenow

                else:
                    #SAVE DATENOW
                    data = self._TempDataJson[str(datenow)]
                    for device_name in data.keys():
                        data_dev = data[device_name]
                        data[device_name] = {} #Empty 'ed
                        self.SaveJSON(datenow, data_dev)

                    
            except Exception as e:
                logger.error(e, exc_info=True)
                
            # sleep(3600)
            for i in range(int(3600/10)):
                #STOP
                if self._stoppedo_call:
                    self._stoppedo_confirm_record2 = True
                    self._startedo_record2 = False
                    return
                sleep(10)

        self._startedo_record2 = False

        
if __name__ == "__main__":
    APPS = wx.App(False)
    a = Modbus_Mod()
    APPS.MainLoop()