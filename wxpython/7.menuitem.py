import wx

APP_EXIT = 1


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu, APP_EXIT, "&QuittCtrl+Q")
        import os

        print()
        qmi.SetBitmap(wx.Bitmap("./texit.png"))
        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        self.SetSize((250, 200))
        self.SetTitle("Icons and shortcuts")
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == "__main__":
    main()
