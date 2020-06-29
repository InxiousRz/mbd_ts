
import frame_main
import wx
from temp_sql_module import TempQuerySQL


class Starter(frame_main.frame_main):
    def __init__(self):
        super().__init__(None)


if __name__ == "__main__":
    s = wx.App()
    a = Starter()
    s.MainLoop()
