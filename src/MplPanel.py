# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Sun Apr 27 18:12:16 2014

import wx
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import matplotlib.gridspec as gridspec

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade


class MplPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        self.figure = Figure()
        # begin wxGlade: MplPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.canvas = FigureCanvas(self, wx.ID_ANY, self.figure)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MplPanel.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MplPanel.__do_layout
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.canvas, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        # end wxGlade
        
    def set_grid(self, nr, nc):
        #setup gridspec with the number of rows and columns given
        self.gridspec = gridspec.GridSpec(nr, nc)
        #add axis to each cell of the gridspec
        for i in range(nr*nc):
            self.figure.add_subplot(self.gridspec[i])
        
        self.canvas.draw()
# end of class MplPanel
