import wx
from src.converter import Converter


if __name__ == '__main__':
    app = wx.App(False)
    frame = Converter(None, "Converter .txt to db")
    frame.Show()
    app.MainLoop()