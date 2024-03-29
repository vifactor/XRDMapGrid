import wx
import os
import numpy as np
import xrayutilities as xu

import cfg
from AxesDialog import AxesDialog
from CSVDialog import CSVDialog

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
        dlg = wx.FileDialog(None, "Choose a file", cfg.USER_WORK_DIR, "", 
                    "All files (*.*)|*.*|XRDML files (*.xrdml)|*.xrdml|QFIT files (*.qfit)|*.qfit",
                    wx.OPEN|wx.FD_CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            #save path in the global variable
            cfg.USER_WORK_DIR = dlg.GetDirectory()
            
            fileBase, fileExtension = os.path.splitext(path)
            if fileExtension == '.xrdml':
                self.loadXRDML(path)
            else:
                self.loadCSV(path)
        dlg.Destroy()
            
    def loadXRDML(self, path):
        #read xrdml datafile
        om, tt, intensity = xu.io.getxrdml_map(path)
    
        #hxrd transformator
        Si = xu.materials.Si
        hxrd = xu.HXRD(Si.Q(1,1,0),Si.Q(0,0,1))
            
        #transform angles to reciprocal points
        [qx,qy,qz] = hxrd.Ang2Q(om, tt, delta=[0.0, 0.0])
            
        #clear axes from previous drawing
        self.axes.clear()

        #draw rsm
        self.axes.rsm(qy,qz, intensity)
    
    def loadCSV(self, path):
        dlg = CSVDialog(None)
        dlg.process(path)
        xarr = []; yarr = []; zarr = []
        if dlg.ShowModal() == wx.ID_OK:
            import csv, sys
            data_cols = dlg.GetDataCols()
            dialect = dlg.GetDialect()
            commentchar = dlg.GetCommentChar()
            with open(path, 'rb') as csvfile:
                reader = csv.reader(csvfile, dialect = dialect)
                try:
                    for row in reader:
                        if row[0].startswith(commentchar):
                            continue
                        try:
                            xarr.append(float(row[data_cols[0]]))
                            yarr.append(float(row[data_cols[1]]))
                            zarr.append(float(row[data_cols[2]]))
                        except IndexError as e:
                            print("Line %d: %s in %s" % (reader.line_num, row, e))
                            #clear axes from previous drawing
                except csv.Error as e:
                    sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
            self.axes.clear()

            #draw data
            self.axes.rsm(xarr, yarr, zarr)

        dlg.Destroy()
        
    
    def onSetPreferences(self, event):
        dlg = AxesDialog(None)
        dlg.initialize(self.figure, self.axes)
        dlg.ShowModal()
        dlg.Destroy()
            
    def onClear(self, event):
        self.axes.clear()
