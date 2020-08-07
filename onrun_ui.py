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
import sys
import wx.adv
import datetime

from ui.graph_generator import GraphGen

###########################################################################
## Class MyFrame1
###########################################################################

class OnRunUis ( wx.Frame ):

    def __init__( self ):
        self._Onrun_UI = wx.Frame(None, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 927,556 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self._Onrun_UI.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self._Onrun_UI.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText1 = wx.StaticText( self._Onrun_UI, wx.ID_ANY, u"Modbus Data Sampling", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )
        self.m_staticText1.SetForegroundColour( wx.Colour( 0, 64, 128 ) )
        self.m_staticText1.SetBackgroundColour( wx.Colour( 244, 244, 244 ) )

        fgSizer1.Add( self.m_staticText1, 0, wx.EXPAND, 5 )

        self.m_panel1 = wx.Panel( self._Onrun_UI, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer2 = wx.FlexGridSizer( 3, 1, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_panel2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer3 = wx.FlexGridSizer( 1, 2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_panel6 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer8 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer8.SetFlexibleDirection( wx.BOTH )
        fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText2 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Read Data", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_staticText2.SetForegroundColour( wx.Colour( 0, 128, 255 ) )

        fgSizer8.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.dv_data = wx.dataview.DataViewListCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,250 ), 0 )
        self.dv_col_nama = self.dv_data.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, 240, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        self.dv_col_value = self.dv_data.AppendTextColumn( u"Average Value", wx.dataview.DATAVIEW_CELL_INERT, 150, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
        fgSizer8.Add( self.dv_data, 0, wx.ALL, 5 )
        

        self.m_panel6.SetSizer( fgSizer8 )
        self.m_panel6.Layout()
        fgSizer8.Fit( self.m_panel6 )
        fgSizer3.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel7 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer9 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer9.SetFlexibleDirection( wx.BOTH )
        fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText3 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Read Log", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_staticText3.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        fgSizer9.Add( self.m_staticText3, 0, wx.ALL, 5 )

        lb_readlogChoices = []
        self.lb_readlog = wx.ListBox( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.Size( 450,250 ), lb_readlogChoices, wx.LB_ALWAYS_SB )
        fgSizer9.Add( self.lb_readlog, 0, wx.ALL, 5 )
        
        

        self.m_panel7.SetSizer( fgSizer9 )
        self.m_panel7.Layout()
        fgSizer9.Fit( self.m_panel7 )
        fgSizer3.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel2.SetSizer( fgSizer3 )
        self.m_panel2.Layout()
        fgSizer3.Fit( self.m_panel2 )
        fgSizer2.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

        ###
        
        self.m_panel61 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer7 = wx.FlexGridSizer( 3, 1, 0, 0 )
        fgSizer7.SetFlexibleDirection( wx.BOTH )
        fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText5 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Check Data Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.m_staticText5.SetForegroundColour( wx.Colour( 0, 128, 128 ) )

        fgSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )

        fgSizer91 = wx.FlexGridSizer( 3, 2, 0, 0 )
        fgSizer91.SetFlexibleDirection( wx.BOTH )
        fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText7 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Choose Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        fgSizer91.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.date_picker_01 = wx.adv.DatePickerCtrl( self.m_panel61, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN  )
        fgSizer91.Add( self.date_picker_01, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Choose Device", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        fgSizer91.Add( self.m_staticText8, 0, wx.ALL, 5 )

        devicelist_graphChoices = []
        self.devicelist_graph = wx.Choice( self.m_panel61, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,-1 ), devicelist_graphChoices, 0 )
        self.devicelist_graph.SetSelection( 0 )
        fgSizer91.Add( self.devicelist_graph, 0, wx.ALL, 5 )


        fgSizer7.Add( fgSizer91, 1, wx.EXPAND, 5 )

        self.cmd_generategraph = wx.Button( self.m_panel61, wx.ID_ANY, u"Generate Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer7.Add( self.cmd_generategraph, 0, wx.ALL, 5 )


        self.m_panel61.SetSizer( fgSizer7 )
        self.m_panel61.Layout()
        fgSizer7.Fit( self.m_panel61 )
        fgSizer2.Add( self.m_panel61, 1, wx.EXPAND |wx.ALL, 5 )


        ###

        self.m_panel5 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer10 = wx.FlexGridSizer( 1, 1, 0, 0 )
        fgSizer10.SetFlexibleDirection( wx.BOTH )
        fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.txt_notif = wx.StaticText( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt_notif.Wrap( -1 )

        fgSizer10.Add( self.txt_notif, 0, wx.ALL, 5 )


        self.m_panel5.SetSizer( fgSizer10 )
        self.m_panel5.Layout()
        fgSizer10.Fit( self.m_panel5 )
        fgSizer2.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel1.SetSizer( fgSizer2 )
        self.m_panel1.Layout()
        fgSizer2.Fit( self.m_panel1 )
        fgSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


        self._Onrun_UI.SetSizer( fgSizer1 )
        self._Onrun_UI.Layout()

        self._Onrun_UI.Centre( wx.BOTH )

        # Connect Events
        self._Onrun_UI.Bind( wx.EVT_CLOSE, self.Destroye )
        self.cmd_generategraph.Bind( wx.EVT_BUTTON, self.generatedagraph )


        

    def __del__( self ):
        pass
    
    def generatedagraph(self, event):
        dates = self.date_picker_01.GetValue() #8/10/2020 12:00:00 AM
        dates = datetime.datetime.strptime(str(dates), "%m/%d/%Y %H:%M:%S %p")
        dates = str(dates.strftime("%Y-%m-%d"))
        devices = self.devicelist_graph.GetString(self.devicelist_graph.GetSelection())
        
        print(dates)
        print(devices)
        GraphGen(dates=dates,
                    lives=False,
                    devices=devices)

    def Destroye(self, event):
        sys.exit(0)
    
    def OpenForms(self):
        self._Onrun_UI.Show()

    def AddItemToLb(self, texts):
        if self.lb_readlog.GetCount() >= 200:
            self.lb_readlog.Clear()

        self.lb_readlog.Append(f"{texts}")
        self.lb_readlog.SetSelection(self.lb_readlog.GetCount()-1)

    def SetDvItem(self, item_list):

        self.dv_data.DeleteAllItems()

        self._items_map = []
        for item in item_list:
            self._items_map.append(item)
            self.dv_data.AppendItem([item,""])

        self.devicelist_graph.SetItems(item_list)
        if len(item_list) != 0:
            self.devicelist_graph.SetSelection(0)

    def UpdateDvItem(self, devicename, value):
        self.dv_data.SetTextValue(value=value,row=self._items_map.index(devicename),col=1)