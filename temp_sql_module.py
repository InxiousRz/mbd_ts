import psycopg2

class TempQuerySQL():
    def __init__(self):
        self._DB_CONN = self.CreateConnection()

        # self._DB_CONN.close()

    def CreateConnection(self):

        conn = psycopg2.connect(
            dbname="agrotechdb",
            user="postgres",
            password="PharmaLogic",
            host="agrotech.cbyoam1fda2f.ap-southeast-1.rds.amazonaws.com",
            port="5432")
        # print(conn)
        return (conn)

    ## ACTUAL QUERIES
    ##===============================================================================

    def InsertDataSample(self, devicename, recordtime, values):
        sql = """
                --INSERT DATA DATA SAMPLE
                INSERT INTO trial_datasample_rooftop(devicename, recordtime, values)
                VALUES(%(devicename)s, %(recordtime)s, %(values)s)
        """

        params = {
            'devicename': devicename,
            'recordtime': recordtime,
            'values': values,
        }

        #Execute
        try:
            cur = self._DB_CONN.cursor()
            cur.execute(sql, params)
        except Exception as e:
            self._DB_CONN.rollback()
        else:
            self._DB_CONN.commit()

        cur.close()

    def InsertError(self, error_type, devicename, recordtime, detailed_error):
        sql = """
                --INSERT ERROR
                INSERT INTO trial_error_rooftop(error_type, devicename, recordtime, detailed_error)
                VALUES(%(error_type)s, %(devicename)s, %(recordtime)s, %(detailed_error)s)
        """

        params = {
            'devicename': devicename,
            'recordtime': recordtime,
            'values': values,
            'detailed_error': detailed_error,
        }

        #Execute
        try:
            cur = self._DB_CONN.cursor()
            cur.execute(sql, params)
        except Exception as e:
            self._DB_CONN.rollback()
        else:
            self._DB_CONN.commit()

        cur.close()


# if __name__ == "__main__":
#     a = TempQuerySQL()