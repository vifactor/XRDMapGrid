import wx
import os
import numpy as np
import xrayutilities as xu

class AxesPopupMenu(wx.Menu):
    def __init__(self, axes):
        wx.Menu.__init__(self)
        
        self.axes = axes
        
        item = wx.MenuItem(self, wx.ID_OPEN, "Load file...")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.onLoad, item)
        
        item = wx.MenuItem(self, wx.ID_CLEAR, "Clear")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.onClear, item)
        
        item = wx.MenuItem(self, wx.ID_PREFERENCES, "Preferences...")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.onSetPreferences, item)
        
    def onLoad(self, event):
        dlg = wx.FileDialog(None, "Choose a file", "", "", "*.xrdml", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            #destroy dialog
            dlg.Destroy()
            
            #read xrdml datafile
            om, tt, psd = xu.io.getxrdml_map(path)
                    
            gridder = xu.Gridder2D(150,150)
            gridder(om, tt, psd)
            INT = xu.maplog(gridder.data.transpose(),6,0)

            #clear axes from previous drawing
            self.axes.clear()

            #draw rsm
            cf = self.axes.contourf(gridder.xaxis, gridder.yaxis,INT,100,extend='min')

            #annotate axes
            self.axes.set_xlabel(r'$\omega$ (deg)')
            self.axes.set_ylabel(r'$2\theta$ (deg)')
            
    def onSetPreferences(self, event):
        print "SetPreferences handler not yet implemented"
        event.Skip()
        
    def onClear(self, event):
        self.axes.clear()
