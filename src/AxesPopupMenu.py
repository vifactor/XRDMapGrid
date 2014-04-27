import wx
import numpy as np

class AxesPopupMenu(wx.Menu):
    def __init__(self, axes):
        wx.Menu.__init__(self)
        
        self.axes = axes
        
        item = wx.MenuItem(self, wx.NewId(), "Plot")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.onPlot, item)
        
        item = wx.MenuItem(self, wx.NewId(), "Clear")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.onClear, item)
        
    def onPlot(self, event):
        x = np.arange(0, 6, 0.01)
        a = np.random.random(1)
        y = np.sin(x**2)*np.exp(-a * x)
        self.axes.plot(x, y)
        
    def onClear(self, event):
        self.axes.clear()
