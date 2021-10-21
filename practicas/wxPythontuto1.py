import wx

#todo debe estar en una clase cuando se trabaja con wx
class Buck(wx.Frame):
    #metodo constructor
    def __init__(self, parent, id):
        #configuramos la ventana para poder verla
        wx.Frame.__init__(self, parent, id, 'Primera ventana',size=(300,200))

#
if __name__=='__main__':
    #app object = corre el programa
    app=wx.PySimpleApp()
    #frame object = muestra el programa
    frame=Buck(parent=None, id=-1)
    frame.Show()
    app.MainLoop()