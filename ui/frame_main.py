# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
# Class frame_main
###########################################################################


class frame_main (wx.Frame):

    def __init__(self, parent):
        self._frame_main = wx.Frame(None, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            944, 571), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self._frame_main.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self._frame_main.SetBackgroundColour(wx.Colour(255, 255, 255))

        fgSizer1 = wx.FlexGridSizer(0, 0, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_panel1 = wx.Panel(
            self._frame_main, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        fgSizer2 = wx.FlexGridSizer(3, 0, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(
            self.m_panel1, wx.ID_ANY, u"Device Communication Data", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        self.m_staticText1.SetFont(wx.Font(
            16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        fgSizer2.Add(self.m_staticText1, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.dv_devicecomms = wx.dataview.DataViewListCtrl(
            self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(900, 400), 0)
        self.m_dataViewListColumn1 = self.dv_devicecomms.AppendTextColumn(
            u"No", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn2 = self.dv_devicecomms.AppendTextColumn(
            u"Device Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn3 = self.dv_devicecomms.AppendTextColumn(
            u"Communication", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.m_dataViewListColumn13 = self.dv_devicecomms.AppendTextColumn(
            u"devcommid", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN)
        self.m_dataViewListColumn20 = self.dv_devicecomms.AppendTextColumn(
            u"deviceattachdetailid", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_HIDDEN)
        fgSizer2.Add(self.dv_devicecomms, 0, wx.ALL, 5)

        gSizer1 = wx.GridSizer(0, 3, 0, 0)

        self.cmd_editmaindata = wx.Button(
            self.m_panel1, wx.ID_ANY, u"Edit Communication", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.cmd_editmaindata, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.cmd_refreshmaindata = wx.Button(
            self.m_panel1, wx.ID_ANY, u"Refresh Data", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.cmd_refreshmaindata, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.cmd_exit = wx.Button(
            self.m_panel1, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.cmd_exit, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer2.Add(gSizer1, 1, wx.EXPAND, 5)

        self.m_panel1.SetSizer(fgSizer2)
        self.m_panel1.Layout()
        fgSizer2.Fit(self.m_panel1)
        fgSizer1.Add(self.m_panel1, 1,
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self._frame_main.SetSizer(fgSizer1)
        self._frame_main.Layout()

        self._frame_main.Centre(wx.BOTH)

        # Connect Events
        self.cmd_editmaindata.Bind(wx.EVT_BUTTON, self.EditComm)
        self.cmd_refreshmaindata.Bind(wx.EVT_BUTTON, self.RefreshData)
        self.cmd_exit.Bind(wx.EVT_BUTTON, self.Exito)

        self._frame_main.Show()

    def __del__(self):
        pass

    def LoadData(self):
        self.dv_devicecomms.AppendItem()

    # Virtual event handlers, overide them in your derived class
    def EditComm(self, event):
        event.Skip()

    def RefreshData(self, event):
        event.Skip()

    def Exito(self, event):
        event.Skip()
