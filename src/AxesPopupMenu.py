import wx

class AxesPopupMenu(wx.Menu):
    def __init__(self, axes):
        wx.Menu.__init__(self)
        
        self.axes = axes
        
        item = wx.MenuItem(self, wx.NewId(), "Item One")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.onItem1, item)
        
    def onItem1(self, event):
        print "Item1 has been chosen", self.axes
