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
        self.y_axis_max = valmax
        self.y_axis_min = valmin

        #SERIES
        self.line, = self.ax.plot_date([], [],'-', lw=3, color='blue')
        self.ax.set_ylim(int(self.y_axis_min), int(self.y_axis_max))
        self.ax.set_xlim(self.x_axis_start, self.x_axis_end)
        self.ax.set_xlabel('Time Record')
        self.ax.set_ylabel('Value ' + str(self.GR_UsedSensor))
        self.ax.xaxis.set_major_formatter(ds.DateFormatter('%H:%M:%S'))
        self.fig.suptitle(str('Data ' + str(self.GR_UsedSensor) + ' On : ') + str(self.date), fontsize=14, fontweight='bold')
        self.fig.autofmt_xdate()
        self.ax.grid()

        #ANIMATION
        # self.ani = animation.FuncAnimation(self.fig, self.GpRun, self.GpDatapassing, blit=False, interval=1000,
        #                                     repeat=False, init_func=self.GpInit)

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
        plt.hold
        if self._LiveUpdate == True:
            self._LiveUpdate = False
        plt.close()
        time.sleep(1)
        self._GraphActivates = False
        return
        # except Exception as e:
        #     print(e)
        #     print("a")
        #     plt.clf()
        #     if self._LiveUpdate == True:
        #         self._LiveUpdate = False
        #     plt.close()
        #     time.sleep(1)
        #     self._GraphActivates = False
        #     return

    def GpGetdatetime(self):
        res = datetime.datetime.now()
        return (res)

    def GpGetdate(self):
        res = datetime.date.today()
        return (res)

    def GpDatapassing(self):
        while True:
            if self._LiveUpdate == True:
                try:
                    Data_Container = self._LiveData
                    
                    if len(Data_Container) != 0:
                        Data_Container.sort()
                        new = True
                        x = Data_Container[0][0]
                        y = Data_Container[0][1]
                        del Data_Container[0]
                    else:
                        new = False
                        x = None
                        y = None
                except Exception as e:
                    print(e)
                    print("b")
                    yield (False,None,None)
                else:
                    yield (new,x, y)
            else:
                new = False
                x = None
                y = None
                yield (new, x, y)


    def GpInit(self):
        self.ax.set_ylim(int(self.y_axis_min), int(self.y_axis_max))
        self.ax.set_xlim(self.x_axis_start, self.x_axis_end)
        self.ax.set_xlabel('Time Record')
        self.ax.set_ylabel('Value ' + str(self.GR_UsedSensor))
        self.ax.xaxis.set_major_formatter(ds.DateFormatter('%H:%M:%S'))
        self.fig.suptitle(str('Data On : ') + str(self.date),fontsize=14,fontweight='bold')
        self.fig.autofmt_xdate()
        self.ax.grid()
        self.line.set_data(self.xdata, self.ydata)
        return (self.line)



    def GpRun(self,data):
        # update the data
        new, x, y = data
        # print new,x,y
        if new == True:
            # print
            self.xdata.append(x)
            self.ydata.append(y)

            if self._LiveUpdate == True:
                date_now = datetime.datetime(year=self.date.year,month=self.date.month,day=self.date.day,
                                       hour=23,minute=59,second=59)
                date_diff = (x - date_now).total_seconds()
                # print (date_diff)

                if date_diff >= 1:
                    # ToDo : Save To File Here
                    print ('Passing A New Day')
                    plt.close()

                    # ToDo : Reset Canvas
                    del self.xdata[:]
                    del self.ydata[:]
                    self.line.set_data(self.xdata, self.ydata)

            print(str(self.xdata[-1])+' // '+str(self.ydata[-1]))

            self.line.set_data(self.xdata, self.ydata)

        return (self.line)


# if __name__ == "__main__":


    # data sample
    # dates = datetime.date.today()
    # container = {}
    # time_start = datetime.datetime.now()

    # for i in range(200):
    #     value = random.randint(0,200)
    #     container.update({
    #         str(time_start):[time_start, value]
    #     })
        # time_start += datetime.timedelta(seconds=1)


    # a = GraphGen(dates="2020-08-05",
    #                 lives=False,
    #                 devices="PH_Sensor")
    