import wx
#import spiderwSET

#todo debe estar en una clase cuando se trabaja con wx
class Buck(wx.Frame):
    #metodo constructor
    def __init__(self, parent, id):
        #configuramos la ventana para poder verla
        wx.Frame.__init__(self, parent, id, 'Primera ventana', size=(800,600))
        #creamos un panel
        panel = wx.Panel(self)

        #creacion de un button salida en la pos                     x   y ,tamaño  m    n
        buttonEnviar = wx.Button(panel, label="Enviar Informacion", pos=(10, 80), size=(160, 30))
        buttonSalir = wx.Button(panel,label="Salida",pos=(10,160),size=(60,40))

        # cada vez que tenga un evento de click al button actual, ejecuta la funcion self.(funcionc)
        self.Bind(wx.EVT_BUTTON, self.closebutton, buttonSalir)
        # y esta es otra forma de cerrar la ventana
        # self.Bind(wx.EVT_CLOSE, self.closewindow)
        self.Bind(wx.EVT_BUTTON, self.sendInfo, buttonEnviar)

        #status bar, barra inferior
        status = self.CreateStatusBar()
        #crear la barra superior, menubar con sus respectivos primer y segundo menu
        menubar = wx.MenuBar()
        firstmenu = wx.Menu()
        secmenu = wx.Menu()

        #agregamos elementos al primer y segundo menu
        firstmenu.Append(wx.NewIdRef(), "Informacion")
        firstmenu.Append(wx.NewIdRef(), "Mas")
        secmenu.Append(wx.NewIdRef(), "Mobin Akhtar Khavari")

        #agregamos los menus creados a la barra de menus
        menubar.Append(firstmenu, "Detalles")
        menubar.Append(secmenu, "Creador")
        self.SetMenuBar(menubar)



    #funcion que cierra la ventana
    def closebutton(self, event):
        self.Close(True)
        #self.Destroy()
    #enviar la info al webscraper
    def sendInfo(self, event):
        pass


if __name__=='__main__':
    #app object = corre el programa
    app=wx.App()
    #frame object = muestra el programa
    frame=Buck(parent=None, id=-1)
    frame.Show()
    app.MainLoop()


































































'''
        #salta un msgbox de confirmacion de salida
        msgExit = wx.MessageDialog(None, 'Desea salir?', 'Advertencia de Salida', wx.YES_NO)
        #almacenamos la respuesta del msgBox
        msgExitR = msgExit.ShowModal()
        print('msgExitR')
        msgExit.Destroy()
'''