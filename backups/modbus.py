import minimalmodbus
import serial
import threading
from time import sleep
import statistics

import modbus_conf


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.setDaemon(True)
        thread.start()
        sleep(0.1)
        return (thread)

    return (wrapper)


class ModbusMasterRTU(modbus_conf.ModbusConfig):
    def __init__(self):
        super().__init__()

        self._data_container = {}
        self._schedules = {}
        for slave_id in self._slaves:

            #Define Schedule for every slaves

            slave_data = {}

            #Create Instrument
            slave_info = self._slaves[slave_id]
            client_ok, slave_data['instrument'] = self.CreateClient(
                slave_info['port'])
            if client_ok:
                #List Registers to Read
                slave_data['registers'] = slave_info['registers']

                #Create Data Container for every registers

                data_reads = {}
                for reg in slave_data['registers']:
                    data_register = {
                        'raw_data': [],
                        'raw_lenght': 20,
                        'filtered': None
                    }
                    data_reads.update({reg: data_register})

                self._data_container.update({slave_id: data_reads})

                #Put Slave Task to schedule
                self._schedules[slave_id] = slave_data

                #Run Task
                self.DataCollector(slave_id=slave_id, slave_data=slave_data)

        self.DataPreseter()

    def threaded(fn):
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
            thread.setDaemon(True)
            thread.start()
            sleep(0.1)
            return (thread)

        return (wrapper)

    def CreateClient(self, port, baudrate=9600):
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
            data = instrument.read_register(registeraddress=int(registeraddress),
                                            number_of_decimals=0,
                                            functioncode=3)
        except Exception as e:
            print(f'Read Register {registeraddress} ERROR :: {e}')
            return (False, e)
        else:
            return (True, data)

    @threaded
    def DataCollector(self, slave_id, slave_data):

        while True:
            
            for register in slave_data['registers']:
                instrument = slave_data['instrument']
                read_ok, data = self.ReadRegister(register, instrument)

                if read_ok:

                    if len(self._data_container[slave_id][register]
                           ['raw_data']) >= self._data_container[slave_id][
                               register]['raw_lenght']:
                        del self._data_container[slave_id][register][
                            'raw_data'][:len(self._data_container) - 20]

                        self._data_container[slave_id][register][
                            'raw_data'].append(data)

                    else:
                        self._data_container[slave_id][register][
                            'raw_data'].append(data)

                    #Set Filtered
                    self._data_container[slave_id][register][
                        'filtered'] = statistics.mean(
                            self._data_container[slave_id][register]
                            ['raw_data'])

                sleep(0.25)

    def DataPreseter(self):

        while True:

            print('## VIEW READING')
            print("")
            for slave_id in self._data_container:

                print(
                    "==================================================================="
                )
                print("")
                print(f'Data Slave # {slave_id}')
                print("")
                for register in self._data_container[slave_id]:
                    filtered = self._data_container[slave_id][register][
                        'filtered']
                    print(f'ON Registers > {register} read {filtered}')
                print("")
                print(
                    "==================================================================="
                )

            sleep(5)


if __name__ == "__main__":
    a = ModbusMasterRTU()