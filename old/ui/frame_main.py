# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
from ui.db_simulator import DB_Sim as dbs
import sys

from ui.frame_inputdatamain import frame_inputdatamains

###########################################################################
## Class frame_main
###########################################################################

class frame_main( frame_inputdatamains ):

    def __init__( self, parent ):
        frame_inputdatamains.__init__(self,None)


        self._frame_main = wx.Frame(None, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 944,571 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self._frame_main.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self._frame_main.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        fgSizer1 = wx.FlexGridSizer( 0, 0, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_panel1 = wx.Panel( self._frame_main, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        fgSizer2 = wx.FlexGridSizer( 3, 0, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Device Communication Data", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        fgSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.dv_devicecomms = wx.dataview.DataViewListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 900,400 ), 0 )
        self.m_dataViewListColumn1 = self.dv_devicecomms.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn2 = self.dv_devicecomms.AppendTextColumn( u"Device Name", wx.dataview.DATAVIEW_CELL_INERT, 250, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn3 = self.dv_devicecomms.AppendTextColumn( u"Communication Type", wx.dataview.DATAVIEW_CELL_INERT, 150, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        
        self.m_dataViewListColumn211 = self.dv_devicecomms.AppendToggleColumn( u"deviceattachdetailid", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN )
        fgSizer2.Add( self.dv_devicecomms, 0, wx.ALL, 5 )

        gSizer1 = wx.GridSizer( 0, 5, 0, 0 )

        self.cmd_addtestdevice = wx.Button( self.m_panel1, wx.ID_ANY, u"Add Device Test", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.cmd_addtestdevice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.cmd_deletetestdevice = wx.Button( self.m_panel1, wx.ID_ANY, u"Delete Device Test", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.cmd_deletetestdevice, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.cmd_editmaindata = wx.Button( self.m_panel1, wx.ID_ANY, u"Edit Communication", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.cmd_editmaindata, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.cmd_refreshmaindata = wx.Button( self.m_panel1, wx.ID_ANY, u"Refresh Data", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.cmd_refreshmaindata, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.cmd_exit = wx.Button( self.m_panel1, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.cmd_exit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


        fgSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )


        self.m_panel1.SetSizer( fgSizer2 )
        self.m_panel1.Layout()
        fgSizer2.Fit( self.m_panel1 )
        fgSizer1.Add( self.m_panel1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self._frame_main.SetSizer( fgSizer1 )
        self._frame_main.Layout()

        self._frame_main.Centre( wx.BOTH )

        # Connect Events
        self._frame_main.Bind( wx.EVT_CLOSE, self.Exito )
        self.cmd_addtestdevice.Bind( wx.EVT_BUTTON, self.OpenAddTestDevicePanel )
        self.dv_devicecomms.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.SelectionChangesMain, id = wx.ID_ANY )
        self.cmd_editmaindata.Bind( wx.EVT_BUTTON, self.EditComm )
        self.cmd_deletetestdevice.Bind( wx.EVT_BUTTON, self.DeleteComm )
        self.cmd_refreshmaindata.Bind( wx.EVT_BUTTON, self.RefreshData )
        self.cmd_exit.Bind( wx.EVT_BUTTON, self.Exito )

        self.GetAllData()
        self.RefreshDvDataMain()
        self._frame_main.Show()

    def __del__( self ):
        pass

    def SelectionChangesMain(self, event):
        row = self.dv_devicecomms.GetSelectedRow()
        if row != -1:
            self.cmd_editmaindata.Enable()
            self.cmd_deletetestdevice.Enable()
        else:
            self.cmd_editmaindata.Disable()
            self.cmd_deletetestdevice.Disable()

    def RefreshDvDataMain(self):
        self.dv_devicecomms.DeleteAllItems()

        no = 1
        listing_order = list(self._data_main_all.keys())
        listing_order.sort()
        for ids in listing_order:
            data = self._data_main_all[ids]
            array_row = [no, str(data["devicename"]), str(data["comm_type"]), str(ids)]
            self.dv_devicecomms.AppendItem(array_row)
            no+=1

        self.SelectionChangesMain(None)


    def GetAllData(self):
        data = dbs().read_datadevicetest()
        self._data_main_all = data
        print(data)

    # Virtual event handlers, overide them in your derived class
    def OpenAddTestDevicePanel( self, event ):
        event.Skip()
        self._main_input_type = "A"
        self.cmd_step2.SetLabel("Save")
        self.ResetFormInput()
        self._frame_inputdatamaine.Show()

    def DeleteComm( self, event ):
        event.Skip()

        try:
            row = self.dv_devicecomms.GetSelectedRow()
        except Exception as e:
            wx.MessageBox(f"No Selected Row! \b {e}")
            return
        else:
            if row == -1:
                wx.MessageBox(f"No Selected Row!")
                return
            
            target = str(self.dv_devicecomms.GetValue(row=row, col=3))
            # print(target)

            try:
                #DELETE at DB
                dbs().delete_datadevicetest(key=target)
                self.GetAllData()
            except Exception as e:
                wx.MessageBox(f"Remove Failed, \n {e}")
            else:
                wx.MessageBox("Remove Success!")

            self.RefreshDvDataMain()

    def EditComm( self, event ):
        event.Skip()
        try:
            row = self.dv_devicecomms.GetSelectedRow()
        except Exception as e:
            wx.MessageBox(f"No Selected Row! \b {e}")
            return
        else:
            if row == -1:
                wx.MessageBox(f"No Selected Row!")
                return
            
            target = str(self.dv_devicecomms.GetValue(row=row, col=3))
            
            #Agent
            self._main_edit_target_ids = target
            self._main_input_type = "E"

            #Add Value
            datas = self._data_main_all[target] 
            self.txt_device_name.SetValue(datas["devicename"])
            self.txt_selected_slave_id.SetValue(datas["slave_id"])
            self.txt_com_port.SetValue(datas["port"])
            self.txt_decimal_point.SetValue(int(datas["decimal_point"]))
            self.txt_readinterval.SetValue(str(datas["read_interval"]))
            if datas["comm_type"] == "B":
                self.txt_modbus_type.SetSelection(1)
            else:
                self.txt_modbus_type.SetSelection(0)

            self._associated_registers = datas["register_data"]
            self.cmd_step2.SetLabel("Update")
            self.RefreshDvInputDataMainRegister()
            

            self._frame_inputdatamaine.Show()

    def RefreshData( self, event ):
        event.Skip()

        self.GetAllData()
        self.RefreshDvDataMain()

        wx.MessageBox("Refresh Success!")

    def Exito( self, event ):
        event.Skip()
        sys.exit()


