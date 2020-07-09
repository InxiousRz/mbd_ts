import psycopg2


class TempQuerySQL():
    def __init__(self):
        self._DB_CONN = self.CreateConnection()

        # self.GetDeviceConnType(1)
        # self.GetDeviceCommDetailMQTT(1)
        # self.GetDeviceCommDetailMODBUS(5)
        self.GetDataAll(1)
        self.GetDataMQTT(1)
        self.GetDataMODBUS(1)

        self._DB_CONN.close()

    def CreateConnection(self):

        conn = psycopg2.connect(
            dbname="agrotechdb",
            user="postgres",
            password="PharmaLogic",
            host="agrotech.cbyoam1fda2f.ap-southeast-1.rds.amazonaws.com",
            port="5432")
        print(conn)
        return (conn)

    def RunGeneralQuery(self, string_query, params, types, howmany=0):
        cur = self._DB_CONN.cursor()

        try:
            cur.execute(string_query, params)

            if types == 1:
                data = None
            elif types == 2:
                data = cur.fetchone()
            elif types == 3:
                data = cur.fetchmany(howmany)
            elif types == 4:
                data = cur.fetchall()
        except Exception as e:
            self._DB_CONN.rollback()
            ok = False
            data = None
            err = e
        else:
            self._DB_CONN.commit()
            ok = True
            err = None

        cur.close()
        return (ok, data, err)

    def GetDataAll(self, deviceattachid):

        list_device_comm = self.GetAllDeviceCommType(deviceattachid)

        container_mqtt = {}
        container_modbus = {}

        for dev in list_device_comm.keys():
            deviceattachdetailid = dev
            device_comms = list_device_comm[deviceattachdetailid]

            if device_comms == "MQTT":
                data_device_comm = self.GetDeviceCommDetailMQTT(
                    deviceattachdetailid=deviceattachdetailid)
                container_mqtt.update({deviceattachdetailid: data_device_comm})
            elif device_comms == "MODBUS":
                data_device_comm = self.GetDeviceCommDetailMODBUS(
                    deviceattachdetailid=deviceattachdetailid)
                container_modbus.update(
                    {deviceattachdetailid: data_device_comm})

        print(
            "===============================================================")
        print(container_mqtt)
        print(
            "===============================================================")
        print(container_modbus)

    
    def GetDataMODBUS(self, deviceattachid):

        list_device_comm = self.GetDeviceCommTypeMODBUS(deviceattachid)

        container_modbus = {}

        for dev in list_device_comm.keys():
            deviceattachdetailid = dev
            device_comms = list_device_comm[deviceattachdetailid]

            data_device_comm = self.GetDeviceCommDetailMODBUS(
                deviceattachdetailid=deviceattachdetailid)
            container_modbus.update(
                {deviceattachdetailid: data_device_comm})

        print(
            "===============================================================")
        print(container_modbus)

        return(container_modbus)


    def GetDataMQTT(self, deviceattachid):

        list_device_comm = self.GetDeviceCommTypeMQTT(deviceattachid)

        container_mqtt = {}

        for dev in list_device_comm.keys():
            deviceattachdetailid = dev
            device_comms = list_device_comm[deviceattachdetailid]

            data_device_comm = self.GetDeviceCommDetailMQTT(
                deviceattachdetailid=deviceattachdetailid)
            container_mqtt.update({deviceattachdetailid: data_device_comm})

        print(
            "===============================================================")
        print(container_mqtt)

        return(container_mqtt)

    ## ACTUAL QUERIES
    ##===============================================================================

    def GetAllDeviceCommType(self, deviceattachid):
        sql = """
                --GET MODBUS COMMUNICATION TYPE 
                SELECT 
                    dad.deviceattachdetailid,
                    dcom.comm_type
                    
                FROM msdeviceattachdetail as dad
                JOIN msdevicecommunication as dcom ON dad.deviceattachdetailid = dcom.deviceattachdetailid
                WHERE dad.deviceattachid = %(deviceattachid)s
        """

        params = {'deviceattachid': deviceattachid}

        #Execute
        ok, data, err = self.RunGeneralQuery(string_query=sql,
                                             params=params,
                                             types=4)

        if ok:

            # print(data)

            #FORMAT DATA
            container = {}
            for row in data:
                container.update({row[0]: row[1]})

            # print(container)
            return (container)
        else:
            return (None)

    def GetDeviceCommTypeMQTT(self, deviceattachid):
        sql = """
                --GET MODBUS COMMUNICATION TYPE 
                SELECT 
                    dad.deviceattachdetailid,
                    dcom.comm_type
                    
                FROM msdeviceattachdetail as dad
                JOIN msdevicecommunication as dcom ON dad.deviceattachdetailid = dcom.deviceattachdetailid
                WHERE dad.deviceattachid = %(deviceattachid)s AND
                dcom.comm_type = 'MQTT'
        """

        params = {'deviceattachid': deviceattachid}

        #Execute
        ok, data, err = self.RunGeneralQuery(string_query=sql,
                                             params=params,
                                             types=4)

        if ok:

            # print(data)

            #FORMAT DATA
            container = {}
            for row in data:
                container.update({row[0]: row[1]})

            # print(container)
            return (container)
        else:
            return (None)

    def GetDeviceCommTypeMODBUS(self, deviceattachid):
        sql = """
                --GET MODBUS COMMUNICATION TYPE 
                SELECT 
                    dad.deviceattachdetailid,
                    dcom.comm_type
                    
                FROM msdeviceattachdetail as dad
                JOIN msdevicecommunication as dcom ON dad.deviceattachdetailid = dcom.deviceattachdetailid
                WHERE dad.deviceattachid = %(deviceattachid)s AND
                dcom.comm_type = 'MODBUS'
        """

        params = {'deviceattachid': deviceattachid}

        #Execute
        ok, data, err = self.RunGeneralQuery(string_query=sql,
                                             params=params,
                                             types=4)

        if ok:

            # print(data)

            #FORMAT DATA
            container = {}
            for row in data:
                container.update({row[0]: row[1]})

            # print(container)
            return (container)
        else:
            return (None)

    def GetDeviceCommDetailMQTT(self, deviceattachdetailid):
        sql = """
                --GET MODBUS COMMUNICATION DETAIL - MQTT
                SELECT 
                    dad.deviceattachdetailid,
                    dad.deviceid, 
                    dcom.comm_type, 
                    mqcom.mqttcommid,
                    mqcom.brokerid, 
                    mqcom.command_topic, 
                    mqcom.feedback_topic,
                    mbroke.brokerlink,
                    mbroke.brokername,
                    mbroke.brokerkeepalive,
                    mbroke.types,
                    mbroke.needauthlogin,
                    mbroke.username,
                    mbroke.password,
                    mbroke.brokerport
                    
                FROM msdeviceattachdetail as dad
                JOIN msdevice as d ON dad.deviceid = d.deviceid
                JOIN msdevicecommunication as dcom ON dad.deviceattachdetailid = dcom.deviceattachdetailid
                JOIN mqtt_comms as mqcom ON dad.deviceattachdetailid = mqcom.deviceattachdetailid
                JOIN msbroker as mbroke ON mqcom.brokerid = mbroke.brokerid
                WHERE dad.deviceattachdetailid = %(deviceattachdetailid)s
        """

        params = {'deviceattachdetailid': deviceattachdetailid}

        #Execute
        ok, data, err = self.RunGeneralQuery(string_query=sql,
                                             params=params,
                                             types=2)

        if ok:

            # print(data)

            #FORMAT DATA
            container = {
                "deviceattachdetailid": data[0],
                "deviceid": data[1],
                "comm_type": data[2],
                "mqttcommid": data[3],
                "brokerid": data[4],
                "command_topic": data[5],
                "feedback_topic": data[6],
                "brokerlink": data[7],
                "brokername": data[8],
                "brokerkeepalive": data[9],
                "types": data[10],
                "needauthlogin": data[11],
                "username": data[12],
                "password": data[13],
                "brokerport": data[14],
            }

            print(container)
            return (container)
        else:
            return (None)

    def GetDeviceCommDetailMODBUS(self, deviceattachdetailid):

        ## PART 01
        # ------------------------------------------------------------------------------
        sql = """
                --GET MODBUS COMMUNICATION DETAIL - MODBUS - part01 
                SELECT 
                    dad.deviceattachdetailid,
                    dad.deviceid, 
                    dcom.comm_type,
                    mbcom.modbuscommid,
                    mbcom.types,
                    mbcom.decimal_point,
                    mbcom.modbusslaveid,
                    mbslave.slave_id,
                    mbslave.port
                    
                FROM msdeviceattachdetail as dad
                JOIN msdevice as d ON dad.deviceid = d.deviceid
                JOIN msdevicecommunication as dcom ON dad.deviceattachdetailid = dcom.deviceattachdetailid
                JOIN modbus_comms as mbcom ON dad.deviceattachdetailid = mbcom.deviceattachdetailid
                JOIN modbus_slaves as mbslave ON mbcom.modbusslaveid = mbslave.modbusslaveid
                WHERE dad.deviceattachdetailid = %(deviceattachdetailid)s
        """

        params = {'deviceattachdetailid': deviceattachdetailid}

        #Execute
        ok, data, err = self.RunGeneralQuery(string_query=sql,
                                             params=params,
                                             types=2)

        if ok:

            # print(data)

            #FORMAT DATA
            container = {
                "deviceattachdetailid": data[0],
                "deviceid": data[1],
                "comm_type": data[2],
                "modbuscommid": data[3],
                "types": data[4],
                "decimal_point": data[5],
                "modbusslaveid": data[6],
                "slave_id": data[7],
                "port": data[8],
            }

            print(container)
            # return (container)
        else:
            return (None)

        ## PART 02
        # ------------------------------------------------------------------------------
        sql = """
                -- GET REGISTER MEMBER OF MODBUS COMMUNICATION DATA - part02
                SELECT 
                    mbcom.modbuscommid,
                    mbcom_reg.sequence,
                    mbcom_reg.modbusregisterid,
                    mbreg.register_address,
                    mbreg.register_alias
                    
                FROM modbus_comms as mbcom
                JOIN modbus_comms_registers as mbcom_reg ON mbcom.modbuscommid = mbcom_reg.modbuscommid
                JOIN modbus_registers as mbreg ON mbcom_reg.modbusregisterid = mbreg.modbusregisterid
                WHERE mbcom.modbuscommid = %(modbuscommid)s
        """

        params = {'modbuscommid': container["modbuscommid"]}

        #Execute
        ok, data, err = self.RunGeneralQuery(string_query=sql,
                                             params=params,
                                             types=4)

        if ok:

            # print(data)

            container.update({"register_data": {}})

            #FORMAT DATA
            for row in data:
                sequence = row[1]
                data_detail = {
                    "modbuscommid": row[0],
                    "sequence": row[1],
                    "modbusregisterid": row[2],
                    "register_address": row[3],
                    "register_alias": row[4],
                }
                container["register_data"].update({sequence: data_detail})

            print(container)
            return (container)
        else:
            return (None)


    def GetDosingData(self, dosingid):

        ## PART 01
        # ------------------------------------------------------------------------------
        sql = """
                --GET Dosing Data and Formula - part01 
                SELECT 
                    dos.dosingid,
                    dos.dosingname,
                    df.formulaid,
                    df.full_formula
                FROM msdosing as dos
                JOIN msdosingformula as df ON dos.dosingid = df.dosingid
                WHERE dos.dosingid = %(dosingid)s
        """

        params = {'dosingid': dosingid}

        #Execute
        ok, data, err = self.RunGeneralQuery(string_query=sql,
                                             params=params,
                                             types=2)

        if ok:

            # print(data)

            #FORMAT DATA
            container = {
                "dosingid": data[0],
                "dosingname": data[1],
                "formulaid": data[2],
                "full_formula": data[3]
            }

            print(container)
            # return (container)
        else:
            return (None)

        ## PART 02
        # ------------------------------------------------------------------------------
        sql = """
                -- GET Data Fertilizer Ratio - part02
                SELECT 
                    dos.dosingid,
                    fr.fertilizerid,
                    fr.fertilizername,
                    fr.ratio_mt,
                    fr.sequence
                FROM msdosing as dos
                JOIN msfertilizerratio as fr ON dos.dosingid = fr.dosingid
                WHERE dos.dosingid = %(dosingid)s
        """

        params = {'dosingid': dosingid}

        #Execute
        ok, data, err = self.RunGeneralQuery(string_query=sql,
                                             params=params,
                                             types=4)

        if ok:

            # print(data)

            container.update({"ratio_data": {}})

            #FORMAT DATA
            for row in data:
                sequence = row[1]
                data_detail = {
                    "dosingid": row[0],
                    "fertilizerid": row[1],
                    "fertilizername": row[2],
                    "ratio_mt": row[3],
                    "sequence": row[4],
                }
                container["ratio_data"].update({sequence: data_detail})

            print(container)
            return (container)
        else:
            return (None)

if __name__ == "__main__":
    a = TempQuerySQL()