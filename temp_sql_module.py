import psycopg2
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

class TempQuerySQL():
    def __init__(self):
        self._DB_CONN = self.CreateConnection()

    def CreateConnection(self):

        conn = psycopg2.connect(
            dbname="agrotechdb",
            user="postgres",
            password="PharmaLogic",
            host="agrotech.cbyoam1fda2f.ap-southeast-1.rds.amazonaws.com",
            port="5432")
        return (conn)

    ## ACTUAL QUERIES
    ##===============================================================================

    def InsertDataSample(self, devicename, recordtime, values):
        

        #Execute
        try:
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
            
            cur = self._DB_CONN.cursor()
            cur.execute(sql, params)
        except Exception as e:
            logger.error(e, exc_info=True)
            self._DB_CONN.rollback()
        else:
            self._DB_CONN.commit()

        cur.close()

    def InsertError(self, error_type, devicename, recordtime, detailed_error):
        
        #Execute
        try:
            sql = """
                    --INSERT ERROR
                    INSERT INTO trial_error_rooftop(error_type, devicename, recordtime, detailed_error)
                    VALUES(%(error_type)s, %(devicename)s, %(recordtime)s, %(detailed_error)s)
            """

            params = {
                'devicename': devicename,
                'recordtime': recordtime,
                'error_type': error_type,
                'detailed_error': detailed_error,
            }

            cur = self._DB_CONN.cursor()
            cur.execute(sql, params)
        except Exception as e:
            logger.error(e, exc_info=True)
            self._DB_CONN.rollback()
        else:
            self._DB_CONN.commit()

        cur.close()


# if __name__ == "__main__":
#     a = TempQuerySQL()