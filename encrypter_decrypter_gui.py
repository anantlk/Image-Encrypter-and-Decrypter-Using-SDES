# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

actual_path='';


def findAllOccurences(ch,path):
	return [i for i,letter in enumerate(path) if letter==ch]
	
###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Image Encrypter", pos = wx.DefaultPosition, size = wx.Size( 403,316 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Image Encrypter And Decrypter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 12, 75, 90, 92, False, "Lucida Sans Typewriter" ) )
		self.m_staticText1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_staticText1.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		gbSizer1.Add( self.m_staticText1, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.file_path = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE )
		gbSizer1.Add( self.file_path, wx.GBPosition( 5, 4 ), wx.GBSpan( 1, 1 ), wx.ALIGN_BOTTOM|wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALIGN_RIGHT|wx.ALIGN_TOP|wx.ALL|wx.BOTTOM|wx.LEFT|wx.TOP, 5 )
		
		self.encrypt = wx.Button( self, wx.ID_ANY, u"Encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.encrypt, wx.GBPosition( 7, 0 ), wx.GBSpan( 4, 11 ), wx.ALIGN_CENTER|wx.ALIGN_TOP|wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 2 )
		
		self.decrypt = wx.Button( self, wx.ID_ANY, u"Decrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.decrypt, wx.GBPosition( 11, 0 ), wx.GBSpan( 4, 11 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 1 )
		
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.encrypt.Bind( wx.EVT_BUTTON, self.encryption )
		self.decrypt.Bind( wx.EVT_BUTTON, self.decryption )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def encryption( self, event ):
		try:
			path=self.file_path.GetPath();
			pos_arr=findAllOccurences("\\",path)
			path=list(path)
			for i in range(len(pos_arr)):
				path.insert(pos_arr[i]+i,"\\")
			print("".join(path))
		except Exception:
			print("Error in Encryption")
	
	def decryption( self, event ):
		try:		
			path=self.file_path.GetPath();
			pos_arr=findAllOccurences("\\",path)
			path=list(path)
			for i in range(len(pos_arr)):
				path.insert(pos_arr[i]+i,"\\")
			print("".join(path))
		except Exception:
			print("Error in Decryption");
	




if __name__ == "__main__":
	app = wx.App(False)
	frame = MainFrame(None)
	frame.Show()
	app.MainLoop()
	
