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
from time import sleep
import threading

import logging
from ui.graph_generator import GraphGen
from ui.graph_generator2 import GraphGen2 

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




###########################################################################
## Class MyFrame1
###########################################################################

class OnRunUis ( wx.Frame ):

    def __init__( self ):
        self._Onrun_UI = wx.Frame(None, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 927,686 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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
        fgSizer7 = wx.FlexGridSizer( 6, 1, 0, 0 )
        fgSizer7.SetFlexibleDirection( wx.BOTH )
        fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText5 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Check Data Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.m_staticText5.SetForegroundColour( wx.Colour( 0, 128, 128 ) )

        fgSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )

        fgSizer81 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer81.SetFlexibleDirection( wx.BOTH )
        fgSizer81.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        m_radioBox1Choices = [ u"Single Day", u"Multiple Day" ]
        self.m_radioBox1 = wx.RadioBox( self.m_panel61, wx.ID_ANY, u"Choose Method", wx.DefaultPosition, wx.Size( 200,-1 ), m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox1.SetSelection( 1 )
        fgSizer81.Add( self.m_radioBox1, 0, wx.ALL, 5 )

        fgSizer7.Add( fgSizer81, 0, wx.ALL, 5 )

        ##============================================================== 111

        fgSizer420 = wx.FlexGridSizer( 1, 2, 0, 0 )
        fgSizer420.SetFlexibleDirection( wx.BOTH )
        fgSizer420.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        ##============================================================== 111

        ##============================================================================

        

        fgSizer92 = wx.FlexGridSizer( 1, 4, 0, 0 )
        fgSizer92.SetFlexibleDirection( wx.BOTH )
        fgSizer92.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText81 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"From", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText81.Wrap( -1 )

        fgSizer92.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.datepick_start = wx.adv.DatePickerCtrl( self.m_panel61, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN  )
        fgSizer92.Add( self.datepick_start, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"To", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        fgSizer92.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.datepick_end = wx.adv.DatePickerCtrl( self.m_panel61, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN  )
        fgSizer92.Add( self.datepick_end, 0, wx.ALL, 5 )

        fgSizer420.Add( fgSizer92, 1, wx.EXPAND, 5 )
        # fgSizer7.Add( fgSizer81, 1, wx.EXPAND, 5 )
        #==========================================================================================

        fgSizer91 = wx.FlexGridSizer( 3, 2, 0, 0 )
        fgSizer91.SetFlexibleDirection( wx.BOTH )
        fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText7 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Choose Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        fgSizer91.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.date_picker_01 = wx.adv.DatePickerCtrl( self.m_panel61, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN  )
        fgSizer91.Add( self.date_picker_01, 0, wx.ALL, 5 )


        fgSizer420.Add( fgSizer91, 1, wx.EXPAND, 5 )
        # fgSizer7.Add( fgSizer91, 1, wx.EXPAND, 5 )
        

        ##=====================================================================================

        fgSizer7.Add( fgSizer420, 1, wx.EXPAND, 5 )

        ##========================================================== 111

        fgSizer911 = wx.FlexGridSizer( 1, 2, 0, 0 )
        fgSizer911.SetFlexibleDirection( wx.BOTH )
        fgSizer911.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText8 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Choose Device", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        fgSizer911.Add( self.m_staticText8, 0, wx.ALL, 5 )

        devicelist_graphChoices = []
        self.devicelist_graph = wx.Choice( self.m_panel61, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,-1 ), devicelist_graphChoices, 0 )
        self.devicelist_graph.SetSelection( 0 )
        fgSizer911.Add( self.devicelist_graph, 0, wx.ALL, 5 )

        fgSizer7.Add( fgSizer911, 1, wx.EXPAND, 5 )

        self.cmd_generategraph = wx.Button( self.m_panel61, wx.ID_ANY, u"Generate Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer7.Add( self.cmd_generategraph, 0, wx.ALL, 5 )


        self.m_panel61.SetSizer( fgSizer7 )
        self.m_panel61.Layout()
        fgSizer7.Fit( self.m_panel61 )
        fgSizer2.Add( self.m_panel61, 1, wx.EXPAND |wx.ALL, 5 )


        ###

        self.m_panel5 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer1 = wx.GridSizer( 1, 2, 0, 0 )

        self.cmd_start6969 = wx.Button( self.m_panel5, wx.ID_ANY, u"START", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.cmd_start6969, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.cmd_stop6969 = wx.Button( self.m_panel5, wx.ID_ANY, u"STOP", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.cmd_stop6969, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel5.SetSizer( gSizer1 )
        self.m_panel5.Layout()
        gSizer1.Fit( self.m_panel5 )
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
        self.cmd_start6969.Bind( wx.EVT_BUTTON, self.StartRecord )
        self.cmd_stop6969.Bind( wx.EVT_BUTTON, self.StopRecord )
        self.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.setRadionewoption )



        self.cmd_stop6969.Disable()

        sleep(1)
        self.StartRecord(None)
        


    def threaded(fn):
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
            thread.setDaemon(True)
            thread.start()
            sleep(0.1)
            return (thread)

        return (wrapper)

        

    def __del__( self ):
        pass

    def setRadionewoption(self, event):
        selected_method = self.m_radioBox1.GetSelection()
        print(f"SELECTED >> {selected_method}")

        if selected_method == 0: #Single
            self.m_staticText81.Hide()
            self.m_staticText9.Hide()
            self.datepick_start.Hide()
            self.datepick_end.Hide()

            self.m_staticText7.Show()
            self.date_picker_01.Show()

        elif selected_method == 1: #Multiple
            self.m_staticText81.Show()
            self.m_staticText9.Show()
            self.datepick_start.Show()
            self.datepick_end.Show()

            self.m_staticText7.Hide()
            self.date_picker_01.Hide()

    @threaded
    def StartRecord(self, event):

        self.cmd_start6969.Disable()

        try:
            print("========================================")
            print("START RECORDING ========================")
            print("========================================")

            self._stoppedo_call = False
            self._stoppedo_confirm = {}
            self._stoppedo_confirm_record = False

            if self._startedo == False:
                self.DataReader()                
                self.DataRecorder()
                self.SaveJSONLoop()

            sleep(5)


            print("========================================")
            print("STARTING DONE ==========================")
            print("========================================")
        except Exception as e:
            logger.error(e, exc_info=True)
            self.StopRecord(None)
            self.cmd_start6969.Enable()
        else:
            self.cmd_stop6969.Enable()

    @threaded
    def StopRecord(self, event):

        self.cmd_stop6969.Disable()
        try:
            print("========================================")
            print("START STOPPING =========================")
            print("========================================")

            self._stoppedo_call = True

            #1
            stope = False
            while not stope:
                if len(self._stoppedo_confirm) == 0:
                    stope = True
                else:
                    values = list(self._stoppedo_confirm.values())
                    if True in values:
                        pass
                    else:
                        stope = True
                
                sleep(1)

            #2
            stope2 = False
            while not stope2:
                if self._stoppedo_confirm_record == True:
                    stope2 = True

                sleep(1)

            #3
            stope3 = False
            while not stope3:
                if self._stoppedo_confirm_record2 == True:
                    stope3 = True

                sleep(1)

            self._startedo = False
        
            print("========================================")
            print("STOPPING DONE ==========================")
            print("========================================")
        except Exception as e:
            logger.error(e, exc_info=True)
            self.cmd_stop6969.Enable()
        else:
            self.cmd_start6969.Enable()

    # @threaded
    def generatedagraph(self, event):

        
        selected_method = self.m_radioBox1.GetSelection()

        print(f"SELECTED TO GRAPH >> {selected_method}")

        if selected_method == 0: #Single

            # self.m_radioBox1.SetSelection()
            self.cmd_generategraph.Disable()

            dates = self.date_picker_01.GetValue() #8/10/2020 12:00:00 AM
            print(dates)
            dates = datetime.datetime.strptime(str(dates), "%m/%d/%Y %H:%M:%S")
            dates = str(dates.strftime("%Y-%m-%d"))
            devices = self.devicelist_graph.GetString(self.devicelist_graph.GetSelection())
            
            print(dates)
            print(devices)
            GraphGen(dates=dates,
                        lives=False,
                        devices=devices)

        elif selected_method == 1: #Multiple
            # self.m_radioBox1.SetSelection()
            self.cmd_generategraph.Disable()

            dates_a = self.datepick_start.GetValue() #8/10/2020 12:00:00 AM
            print(dates_a)
            dates_a = datetime.datetime.strptime(str(dates_a), "%m/%d/%Y %H:%M:%S")
            dates_a = str(dates_a.strftime("%Y-%m-%d"))

            dates_b = self.datepick_end.GetValue() #8/10/2020 12:00:00 AM
            print(dates_b)
            dates_b = datetime.datetime.strptime(str(dates_b), "%m/%d/%Y %H:%M:%S")
            dates_b = str(dates_b.strftime("%Y-%m-%d"))


            devices = self.devicelist_graph.GetString(self.devicelist_graph.GetSelection())
            
            print(dates_a)
            print(dates_b)
            print(devices)
            GraphGen2(dates_a=dates_a,
                        dates_b=dates_b,
                        devices=devices)

        self.cmd_generategraph.Enable()

    def Destroye(self, event):
        sys.exit(0)
    
    def OpenForms(self):
        self._Onrun_UI.Show()
        self.setRadionewoption(None)

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