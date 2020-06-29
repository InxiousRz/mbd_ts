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
from db_simulator import DB_Sim as dbs


from frame_registerinput import frame_register_input

###########################################################################
## Class frame_edit2
###########################################################################

class frame_inputdatamains (frame_register_input):

    def __init__( self, parent ):
        frame_register_input.__init__(self,None)
        self._associated_registers = {}




        self._frame_inputdatamaine = wx.Frame(  parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 756,655 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self._frame_inputdatamaine.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self._frame_inputdatamaine.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        gSizer6 = wx.GridSizer( 0, 0, 0, 0 )

        self.m_panel4 = wx.Panel( self._frame_inputdatamaine, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer5 = wx.FlexGridSizer( 4, 0, 0, 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText6 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"INPUT DATA MODBUS COMMUNICATION", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        self.m_staticText6.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        fgSizer5.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_panel5 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer25 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer25.SetFlexibleDirection( wx.BOTH )
        fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_panel16 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel16.SetBackgroundColour( wx.Colour( 155, 205, 255 ) )

        fgSizer29 = wx.FlexGridSizer( 4, 2, 0, 0 )
        fgSizer29.SetFlexibleDirection( wx.BOTH )
        fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        fgSizer29.SetMinSize( wx.Size( 700,-1 ) )
        self.m_staticText24 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Device Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )

        self.m_staticText24.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        fgSizer29.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt_device_name = wx.TextCtrl( self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
        fgSizer29.Add( self.txt_device_name, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel16.SetSizer( fgSizer29 )
        self.m_panel16.Layout()
        fgSizer29.Fit( self.m_panel16 )
        fgSizer25.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel15 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer6 = wx.FlexGridSizer( 4, 2, 0, 0 )
        fgSizer6.SetFlexibleDirection( wx.BOTH )
        fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        fgSizer6.SetMinSize( wx.Size( 700,-1 ) )
        self.m_staticText7 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Slave ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        self.m_staticText7.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        fgSizer6.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer7.SetFlexibleDirection( wx.BOTH )
        fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.txt_selected_slave_id = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer7.Add( self.txt_selected_slave_id, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        fgSizer6.Add( fgSizer7, 1, wx.EXPAND, 5 )

        self.m_staticText26 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Com Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )

        self.m_staticText26.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        fgSizer6.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.txt_com_port = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer6.Add( self.txt_com_port, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText8 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Choose Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        self.m_staticText8.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        fgSizer6.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        txt_modbus_typeChoices = [ u"A", u"B" ]
        self.txt_modbus_type = wx.Choice( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, txt_modbus_typeChoices, 0 )
        self.txt_modbus_type.SetSelection( 0 )
        fgSizer6.Add( self.txt_modbus_type, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText9 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Decimal Point", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        self.m_staticText9.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        fgSizer6.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer8.SetFlexibleDirection( wx.BOTH )
        fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.txt_decimal_point = wx.SpinCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        fgSizer8.Add( self.txt_decimal_point, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText10 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"x 10", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        fgSizer8.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        fgSizer6.Add( fgSizer8, 1, wx.EXPAND, 5 )


        self.m_panel15.SetSizer( fgSizer6 )
        self.m_panel15.Layout()
        fgSizer6.Fit( self.m_panel15 )
        fgSizer25.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel5.SetSizer( fgSizer25 )
        self.m_panel5.Layout()
        fgSizer25.Fit( self.m_panel5 )
        fgSizer5.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel6 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer9 = wx.FlexGridSizer( 3, 0, 0, 0 )
        fgSizer9.SetFlexibleDirection( wx.BOTH )
        fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        fgSizer9.SetMinSize( wx.Size( -1,250 ) )
        self.m_staticText11 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Associated Registers", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        self.m_staticText11.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.m_staticText11.SetForegroundColour( wx.Colour( 0, 128, 255 ) )

        fgSizer9.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.dv_associatedregister = wx.dataview.DataViewListCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,150 ), 0 )
        self.m_dataViewListColumn4 = self.dv_associatedregister.AppendTextColumn( u"No", wx.dataview.DATAVIEW_CELL_INERT, 50, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn5 = self.dv_associatedregister.AppendTextColumn( u"Sequence", wx.dataview.DATAVIEW_CELL_INERT, 150, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn6 = self.dv_associatedregister.AppendTextColumn( u"Alias", wx.dataview.DATAVIEW_CELL_INERT, 200, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.m_dataViewListColumn7 = self.dv_associatedregister.AppendTextColumn( u"Register Address", wx.dataview.DATAVIEW_CELL_INERT, 200, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        # self.m_dataViewListColumn12 = self.dv_associatedregister.AppendTextColumn( u"associatedid", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN )
        fgSizer9.Add( self.dv_associatedregister, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        fgSizer10 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer10.SetFlexibleDirection( wx.BOTH )
        fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.cmd_addassociatedregister = wx.Button( self.m_panel6, wx.ID_ANY, u"Add Registers", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer10.Add( self.cmd_addassociatedregister, 0, wx.ALL, 5 )

        self.cmd_editassociatedregister = wx.Button( self.m_panel6, wx.ID_ANY, u"Edit Registers", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer10.Add( self.cmd_editassociatedregister, 0, wx.ALL, 5 )

        self.cmd_removeassociatedregister = wx.Button( self.m_panel6, wx.ID_ANY, u"Remove Registers", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer10.Add( self.cmd_removeassociatedregister, 0, wx.ALL, 5 )


        fgSizer9.Add( fgSizer10, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.m_panel6.SetSizer( fgSizer9 )
        self.m_panel6.Layout()
        fgSizer9.Fit( self.m_panel6 )
        fgSizer5.Add( self.m_panel6, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

        self.cmd_step2 = wx.Button( self.m_panel4, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer7.Add( self.cmd_step2, 0, wx.ALL, 5 )

        self.cmd_cancel2 = wx.Button( self.m_panel4, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer7.Add( self.cmd_cancel2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        fgSizer5.Add( gSizer7, 1, wx.EXPAND, 5 )


        self.m_panel4.SetSizer( fgSizer5 )
        self.m_panel4.Layout()
        fgSizer5.Fit( self.m_panel4 )
        gSizer6.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


        self._frame_inputdatamaine.SetSizer( gSizer6 )
        self._frame_inputdatamaine.Layout()

        self._frame_inputdatamaine.Centre( wx.BOTH )

        #Start
        self.cmd_removeassociatedregister.Disable()
        self.cmd_editassociatedregister.Disable()

        # Connect Events
        self.dv_associatedregister.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.SelectionChanges, id = wx.ID_ANY )
        self.cmd_addassociatedregister.Bind( wx.EVT_BUTTON, self.OpenRegisterPanel )
        self.cmd_editassociatedregister.Bind( wx.EVT_BUTTON, self.OpenRegisterPanelE )
        self.cmd_removeassociatedregister.Bind( wx.EVT_BUTTON, self.RemoveAssociatedRegister )
        self.cmd_step2.Bind( wx.EVT_BUTTON, self.GO_step2 )
        self.cmd_cancel2.Bind( wx.EVT_BUTTON, self.GOCancel_2 )

        # self._frame_inputdatamaine.Show()
        

    def __del__( self ):
        pass

    # def RefreshDvInputDataMain(self):
    #     pass

    def ResetFormInput(self):
        self.txt_device_name.SetValue("")
        self.txt_selected_slave_id.SetValue("")
        self.txt_com_port.SetValue("")
        self.txt_decimal_point.SetValue(0)
        self.txt_modbus_type.SetSelection(0)

        self._associated_registers = {}
        self.RefreshDvInputDataMainRegister()

    def SelectionChanges(self, event):
        row = self.dv_associatedregister.GetSelectedRow()
        if row != -1:
            self.cmd_removeassociatedregister.Enable()
            self.cmd_editassociatedregister.Enable()
        else:
            self.cmd_removeassociatedregister.Disable()
            self.cmd_editassociatedregister.Disable()


    def RefreshDvInputDataMainRegister(self):
        self.dv_associatedregister.DeleteAllItems()
        no = 1
        listing_order = list(self._associated_registers.keys())
        listing_order.sort()
        for ids in listing_order:
            data = self._associated_registers[ids]
            array_row = [no, str(data["sequence"]), str(data["register_alias"]), str(data["register_address"])]
            self.dv_associatedregister.AppendItem(array_row)
            no+=1

        self.SelectionChanges(None)

    # Virtual event handlers, overide them in your derived class
    def OpenRegisterPanel( self, event ):
        event.Skip()

        self._register_input_mode = "A"

        self.txt_sequenceregister.Clear()
        self.txt_address_inputregister.SetValue(0)
        self.txt_alias_inputregister.Clear()
        self.cmd_saveinputregister.SetLabel("Save")

        self._frame_registerinput.Show()

    def OpenRegisterPanelE( self, event ):
        event.Skip()

        try:
            row = self.dv_associatedregister.GetSelectedRow()
        except Exception as e:
            wx.MessageBox(f"No Selected Row! \b {e}")
            return
        else:
            if row == -1:
                wx.MessageBox(f"No Selected Row!")
                return
            
            target = str(self.dv_associatedregister.GetValue(row=row, col=1))

        self._register_input_mode = "E"
        self._register_edit_seq = self._associated_registers[target]["sequence"]

        self.txt_sequenceregister.SetValue(self._associated_registers[target]["sequence"])
        self.txt_address_inputregister.SetValue(int(self._associated_registers[target]["register_address"]))
        self.txt_alias_inputregister.SetValue(self._associated_registers[target]["register_alias"])

        self.cmd_saveinputregister.SetLabel("Update")

        self._frame_registerinput.Show()

    def RemoveAssociatedRegister( self, event ):
        event.Skip()
        try:
            row = self.dv_associatedregister.GetSelectedRow()
        except Exception as e:
            wx.MessageBox(f"No Selected Row! \b {e}")
            return
        else:
            if row == -1:
                wx.MessageBox(f"No Selected Row!")
                return
            
            target = str(self.dv_associatedregister.GetValue(row=row, col=1))
            # print(target)
            if self._associated_registers.get(target) != None:
                del self._associated_registers[target]

                wx.MessageBox("Remove Success!")
            else:
                wx.MessageBox(f"Remove Failed, No {target} in tabledata")

            self.RefreshDvInputDataMainRegister()
            

    def GO_step2( self, event ):
        event.Skip()
    
        if len(self._associated_registers) == 0:
            wx.MessageBox("associated register empty")
            return

        inserts = {
            "devicename":self.txt_device_name.GetValue(),
            "slave_id":self.txt_selected_slave_id.GetValue(),
            "port":self.txt_com_port.GetValue(),
            "comm_type":self.txt_modbus_type.GetString(self.txt_modbus_type.GetSelection()),
            "decimal_point":self.txt_decimal_point.GetValue(),
            # "active":True,
            "register_data":self._associated_registers,
        }
        
        if self._main_input_type == "A":
            data = dbs().insert_datadevicetest(inserts)
            wx.MessageBox("Save Success!")
        elif self._main_input_type == "E":
            key = self._main_edit_target_ids
            data = dbs().update_datadevicetest(key,inserts)
            wx.MessageBox("Update Success!")
        else:
            wx.MessageBox("Something Wrong!")

        
        self.GetAllData()

        self.RefreshDvDataMain()
        self._main_edit_target_ids = None
        
        self._frame_inputdatamaine.Hide()


    def GOCancel_2( self, event ):
        event.Skip()

        self._frame_inputdatamaine.Hide()


