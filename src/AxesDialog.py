# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Tue Apr 29 11:18:44 2014

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade


class AxesDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AxesDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, -1, style=wx.NB_LEFT)
        self.paneSize_n_Position = wx.Panel(self.notebook_1, -1)
        self.label_7_copy = wx.StaticText(self.paneSize_n_Position, -1, "Move")
        self.label_12 = wx.StaticText(self.paneSize_n_Position, -1, "Left")
        self.tcLeft = wx.TextCtrl(self.paneSize_n_Position, -1, "")
        self.label_13 = wx.StaticText(self.paneSize_n_Position, -1, "Top")
        self.tcTop = wx.TextCtrl(self.paneSize_n_Position, -1, "")
        self.label_11 = wx.StaticText(self.paneSize_n_Position, -1, "Resize")
        self.label_14 = wx.StaticText(self.paneSize_n_Position, -1, "Width")
        self.tcWidth = wx.TextCtrl(self.paneSize_n_Position, -1, "")
        self.tcWidth_cm = wx.TextCtrl(self.paneSize_n_Position, -1, "")
        self.label_15 = wx.StaticText(self.paneSize_n_Position, -1, "Height")
        self.tcHeight = wx.TextCtrl(self.paneSize_n_Position, -1, "")
        self.tcHeight_cm = wx.TextCtrl(self.paneSize_n_Position, -1, "")
        self.paneScale_n_Ticks = wx.Panel(self.notebook_1, -1)
        self.label_1_copy = wx.StaticText(self.paneScale_n_Ticks, -1, "Selection")
        self.lbScaleTicksAxes = wx.ListBox(self.paneScale_n_Ticks, -1, choices=["Horizontal", "Vertical"], style=wx.LB_SINGLE)
        self.label_8 = wx.StaticText(self.paneScale_n_Ticks, -1, "From")
        self.tcFrom = wx.TextCtrl(self.paneScale_n_Ticks, -1, "")
        self.label_9 = wx.StaticText(self.paneScale_n_Ticks, -1, "To")
        self.tcTo = wx.TextCtrl(self.paneScale_n_Ticks, -1, "")
        self.rbTicksIncrement = wx.RadioButton(self.paneScale_n_Ticks, -1, "")
        self.lbTicksIncrement = wx.StaticText(self.paneScale_n_Ticks, -1, "Increment", style=wx.ALIGN_RIGHT)
        self.tcTicksIncrement = wx.TextCtrl(self.paneScale_n_Ticks, -1, "")
        self.rbTicksNumber = wx.RadioButton(self.paneScale_n_Ticks, -1, "")
        self.lbMajorTicksNb = wx.StaticText(self.paneScale_n_Ticks, -1, "Major ticks", style=wx.ALIGN_RIGHT)
        self.tcMajorTicksNb = wx.TextCtrl(self.paneScale_n_Ticks, -1, "")
        self.lbMinorTicksNb = wx.StaticText(self.paneScale_n_Ticks, -1, "Minor ticks", style=wx.ALIGN_RIGHT)
        self.tcMinorTicksNb = wx.TextCtrl(self.paneScale_n_Ticks, -1, "")
        self.paneTitle_n_Format = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.label_16 = wx.StaticText(self.paneTitle_n_Format, -1, "Selection")
        self.lbTitleFormatAxes = wx.ListBox(self.paneTitle_n_Format, -1, choices=["Horizontal", "Vertical"], style=wx.LB_SINGLE)
        self.cbShowLabels = wx.CheckBox(self.paneTitle_n_Format, -1, "Show labels")
        self.lbTitle = wx.StaticText(self.paneTitle_n_Format, -1, "Title")
        self.tcTitle = wx.TextCtrl(self.paneTitle_n_Format, -1, "")
        self.panePalette_n_Style = wx.Panel(self.notebook_1, -1)
        self.label_6 = wx.StaticText(self.panePalette_n_Style, -1, "Gridder")
        self.label_17 = wx.StaticText(self.panePalette_n_Style, -1, "X sampling")
        self.spXSamp = wx.SpinCtrl(self.panePalette_n_Style, -1, "25", min=0, max=200)
        self.label_18 = wx.StaticText(self.panePalette_n_Style, -1, "Y sampling")
        self.spYSamp = wx.SpinCtrl(self.panePalette_n_Style, -1, "25", min=0, max=200)
        self.label_6_copy = wx.StaticText(self.panePalette_n_Style, -1, "Data limits")
        self.label_19 = wx.StaticText(self.panePalette_n_Style, -1, "Min")
        self.tcDataMin = wx.TextCtrl(self.panePalette_n_Style, -1, "")
        self.label_20 = wx.StaticText(self.panePalette_n_Style, -1, "Max")
        self.tcDataMax = wx.TextCtrl(self.panePalette_n_Style, -1, "")
        self.bCancel_copy = wx.Button(self, wx.ID_CANCEL, "Cancel")
        self.bApply_copy = wx.Button(self, wx.ID_APPLY, "Apply")
        self.bOK_copy = wx.Button(self, wx.ID_OK, "OK")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LISTBOX, self.onScaleTicksAxesSelect, self.lbScaleTicksAxes)
        self.Bind(wx.EVT_RADIOBUTTON, self.onIncrementTicksSelect, self.rbTicksIncrement)
        self.Bind(wx.EVT_RADIOBUTTON, self.onNbMajorTicksSelect, self.rbTicksNumber)
        self.Bind(wx.EVT_LISTBOX, self.onTitleFormatAxesSelect, self.lbTitleFormatAxes)
        self.Bind(wx.EVT_CHECKBOX, self.onLabelCheck, self.cbShowLabels)
        self.Bind(wx.EVT_BUTTON, self.onApply, id=wx.ID_APPLY)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AxesDialog.__set_properties
        self.SetTitle("Axes settings")
        self.SetSize((656, 200))
        self.label_12.SetMinSize((55, 19))
        self.label_13.SetMinSize((55, 19))
        self.label_14.SetMinSize((55, 19))
        self.tcWidth_cm.Enable(False)
        self.label_15.SetMinSize((55, 19))
        self.tcHeight_cm.Enable(False)
        self.lbScaleTicksAxes.SetSelection(0)
        self.label_8.SetMinSize((50, 19))
        self.label_9.SetMinSize((50, 19))
        self.rbTicksIncrement.SetMinSize((20, 21))
        self.lbTicksIncrement.SetMinSize((130, 19))
        self.rbTicksNumber.SetMinSize((20, 21))
        self.lbMajorTicksNb.SetMinSize((130, 19))
        self.lbMajorTicksNb.Enable(False)
        self.tcMajorTicksNb.Enable(False)
        self.lbMinorTicksNb.SetMinSize((130, 19))
        self.lbTitleFormatAxes.SetSelection(0)
        self.cbShowLabels.SetValue(1)
        self.label_6.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.label_6_copy.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.bOK_copy.SetFocus()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AxesDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.VERTICAL)
        sizer_17 = wx.BoxSizer(wx.VERTICAL)
        sizer_35 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_37 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_36 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_31 = wx.BoxSizer(wx.VERTICAL)
        sizer_32 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_34 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_33 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_27 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_28 = wx.BoxSizer(wx.VERTICAL)
        sizer_29 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_30 = wx.BoxSizer(wx.VERTICAL)
        sizer_3_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18 = wx.BoxSizer(wx.VERTICAL)
        sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_19 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_17_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_22 = wx.BoxSizer(wx.VERTICAL)
        sizer_26 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_14_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_24 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12.Add(self.label_7_copy, 0, wx.LEFT, 5)
        sizer_23.Add(self.label_12, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_23.Add(self.tcLeft, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_14_copy.Add(sizer_23, 0, wx.LEFT | wx.TOP | wx.EXPAND, 10)
        sizer_24.Add(self.label_13, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_24.Add(self.tcTop, 0, wx.LEFT, 5)
        sizer_14_copy.Add(sizer_24, 0, wx.LEFT | wx.EXPAND, 10)
        sizer_12.Add(sizer_14_copy, 0, wx.EXPAND, 0)
        sizer_11.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_13.Add(self.label_11, 0, wx.LEFT, 5)
        sizer_25.Add(self.label_14, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_25.Add(self.tcWidth, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_25.Add(self.tcWidth_cm, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_22.Add(sizer_25, 0, wx.LEFT | wx.TOP | wx.EXPAND, 10)
        sizer_26.Add(self.label_15, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_26.Add(self.tcHeight, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_26.Add(self.tcHeight_cm, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_22.Add(sizer_26, 0, wx.LEFT | wx.EXPAND, 10)
        sizer_13.Add(sizer_22, 0, wx.EXPAND, 0)
        sizer_11.Add(sizer_13, 1, wx.EXPAND, 0)
        self.paneSize_n_Position.SetSizer(sizer_11)
        sizer_4_copy.Add(self.label_1_copy, 0, wx.EXPAND | wx.ALIGN_BOTTOM, 0)
        sizer_4_copy.Add(self.lbScaleTicksAxes, 0, wx.EXPAND | wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3_copy.Add(sizer_4_copy, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_16_copy.Add(self.label_8, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_16_copy.Add(self.tcFrom, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_15_copy.Add(sizer_16_copy, 0, wx.EXPAND, 0)
        sizer_17_copy.Add(self.label_9, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_17_copy.Add(self.tcTo, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_15_copy.Add(sizer_17_copy, 0, wx.EXPAND, 0)
        sizer_3_copy.Add(sizer_15_copy, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_19.Add(self.rbTicksIncrement, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_19.Add(self.lbTicksIncrement, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_19.Add(self.tcTicksIncrement, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_18.Add(sizer_19, 0, wx.EXPAND, 0)
        sizer_20.Add(self.rbTicksNumber, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_20.Add(self.lbMajorTicksNb, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_20.Add(self.tcMajorTicksNb, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_18.Add(sizer_20, 0, wx.TOP | wx.EXPAND, 10)
        sizer_21.Add((20, 21), 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_21.Add(self.lbMinorTicksNb, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_21.Add(self.tcMinorTicksNb, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_18.Add(sizer_21, 0, wx.EXPAND, 0)
        sizer_3_copy.Add(sizer_18, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        self.paneScale_n_Ticks.SetSizer(sizer_3_copy)
        sizer_30.Add(self.label_16, 0, 0, 0)
        sizer_30.Add(self.lbTitleFormatAxes, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_27.Add(sizer_30, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_28.Add(self.cbShowLabels, 0, 0, 0)
        sizer_29.Add(self.lbTitle, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_29.Add(self.tcTitle, 1, wx.LEFT | wx.EXPAND, 10)
        sizer_28.Add(sizer_29, 0, wx.EXPAND, 0)
        sizer_27.Add(sizer_28, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        self.paneTitle_n_Format.SetSizer(sizer_27)
        sizer_31.Add(self.label_6, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_33.Add(self.label_17, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_33.Add(self.spXSamp, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_32.Add(sizer_33, 0, wx.LEFT, 5)
        sizer_34.Add(self.label_18, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_34.Add(self.spYSamp, 0, 0, 0)
        sizer_32.Add(sizer_34, 0, wx.LEFT, 5)
        sizer_31.Add(sizer_32, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_16.Add(sizer_31, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_17.Add(self.label_6_copy, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_36.Add(self.label_19, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_36.Add(self.tcDataMin, 0, wx.LEFT, 5)
        sizer_35.Add(sizer_36, 0, wx.EXPAND, 0)
        sizer_37.Add(self.label_20, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_37.Add(self.tcDataMax, 0, wx.LEFT, 5)
        sizer_35.Add(sizer_37, 0, wx.EXPAND, 0)
        sizer_17.Add(sizer_35, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_16.Add(sizer_17, 1, wx.EXPAND, 0)
        self.panePalette_n_Style.SetSizer(sizer_16)
        self.notebook_1.AddPage(self.paneSize_n_Position, "Size/Position")
        self.notebook_1.AddPage(self.paneScale_n_Ticks, "Scale/Ticks")
        self.notebook_1.AddPage(self.paneTitle_n_Format, "Title/Format")
        self.notebook_1.AddPage(self.panePalette_n_Style, "Palette/Style")
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        sizer_2.Add((300, 20), 0, 0, 0)
        sizer_2.Add(self.bCancel_copy, 0, wx.ALIGN_RIGHT, 0)
        sizer_2.Add(self.bApply_copy, 0, wx.ALIGN_RIGHT, 0)
        sizer_2.Add(self.bOK_copy, 0, wx.ALIGN_RIGHT, 0)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade
    
    def initialize(self, figure, axes):
        self.axes = axes
        self.figure = figure
        
        if self.lbScaleTicksAxes.GetSelection() == 0:#if horizontal axis selected
            #initialize x-axis limits
            [xmin, xmax] = self.axes.get_xlim()
            self.tcFrom.SetValue("%.3f" % xmin)
            self.tcTo.SetValue("%.3f" % xmax)
            
            #display x ticks
            nbMajTicks = len(self.axes.get_xmajorticklabels())
            nbMinTicks = len(self.axes.get_xminorticklabels())
            self.tcMajorTicksNb.SetValue("%d" % nbMajTicks)
            self.tcMinorTicksNb.SetValue("%d" % nbMinTicks)
        elif self.lbScaleTicksAxes.GetSelection() == 1:#if horizontal axis selected:
            #initialize y-axis limits
            [ymin, ymax] = self.axes.get_ylim()
            self.tcFrom.SetValue("%.3f" % ymin)
            self.tcTo.SetValue("%.3f" % ymax)
            
            #display y ticks
            nbMajTicks = len(self.axes.get_ymajorticklabels())
            nbMinTicks = len(self.axes.get_yminorticklabels())
            self.tcMajorTicksNb.SetValue("%d" % nbMajTicks)
            self.tcMinorTicksNb.SetValue("%d" % nbMinTicks)
        
        if self.lbTitleFormatAxes.GetSelection() == 0:
            #display x axis lable
            label = self.axes.get_xlabel()
            self.tcTitle.SetValue(label)
        elif self.lbTitleFormatAxes.GetSelection() == 1:
            #display x axis lable
            label = self.axes.get_ylabel()
            self.tcTitle.SetValue(label)
        
        #get axes position and size
        bbox = self.axes.get_position()
        x0, y0, width, height = bbox.bounds
        #initilize axes position
        self.tcLeft.SetValue("%.3f" % x0)
        self.tcTop.SetValue("%.3f" % y0)
        #initialize axes size
        self.tcWidth.SetValue("%.3f" % width)
        self.tcHeight.SetValue("%.3f" % height)
        #get axes size in inches
        bbox = self.axes.get_window_extent().transformed(self.figure.dpi_scale_trans.inverted())
        width, height = bbox.width, bbox.height
        #initialize axes sizes in inches
        self.tcWidth_cm.SetValue("%.3f" % width)
        self.tcHeight_cm.SetValue("%.3f" % height)
        
        #data limits TODO: cannot be implemented as it requires contourset
        cmin = 0; cmax = 1
        self.tcDataMin.SetValue("%.4f" % cmin)
        self.tcDataMax.SetValue("%.4f" % cmax)
        
        #gridder samplings
        self.spXSamp.SetValue(self.axes.gridder.nx)
        self.spYSamp.SetValue(self.axes.gridder.ny)
                
    def onScaleTicksAxesSelect(self, event):  # wxGlade: AxesDialog.<event_handler>
        if self.lbScaleTicksAxes.GetSelection() == 0: #horizontal axis
            [xmin, xmax] = self.axes.get_xlim()
            self.tcFrom.SetValue("%.3f" % xmin)
            self.tcTo.SetValue("%.3f" % xmax)
        elif self.lbScaleTicksAxes.GetSelection() == 1: #vertical axis
            [ymin, ymax] = self.axes.get_ylim()
            self.tcFrom.SetValue("%.3f" % ymin)
            self.tcTo.SetValue("%.3f" % ymax)
    
    def onIncrementTicksSelect(self, event):  # wxGlade: AxesDialog.<event_handler>
        #enable ticks increment
        self.lbTicksIncrement.Enable(True)
        self.tcTicksIncrement.Enable(True)
        #if ticks increment selected, nb of ticks should be disabled
        self.lbMajorTicksNb.Enable(False)
        self.tcMajorTicksNb.Enable(False)
        
    
    def onNbMajorTicksSelect(self, event):  # wxGlade: AxesDialog.<event_handler>
        #enable number of ticks
        self.lbMajorTicksNb.Enable(True)
        self.tcMajorTicksNb.Enable(True)
        #if ticks number of increment selected, ticks increment should be disabled
        self.lbTicksIncrement.Enable(False)
        self.tcTicksIncrement.Enable(False)
    
    def onTitleFormatAxesSelect(self, event):  # wxGlade: AxesDialog.<event_handler>
        if self.lbTitleFormatAxes.GetSelection() == 0: #horizontal axis
            label = self.axes.get_xlabel()
            self.tcTitle.SetValue(label)
        elif self.lbTitleFormatAxes.GetSelection() == 1: #vertical axis
            label = self.axes.get_ylabel()
            self.tcTitle.SetValue(label)
            
    def onApply(self, event):  # wxGlade: AxesDialog.<event_handler>
        if self.lbTitleFormatAxes.GetSelection() == 0: #horizontal axis
            label = self.tcTitle.GetValue()
            self.axes.set_xlabel(label)
        elif self.lbTitleFormatAxes.GetSelection() == 1: #vertical axis
            label = self.tcTitle.GetValue()
            self.axes.set_ylabel(label)
       
        if self.lbScaleTicksAxes.GetSelection() == 0: #horizontal axis
            xmin = float(self.tcFrom.GetValue())
            xmax = float(self.tcTo.GetValue())
            self.axes.set_xlim(xmin, xmax)
        elif self.lbScaleTicksAxes.GetSelection() == 1: #vertical axis
            ymin = float(self.tcFrom.GetValue())
            ymax = float(self.tcTo.GetValue())
            self.axes.set_ylim(ymin, ymax)
            
        #axes position
        x0 = float(self.tcLeft.GetValue())
        y0 = float(self.tcTop.GetValue())
        #axes size
        width = float(self.tcWidth.GetValue())
        height = float(self.tcHeight.GetValue())
        #update axes
        self.axes.set_position([x0, y0, width, height])
        
        nx = int(self.spXSamp.GetValue())
        ny = int(self.spYSamp.GetValue())
        self.axes.set_gridder_resolution(nx, ny)
            
        self.initialize(self.figure, self.axes)
        
        
        #update figure
        self.figure.canvas.draw()

    def onLabelCheck(self, event):  # wxGlade: AxesDialog.<event_handler>
        if event.IsChecked():            
            if self.lbTitleFormatAxes.GetSelection() == 0:
                #hide x axis
                self.axes.tick_params(axis='x', reset = True) # reset labels

            elif self.lbTitleFormatAxes.GetSelection() == 1:
                #hide y axis lable
                self.axes.tick_params(axis='y', reset = True) # reset labels
        else:
            if self.lbTitleFormatAxes.GetSelection() == 0:
                #hide x axis label and title
                self.axes.tick_params(\
                    axis='x',          # changes apply to the x-axis
                    labelbottom='off') # labels along the bottom edge are off
            elif self.lbTitleFormatAxes.GetSelection() == 1:
                #hide y axis lable title
                self.axes.tick_params(\
                    axis='y',          # changes apply to the x-axis
                    labelleft='off') # labels along the left edge are off
        self.figure.canvas.draw()

# end of class AxesDialog
