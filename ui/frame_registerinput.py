# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from db_simulator import DB_Sim as dbs



###########################################################################
## Class frame_register_input
###########################################################################

class frame_register_input ( ):

	def __init__( self, parent ):
		self._frame_registerinput = wx.Frame( parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 652,368 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self._frame_registerinput.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self._frame_registerinput.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer13 = wx.GridSizer( 0, 0, 0, 0 )

		self.m_panel10 = wx.Panel( self._frame_registerinput, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer18 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dkjskdjskdj = wx.StaticText( self.m_panel10, wx.ID_ANY, u"INPUT REGISTER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dkjskdjskdj.Wrap( -1 )

		self.dkjskdjskdj.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		fgSizer18.Add( self.dkjskdjskdj, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel11 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer21 = wx.FlexGridSizer( 6, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer21.SetMinSize( wx.Size( 600,200 ) )
		self.m_staticText18 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Sequence", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		fgSizer21.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt_sequenceregister = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.txt_sequenceregister, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		
		fgSizer21.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt_address_inputregister = wx.SpinCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 255, 0 )
		fgSizer21.Add( self.txt_address_inputregister, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText20 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Alias", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		fgSizer21.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt_alias_inputregister = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer21.Add( self.txt_alias_inputregister, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel11.SetSizer( fgSizer21 )
		self.m_panel11.Layout()
		fgSizer21.Fit( self.m_panel11 )
		fgSizer18.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

		fgSizer19 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer19.SetFlexibleDirection( wx.BOTH )
		fgSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.cmd_saveinputregister = wx.Button( self.m_panel10, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.cmd_saveinputregister, 0, wx.ALL, 5 )

		self.cmd_cancelinputregister = wx.Button( self.m_panel10, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer19.Add( self.cmd_cancelinputregister, 0, wx.ALL, 5 )


		fgSizer18.Add( fgSizer19, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel10.SetSizer( fgSizer18 )
		self.m_panel10.Layout()
		fgSizer18.Fit( self.m_panel10 )
		gSizer13.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )


		self._frame_registerinput.SetSizer( gSizer13 )
		self._frame_registerinput.Layout()

		self._frame_registerinput.Centre( wx.BOTH )

		# Connect Events
		self.cmd_saveinputregister.Bind( wx.EVT_BUTTON, self.SaveRegisterData )
		self.cmd_cancelinputregister.Bind( wx.EVT_BUTTON, self.CancelInputDataRegister )

	def __del__( self ):
		pass
		


	# Virtual event handlers, overide them in your derived class
	def SaveRegisterData( self, event ):
		event.Skip()

		seq = self.txt_sequenceregister.GetValue()

		if self._register_input_mode == "A":
			if seq in [int(x) for x in list(self._associated_registers.keys())]:
				wx.MessageBox("Sequence sudah ada!")
				return
			else:
				data = {
					"sequence":self.txt_sequenceregister.GetValue(),
					"register_address":self.txt_address_inputregister.GetValue(),
					"register_alias":self.txt_alias_inputregister.GetValue()
				}
				self._associated_registers.update({str(seq):data})

			wx.MessageBox("Add Register Success!")
		else:
			if int(self.txt_sequenceregister.GetValue()) != int(self._register_edit_seq):
				if self._associated_registers.get(str(self.txt_sequenceregister)) != None:
					wx.MessageBox("Sequence sudah ada!")
					return
			
			data = {
					"sequence":self.txt_sequenceregister.GetValue(),
					"register_address":self.txt_address_inputregister.GetValue(),
					"register_alias":self.txt_alias_inputregister.GetValue()
				}
			self._associated_registers.update({str(seq):data})

			wx.MessageBox("Update Register Success!")

		self.RefreshDvInputDataMainRegister()

		self._frame_registerinput.Hide()
		

	def CancelInputDataRegister( self, event ):
		self._frame_registerinput.Hide()


