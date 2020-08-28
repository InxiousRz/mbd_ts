import minimalmodbus

## Outer Module
# from sub_modules.controller_mod import Controle

## Inner Member
# from behavior.sensor_reader_store import SensorReader_Storage


class Modbus_Mod():
    def __init__(self):
        super().__init__()

        self._modbus_activity = {}
        # self._modbus_devices =  = {
        #     ##-----------------------------------
        #     ##EXAMPLES
        #     ##-----------------------------------
        #     # "#deviceattachid":{
        #     #     "comm_type":"MODBUS",
        #     #     "types":"A",
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

        try:
            for deviceattachdetailid in self._modbus_devices:

                ##CREATE an Activity for every deviceattachdetailid

                device_activity_data = {}
                device_activity_data = self._modbus_devices[
                    deviceattachdetailid]

                #Create Instrument
                serial_port = device_activity_data['port']
                client_ok, result = self.CreateInstrument(serial_port)
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

                else:
                    raise Exception("Failed to Create Instrument")

        except Exception as e:
            print(e)

        self.DataReader()

    def threaded(fn):
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
            thread.setDaemon(True)
            thread.start()
            sleep(0.1)
            return (thread)

        return (wrapper)

    def CreateInstrument(self, port, baudrate=9600):
        try:
            instrument = minimalmodbus.Instrument(
                port=str(port),
                slaveaddress=1)  # port name, slave address (in decimal)

            instrument.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
            instrument.clear_buffers_before_each_transaction = True

            instrument.serial.baudrate = baudrate  # Baud
            instrument.serial.bytesize = 8
            instrument.serial.parity = serial.PARITY_NONE
            instrument.serial.stopbits = 1
            instrument.serial.timeout = 0.05  # seconds
        except Exception as e:
            print(f'Create Modbus Master ERROR :: {e}')
            return (False, e)
        else:
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

    def ReadJob(self, deviceattachdetailid, read_type):

        task_list = self._modbus_activity[deviceattachdetailid][
            'register_data']
        read_type = self._modbus_activity[deviceattachdetailid]['types']
        task_order = list(task_list.keys()).sort()

        read_result = []
        for task_id in task_order:
            task_data = task_list[task_id]

            register = task_data['register_address']
            instrument = self._modbus_activity[deviceattachdetailid][
                'instrument']
            read_ok, data = self.ReadRegister(registeraddress=register,
                                              instrument=instrument)

            if read_ok:
                read_result.append(data)
            else:
                return (None)

        #Reform Data
        formated_data = self.ReformData(read_data=read_result,
                                        read_type=read_type)
        return (formated_data)

    def ReformData(self, read_data, read_type):

        if str(read_type).upper() == "A":
            result = read_data[0]

        elif str(read_type).upper() == "B":
            result = ''
            for i in range(len(read_data)):
                result += read_data[i]

            #Reverse
            result = result[::-1]

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
        keyword = self._DeviceAttachedMap_byID[deviceattachdetailid]
        self._DeviceValues_Filtered[keyword] = statistics.mean(
            self._modbus_activity[deviceattachdetailid]['read_data']
            ['raw_data'])

    @threaded
    def DataReader(self):

        while True:

            for act_id in self._modbus_activity:

                self.ReadJob(deviceattachdetailid=act_id)

                if read_ok:
                    self.DataFilter(slave_id=slave_id,
                                    device_data=device_data,
                                    value=data)

                sleep(0.25)



if __name__ == "__main__":
    a = Modbus_Mod()