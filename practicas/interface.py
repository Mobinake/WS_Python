#! /usr/bin/python
import wx, os
# modulos para trabajar con el entorno
# grafico y el sistema operativo
from wx.lib.wordwrap import wordwrap

# El mensaje de la licencia de nuestra aplicacion
licenceText = "Este es una muestra del poder de python XD"

# Tipo de archivos de ejemplo, estos son utilizados para
# filtrar por extension al momento de invocar "abrir un archivo"
wildcard = "Archivos de audio mp3 (*.mp3)|*.mp3|" \
           "Documento de Word (*.doc)|*.doc|" \
           "Todos los archivos(*.*)|*.*"


# Clase de nuestra ventana de ejemplo
class MyFrame(wx.Frame):

    def __init__(self):
        """Esta tambien es otra forma de crear comentarios
        utilizando varias lineas, equivaldria a /** ... */ en Java o C.
        Este es el metodo constructor que permite inicializar a nuestra
        ventana, es el equivalente al constructor de Java"""

        # Llamamos a la clase Frame que construira nuestra ventana
        wx.Frame.__init__(self, None, -1, "Mi Ventana", size=(400, 400))

        # El panel de nuestra ventana para poner botones y demas artilugios
        panel = wx.Panel(self, -1)

        # Un boton que mostrara un dialogo "Sobre..."
        b = wx.Button(panel, -1, "Hola Mundo!", (20, 10))

        # integramaos el boton en la ventana
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)

        # Otro boton que abrira un dialogo de abrir un archivo
        b = wx.Button(panel, -1, "Abrir algun archivo", (20, 50))

        # igualmente integramos este boton al al panel
        self.Bind(wx.EVT_BUTTON, self.OnButton2, b)

    def OnButton(self, evt):
        """Metodo que reaccionara cuando presionemos el boton Hola Mundo!"""

        # Creamos el dialogo
        info = wx.AboutDialogInfo()

        # le ponemos nombre superior de nuestro dialogo
        info.Name = "Mi Ventana"

        # le asignamos la version de nuestra aplicacion
        info.Version = "1.0"

        # Un copyright
        info.Copyright = "(C) Copyright Miguel Pinia"

        # Una descripcion de nuestra aplicacion
        info.Description = wordwrap("Este es la informacion sobre la aplicacion: "
                                    "esta aplicacion fue hecha en"
                                    " python ", 350, wx.ClientDC(self))

        # Asignamos la licencia que creamos al principio del documento
        info.License = wordwrap(licenceText, 500, wx.ClientDC(self))

        # Desarrolladores de la aplicacion
        # Nota: Vypi es una mascota XD
        info.Developers = ["Miguel Pinia", "wxPython", "Vypi la mascota"]

        # la que contendra nuestra informacion
        wx.AboutBox(info)

    def OnButton2(self, evt):
        """Este metodo reaccionara al presionar el boton "abrir" generando
        un evento que permitira crear un dialogo de apertura a nuestro archivo,
        claramente este archivo seleccionado no hara nada, ya que no vamos a trabajar
        sobre el, dado que esta es una aplicacion de ejemplo"""

        # Creamos el dialogo y lo mostramos
        dlg = wx.FileDialog(self, message="Escoga un archivo", defaultDir=os.getcwd(), defaultFile="",
                            wildcard=wildcard, style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)

        # Si ya seleccionamos el archivo lo unico que haremos sera destruir el dialogo
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy


if __name__ == "__main__":
    """Metodo main"""
    app = wx.App()

    # creamos un objeto de la clase myframe
    frame = MyFrame()

    # Lo mostramos hasta que algun evento ocurra
    frame.Show(True)
    app.MainLoop()