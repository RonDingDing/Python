import wx

ID_MENU_NEW = wx.NewId()
ID_MENU_OPEN = wx.NewId()
ID_MENU_SAVE = wx.NewId()


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.CreateMenuBar()
        self.CreateStatusBar()

        self.SetSize((250, 180))
        self.SetTitle("Global ids")
        self.Centre()
        self.Show(True)

    def CreateMenuBar(self):

        mb = wx.MenuBar()

        fMenu = wx.Menu()
        fMenu.Append(ID_MENU_NEW, "New")
        fMenu.Append(ID_MENU_OPEN, "Open")
        fMenu.Append(ID_MENU_SAVE, "Save")

        mb.Append(fMenu, "&amp;amp;amp;amp;amp;File")
        self.SetMenuBar(mb)

        self.Bind(wx.EVT_MENU, self.DisplayMessage, id=ID_MENU_NEW)
        self.Bind(wx.EVT_MENU, self.DisplayMessage, id=ID_MENU_OPEN)
        self.Bind(wx.EVT_MENU, self.DisplayMessage, id=ID_MENU_SAVE)

    def DisplayMessage(self, e):

        sb = self.GetStatusBar()

        eid = e.GetId()

        if eid == ID_MENU_NEW:
            msg = "New menu item selected"
        elif eid == ID_MENU_OPEN:
            msg = "Open menu item selected"
        elif eid == ID_MENU_SAVE:
            msg = "Save menu item selected"
        else:
            msg = "Happy"

        sb.SetStatusText(msg)


def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == "__main__":
    main()
