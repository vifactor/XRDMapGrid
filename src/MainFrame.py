# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Sun Apr 27 16:04:31 2014

import wx
from AxesGridDialog import AxesGridDialog

# begin wxGlade: dependencies
from MplPanel import MplPanel
# end wxGlade

# begin wxGlade: extracode

# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.menubar = wx.MenuBar()
        self.File = wx.Menu()
        self.Exit = wx.MenuItem(self.File, wx.ID_EXIT, "E&xit", "Terminate the program", wx.ITEM_NORMAL)
        self.File.AppendItem(self.Exit)
        self.menubar.Append(self.File, "&File")
        self.Options = wx.Menu()
        self.SetGrid = wx.MenuItem(self.Options, wx.ID_ANY, "Set grid", "Defined the size of the grid grid", wx.ITEM_NORMAL)
        self.Options.AppendItem(self.SetGrid)
        self.menubar.Append(self.Options, "&Options")
        self.Help = wx.Menu()
        self.About = wx.MenuItem(self.Help, wx.ID_ABOUT, "&About", "Information about this program", wx.ITEM_NORMAL)
        self.Help.AppendItem(self.About)
        self.menubar.Append(self.Help, "&Help")
        self.SetMenuBar(self.menubar)
        # Menu Bar end
        self.mplPanel = MplPanel(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.onExit, self.Exit)
        self.Bind(wx.EVT_MENU, self.onSetGrid, self.SetGrid)
        self.Bind(wx.EVT_MENU, self.onAbout, self.About)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("Main Window")
        self.SetSize((650, 490))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.mplPanel, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer)
        self.Layout()
        # end wxGlade
        
    def onAbout(self, event):  # wxGlade: MainFrame.<event_handler>
        #Create a message dialog box
        dlg = wx.MessageDialog(self, "XRD MapGrid v0.1\nAuthor: Viktor Kopp", "XRD", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def onExit(self, event):  # wxGlade: MainFrame.<event_handler>
        self.Close(True)

    def onSetGrid(self, event):  # wxGlade: MainFrame.<event_handler>
        dialog = AxesGridDialog(self)
        
        if dialog.ShowModal() == wx.ID_OK:
            nr = int(dialog.scNbRows.GetValue())
            nc = int(dialog.scNbColumns.GetValue())
            self.mplPanel.set_grid(nr, nc)
            print "%s x %s grid has been defined" % (nr, nc)
        
        dialog.Destroy()

# end of class MainFrame
