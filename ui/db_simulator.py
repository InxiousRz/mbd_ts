import json
import os

class DB_Sim():
    _db_data_main = ".\\ui\\db\\data_main.json"

    def __init__(self):
        pass    
    
    def delete_datadevicetest(self, key):

        #read db content
        if os.path.exists(self._db_data_main):
            with open(self._db_data_main, "r") as json_file:
                jsondata = json.load(json_file)
        else:
            #Create File
            jsondata = {}
            with open(self._db_data_main, "w+") as json_file:
                json.dump(jsondata, json_file, indent=4)

        #Remove an ID
        del jsondata[key]

        #Rewrite
        with open(self._db_data_main, "w+") as json_file:
            json.dump(jsondata, json_file)

    def insert_datadevicetest(self, insert_data):
        
        #read db content
        if os.path.exists(self._db_data_main):
            with open(self._db_data_main, "r") as json_file:
                jsondata = json.load(json_file)
        else:
            #Create File
            jsondata = {}
            with open(self._db_data_main, "w+") as json_file:
                json.dump(jsondata, json_file, indent=4)

        #Add an ID
        if len(jsondata) != 0:
            last_data_id = max([int(x) for x in list(jsondata.keys())]) + 1
        else:
            last_data_id = 1
        
        #Add ID to inner data too
        insert_data.update({"deviceattachid":str(last_data_id)})
        jsondata.update({str(last_data_id):insert_data})

        #Rewrite
        with open(self._db_data_main, "w+") as json_file:
            json.dump(jsondata, json_file)

    def update_datadevicetest(self, ids, insert_data):
        
        #read db content
        if os.path.exists(self._db_data_main):
            with open(self._db_data_main, "r") as json_file:
                jsondata = json.load(json_file)
        else:
            #Create File
            jsondata = {}
            with open(self._db_data_main, "w+") as json_file:
                json.dump(jsondata, json_file, indent=4)

        #Update an ID
        jsondata.update({str(ids):insert_data})

        #Rewrite
        with open(self._db_data_main, "w+") as json_file:
            json.dump(jsondata, json_file)


    def read_datadevicetest(self):

        #read db content
        if os.path.exists(self._db_data_main):
            with open(self._db_data_main, "r") as json_file:
                jsondata = json.load(json_file)
        else:
            #Create File
            jsondata = {}
            with open(self._db_data_main, "w+") as json_file:
                json.dump(jsondata, json_file)

        return (jsondata)




