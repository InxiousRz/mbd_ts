import configparser
import os


class ModbusConfig():
    def __init__(self):

        # DEFINE CONFIG FILE
        self.config = configparser.ConfigParser()
        self.config.readfp(open(str(os.getcwd()) + '/modb_conf.cfg'))

        #SLAVE1
        s1_port = str(self.config.get('SLAVE 1', 'port'))
        s1_slaveid = int(self.config.get('SLAVE 1', 'slaveid'))
        s1_registers = self.config.get('SLAVE 1',
                                       'registers').strip().split(',')

        #SLAVE2
        s2_port = str(self.config.get('SLAVE 2', 'port'))
        s2_slaveid = int(self.config.get('SLAVE 2', 'slaveid'))
        s2_registers = self.config.get('SLAVE 2',
                                       'registers').strip().split(',')

        #SLAVE3
        s3_port = str(self.config.get('SLAVE 3', 'port'))
        s3_slaveid = int(self.config.get('SLAVE 3', 'slaveid'))
        s3_registers = self.config.get('SLAVE 3',
                                       'registers').strip().split(',')

        self._slaves = {
            s1_slaveid: {
                'slaveid': s1_slaveid,
                'port': s1_port,
                'registers': s1_registers
            },
            s2_slaveid: {
                'slaveid': s2_slaveid,
                'port': s2_port,
                'registers': s2_registers
            },
            s3_slaveid: {
                'slaveid': s3_slaveid,
                'port': s3_port,
                'registers': s3_registers
            }
        }
