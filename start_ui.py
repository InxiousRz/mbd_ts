
from ui.frame_main import frame_main
import wx


class Starter(frame_main):
    def __init__(self):
        super().__init__(None)


if __name__ == "__main__":
    s = wx.App()
    a = Starter()
    s.MainLoop()
