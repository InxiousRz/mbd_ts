import psycopg2
import datetime

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

class TempQuerySQL_2():
    def __init__(self):
        pass

        # self._DB_CONN.close()
        # self.GetDataSample(devicename="PH_Sensor",recorddate="2020-08-05")

    def CreateConnection(self):

        conn = psycopg2.connect(
            dbname="agrotechdb",
            user="postgres",
            password="PharmaLogic",
            host="agrotech.cbyoam1fda2f.ap-southeast-1.rds.amazonaws.com",
            port="5432")
        # print(conn)
        return (conn)

    def RunGeneralQuery(self, string_query, params, types, howmany=0):
        self._DB_CONN = self.CreateConnection()

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
            logger.error(e, exc_info=True)
            self._DB_CONN.rollback()
            ok = False
            data = None
            err = e
        else:
            self._DB_CONN.commit()
            ok = True
            err = None

        cur.close()

        self._DB_CONN.close()

        return (ok, data, err)

    ## ACTUAL QUERIES
    ##===============================================================================

    def GetDataSample(self, devicename, recorddate):
        try:
            container = {}

            sql = """
                    --GET DATA SAMPLE
                    SELECT
                        recordtime,
                        values
                    FROM trial_datasample_rooftop
                    WHERE devicename = %(devicename)s AND
                    CAST(recordtime as date) = %(recorddate)s --'2020-08-05'
                    ORDER BY recordtime asc
            """

            params = {
                'devicename': devicename,
                'recorddate': recorddate
            }

            #Execute
            ok, data, err = self.RunGeneralQuery(string_query=sql,
                                                params=params,
                                                types=4)

            if ok:

                # print(data)

                #FORMAT DATA
                for row in data:
                    # converted_datetime = datetime.datetime.strftime(row[0],"%Y-%m-%d %H:%M:%S.%f")
                    converted_datetime = row[0]
                    data_detail = [converted_datetime, float(row[1])]
                    container.update({str(row[0]): data_detail})

                print(container)
                return (container)
            else:
                return (None)

        except Exception as e:
            logger.error(e, exc_info=True)
            print(e)
            return (None)

    
    def GetDataSample2(self, devicename, recorddate, recorddate2):
        try:
            container = {}

            sql = """
                    --GET DATA SAMPLE
                    SELECT
                        recordtime,
                        values
                    FROM trial_datasample_rooftop
                    WHERE devicename = %(devicename)s AND
                    CAST(recordtime as date) BETWEEN %(recorddate)s AND %(recorddate2)s  --'2020-08-05'
                    ORDER BY recordtime asc
            """

            params = {
                'devicename': devicename,
                'recorddate': recorddate,
                'recorddate2': recorddate2
            }

            #Execute
            ok, data, err = self.RunGeneralQuery(string_query=sql,
                                                params=params,
                                                types=4)

            if ok:

                # print(data)

                #FORMAT DATA
                for row in data:
                    # converted_datetime = datetime.datetime.strftime(row[0],"%Y-%m-%d %H:%M:%S.%f")
                    converted_datetime = row[0]
                    data_detail = [converted_datetime, float(row[1])]
                    container.update({str(row[0]): data_detail})

                print(container)
                return (container)
            else:
                return (None)

        except Exception as e:
            logger.error(e, exc_info=True)
            print(e)
            return (None)



# if __name__ == "__main__":
#     a = TempQuerySQL()