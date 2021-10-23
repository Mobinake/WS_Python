import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        vboxsizer = wx.BoxSizer(wx.VERTICAL)
        hboxsizer = wx.BoxSizer(wx.HORIZONTAL)

        self.label = wx.StaticText(self, label="This is a label", style=wx.ALIGN_CENTER)
        vboxsizer.Add(self.label, 0, wx.EXPAND)

        self.label2 = wx.StaticText(self, label="This is Second label", style=wx.ALIGN_CENTER)
        vboxsizer.Add(self.label2, 0, wx.EXPAND)

        self.label3 = wx.StaticText(self, label="This is third label", style=wx.ALIGN_CENTER)
        hboxsizer.Add(self.label3, 0, wx.EXPAND)

        self.label4 = wx.StaticText(self, label="This is fourth label", style=wx.ALIGN_CENTER)
        hboxsizer.Add(self.label4, 0, wx.EXPAND, wx.ALIGN_RIGHT, 20)
        hboxsizer.AddStretchSpacer(1)

        vboxsizer.Add(hboxsizer, 1, wx.ALL | wx.EXPAND)

        self.SetSizer(vboxsizer)
        #self.SetSizer(hboxsizer)


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Sizers")
        self.frame.Show()
        return True


app = MyApp()
app.MainLoop()