import wx
import os
import numpy as np
import xrayutilities as xu

from AxesDialog import AxesDialog

class AxesPopupMenu(wx.Menu):
    def __init__(self, figure, axes):
        wx.Menu.__init__(self)
        
        self.axes = axes
        self.figure = figure
        
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
        dlg = wx.FileDialog(None, "Choose a file", "", "", 
                    "XRDML files (*.xrdml)|*.xrdml",
                    wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            #destroy dialog
            dlg.Destroy()
            
            #read xrdml datafile
            om, tt, intensity = xu.io.getxrdml_map(path)
            
            #hxrd transformator
            Si = xu.materials.Si
            hxrd = xu.HXRD(Si.Q(1,1,0),Si.Q(0,0,1))
            
            #transform angles to reciprocal points
            [qx,qy,qz] = hxrd.Ang2Q(om, tt, delta=[0.0, 0.0])
            
            #grid scatter data points
            gridder = xu.Gridder2D(100,100)
            gridder(qy,qz, intensity)
            INT = xu.maplog(gridder.data.transpose(),6,0)

            #clear axes from previous drawing
            self.axes.clear()

            #draw rsm
            cf = self.axes.contourf(gridder.xaxis, gridder.yaxis, INT, 100, extend='min')

            #annotate axis
            self.axes.set_xlabel(r'$Q_{[110]}$ ($\AA^{-1}$)')
            self.axes.set_ylabel(r'$Q_{[001]}$ ($\AA^{-1}$)')
            
    def onSetPreferences(self, event):
        dlg = AxesDialog(None)
        dlg.initialize(self.figure, self.axes)
        dlg.ShowModal()
        dlg.Destroy()
            
    def onClear(self, event):
        self.axes.clear()
