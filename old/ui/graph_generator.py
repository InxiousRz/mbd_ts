"""
=====
Decay
=====
This example showcases:
- using a generator to drive an animation,
- changing axes limits during an animation.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
import matplotlib.dates as ds
import time
import random
import wx

from ui.temp_sql_record import TempQuerySQL_2


class GraphGen():

    def __init__(self,dates,lives,devices):
        
        self._GraphActivates = True
        self._LiveData = []

        db = TempQuerySQL_2()

        datas = db.GetDataSample(devicename=devices,recorddate=dates)
        if len(datas) == 0:
            wx.MessageBox('Data Grafik pada tanggal tersebut kosong', 'Warning',
                                     wx.OK | wx.ICON_WARNING)

        # try:
        #Live Update
        self._LiveUpdate = lives

        #New Var
        self.GR_UsedSensor = devices
        self.GR_Data_Before = datas
        self.GR_Data_Before_key = list(datas.keys())
        self.GR_Data_Before_key.sort()

        self.xdata, self.ydata = [], []
        
        # {
        #     datetime.datetime string:
        #     [datetime.datetime obj, value]
        # }

        #APLLY DATA EXIST
        for key in self.GR_Data_Before_key:
            items = self.GR_Data_Before[key]
            x = items[0]
            y = items[1]
            self.xdata.append(x)
            self.ydata.append(y)

        starts = self.GR_Data_Before[self.GR_Data_Before_key[0]][0]
        ends = self.GR_Data_Before[self.GR_Data_Before_key[-1]][0]

        valmin = self.GR_Data_Before[self.GR_Data_Before_key[0]][1]
        valmax = self.GR_Data_Before[self.GR_Data_Before_key[-1]][1]

        #FIGURE
        self.fig, self.ax = plt.subplots()
        self.date = dates
        self.x_axis_start = starts
        self.x_axis_end = ends
        self.y_axis_max = float(valmax) + (float(valmax) * (10/100))
        self.y_axis_min = float(valmin) - (float(valmax) * (10/100))

        #SERIES
        self.line, = self.ax.plot_date([], [],'-', lw=3, color='blue')
        self.ax.set_ylim(self.y_axis_min, self.y_axis_max)
        self.ax.set_xlim(self.x_axis_start, self.x_axis_end)
        self.ax.set_xlabel('Time Record')
        self.ax.set_ylabel('Value ' + str(self.GR_UsedSensor))
        self.ax.xaxis.set_major_formatter(ds.DateFormatter('%H:%M:%S'))
        self.fig.suptitle(str('Data ' + str(self.GR_UsedSensor) + ' On : ') + str(self.date), fontsize=14, fontweight='bold')
        self.fig.autofmt_xdate()
        self.ax.grid()

        figure = plt.gcf()  # Get current figure
        toolbar = figure.canvas.toolbar  # Get the toolbar handler
        toolbar.update()
        self.line.set_data(self.xdata, self.ydata)
        self.ax.grid()
        plt.rcParams['axes.facecolor'] = 'white'
        plt.rcParams['axes.edgecolor'] = 'white'
        plt.rcParams['axes.grid'] = True
        plt.rcParams['grid.alpha'] = 1
        plt.rcParams['grid.color'] = "#cccccc"
        plt.grid(True)
        plt.show()

        plt.clf()
        if self._LiveUpdate == True:
            self._LiveUpdate = False
        plt.close()
        time.sleep(1)
        self._GraphActivates = False
        return

    def GpGetdatetime(self):
        res = datetime.datetime.now()
        return (res)

    def GpGetdate(self):
        res = datetime.date.today()
        return (res)
