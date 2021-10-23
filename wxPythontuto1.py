import wx
import wx.grid as grid

#to do debe estar en una clase cuando se trabaja con wx
class Buck(wx.Frame):
    #metodo constructor
    def __init__(self, parent, id):
        #configuramos la ventana para poder verla
        wx.Frame.__init__(self, parent, id, 'Primera ventana', size=(800,600))
        #creamos un panel
        panel = wx.Panel(self)

        table = grid.Grid(self)
        table.CreateGrid(33, 12)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(table, 1, wx.EXPAND)
        self.SetSizer(sizer)



        #creacion de un button salida en la pos                     x   y ,tamaÃ±o  m    n
        buttonSalir = wx.Button(panel,label="Salida",pos=(10,160),size=(60,40))

        # cada vez que tenga un evento de click al button actual, ejecuta la funcion self.(funcionc)
        self.Bind(wx.EVT_BUTTON, self.closebutton, buttonSalir)


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

        #creamos el text box para almacenar el aÃ±o
        boxYear = wx.TextEntryDialog(None, "Ingrese el aÃ±o", "WebScraping w Python", "Ingrese el aÃ±o")
        #preguntamos si selecciono aceptar o cancelar
        if boxYear.ShowModal() == wx.ID_OK:
            year = boxYear.GetValue()

        # creamos el text box para almacenar el mes
        boxmonth = wx.TextEntryDialog(None, "Ingrese el mes", "WebScraping w Python", "Ingrese el mes")
        # preguntamos si selecciono aceptar o cancelar
        if boxmonth.ShowModal() == wx.ID_OK:
            month = boxmonth.GetValue()


    #funcion que cierra la ventana
    def closebutton(self, event):
        self.Close(True)
        #self.Destroy()



if __name__=='__main__':
    #app object = corre el programa
    app=wx.App()
    #frame object = muestra el programa
    frame = Buck(parent=None, id=-1)
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