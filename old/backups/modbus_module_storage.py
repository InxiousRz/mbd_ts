## Outer Module
# from sub_modules.api_mod import ApiBridge

## Inner Member


class Modbus_Mod_Storage():
    def __init__(self, sobject_class):

        self._sobject_class = sobject_class
        self._ApiBridge = ApiBridge()

        self.LoadRequiredData()

        pass

    # Real Case
    ##=======================================================================================================
    def LoadRequiredData(self):
        self._modbus_devices = {}
        self._DeviceValues_Filtered = self._sobject_class._G_DeviceValues_Filtered
        self._DeviceAttachedMap_byID, self._DeviceAttachedMap_byKeyword, self._DeviceAttachedData_Full = self.LoadDeviceAttach(
        )

    def LoadDeviceAttach(self):

        mapping_id = self._sobject_class._G_DeviceAttachedMap_byID
        mapping_keyword = self._sobject_class._G_DeviceAttachedMap_byKeyword
        container_datafull = self._sobject_class._G_DeviceAttachedData_Full

        return (mapping_id, mapping_keyword, container_datafull)
