import minimalmodbus
import json
import threading
import serial
from time import sleep
import datetime
import configparser
import struct

from temp_sql_module import TempQuerySQL


class Modbus_Mod():
    def __init__(self):
        super().__init__()

        self._modbus_activity = {}
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

        print(self._modbus_devices) 

        try:
            for deviceattachdetailid in self._modbus_devices:

                ##CREATE an Activity for every deviceattachdetailid

                device_activity_data = {}
                device_activity_data = self._modbus_devices[
                    deviceattachdetailid]

                #Create Instrument
                serial_port = device_activity_data['port']
                slave_id = device_activity_data['slave_id']
                client_ok, result = self.CreateInstrument(slave_id=slave_id,port=serial_port)
                if client_ok:

                    #Add Insrument to Data
                    device_activity_data['instrument'] = result

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

                else:
                    raise Exception("Failed to Create Instrument")

        except Exception as e:
            print(e)
        else:
            self.DataReader()
            # self.DataRecorder()

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
        except Exception as e:
            print(f'Read Registers {start} -> {end} :: {int(end)-int(start)} ERROR :: {e}')
            return (False, e)
        else:
            # Convert to Hex
            print(f'Read Registers {start} -> {end} :: {int(end)-int(start)} OK ')
            data = [hex(x)[2:] for x in data]
            return (True, data)

    def ReadJob(self, deviceattachdetailid, read_type):

        # task_list = self._modbus_activity[deviceattachdetailid][
        #     'register_data']
        # read_type = self._modbus_activity[deviceattachdetailid]['comm_type']
        # task_order = list(task_list.keys())
        # task_order.sort()

        read_result = []
        # # READ ONE BY ONE [A / B IS THE SAME]
        # for task_id in task_order:
        #     task_data = task_list[task_id]

        #     register = task_data['register_address']
        #     instrument = self._modbus_activity[deviceattachdetailid][
        #         'instrument']
        #     read_ok, data = self.ReadRegister(registeraddress=register,
        #                                       instrument=instrument)

        #     if read_ok:
        #         read_result.append(data)
        #     else:
        #         return (False, None)

        ## READ UNDER RULE OF A AND B
        if read_type == "A":
            #Instrument
            instrument = self._modbus_activity[deviceattachdetailid][
                'instrument']
            decimal_point = self._modbus_activity[deviceattachdetailid]['decimal_point']

            #Read One
            keys_one = list(self._modbus_activity[deviceattachdetailid][
            'register_data'].keys())[0]
            task_data = self._modbus_activity[deviceattachdetailid][
            'register_data'][keys_one]
            # print(task_data)
            register = task_data['register_address']
            read_ok, data = self.ReadRegister(registeraddress=register,
                                              instrument=instrument)

            if read_ok:
                read_result.append(data)
            else:
                return (False, None)

        elif read_type == "B":
            #Instrument
            instrument = self._modbus_activity[deviceattachdetailid][
                'instrument']
            decimal_point = self._modbus_activity[deviceattachdetailid]['decimal_point']

            #Well this only for convinient
            register_order = [ int(x) for x in list(self._modbus_activity[deviceattachdetailid][
            'register_data'].keys()) ]
            register_order.sort()

            #Get all Register address
            register_address_list = []
            for seq in register_order:
                register_data = self._modbus_activity[deviceattachdetailid]['register_data'][str(seq)]
                register_addr = register_data['register_address']
                register_address_list.append(register_addr)

            
            #order it up
            min_reg = min(register_address_list)
            max_reg = max(register_address_list)

            read_ok, data = self.ReadRegisters(start=min_reg,
                                                end=max_reg,
                                              instrument=instrument)
            print(data)

            if read_ok:
                #Pickup only the used data and by seq order
                # read_result = []
                for seq in register_order:
                    register_data = self._modbus_activity[deviceattachdetailid]['register_data'][str(seq)]
                    register_addr = register_data['register_address']
                    data_for_you = data[int(register_addr)-int(min_reg)]
                    read_result.append(str(data_for_you))
        
            else:
                return (False, None)

        #Reform Data
        formated_data = self.ReformData(read_data=read_result,
                                        read_type=read_type,
                                        decimal_point=decimal_point)
        return (True, formated_data)

    def ReformData(self, read_data, read_type, decimal_point):

        if str(read_type).upper() == "A":
            result = read_data[0]
            if decimal_point != 0:
                result = float(result) / (10 ** int(decimal_point))
            # result = struct.unpack('!f', bytes.fromhex(str(result)))[0]

        elif str(read_type).upper() == "B":
            result = ''

            #Original
            # result_container = []
            
            # for i in range(len(read_data)):
            #     # result += read_data[i]
            #     word = read_data[i]
            #     for i in range(0, len(word), 2):
            #         result_container.append(word[i:i+2])

            # #Reverse
            # for item in result_container[::-1]:
            #     result += item

            #New 
            lenght_data = len(read_data)
            for i in range(lenght_data):
                result += read_data[(lenght_data-1)-i]

            result = struct.unpack('!f', bytes.fromhex(str(result)))[0]
            if decimal_point != 0:
                result = float(result) / (10 ** int(decimal_point))

        return (result)

    def DataFilter(self, deviceattachdetailid, value):
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
        self._DeviceValues_Filtered[deviceattachdetailid] = statistics.mean(
            self._modbus_activity[deviceattachdetailid]['read_data']
            ['raw_data'])

    @threaded
    def DataReader(self):
        print("START DATA READER")
        while True:

            for act_id in self._modbus_activity:
                datas = self._modbus_activity[act_id]
                devicename = datas['devicename']
                read_ok, data = self.ReadJob(deviceattachdetailid=act_id, read_type=datas["comm_type"])

                if read_ok:
                    # self.DataFilter(deviceattachdetailid=act_id,
                    #                 value=data)
                    print(f"from :: {devicename} : is : {data}")

                # sleep(0.25)
                # print("=================================================")
                # print(str(datas["devicename"]))
                
                interval_read = float(self._config.get("MOBUS_GENERAL","interval_read"))
                sleep(interval_read)

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
    a = Modbus_Mod()
    while True:
        pass