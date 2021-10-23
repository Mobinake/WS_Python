import requests
from bs4 import BeautifulSoup
import wx
import wx.grid as grid

import wxPythontuto1


# url por defecto
url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/a-mes-de-enero'
year = 0
month = 0
# debe estar en una clase cuando se trabaja con wx
class Buck(wx.Frame):

    #constructor
    def __init__(self, parent, id):

        # configuramos la ventana para poder verla
        wx.Frame.__init__(self, parent, id, 'Primera ventana', size=(800, 600))
        # creamos un panel
        panel = wx.Panel(self)

        #tabla
        table = grid.Grid(self)
        table.CreateGrid(33, 12)

        #boxsizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(table, 1, wx.EXPAND)
        self.SetSizer(sizer)

        #botones
        # creacion de un button salida en la pos                     x   y ,tamaÃ±o  m    n
        buttonSalir = wx.Button(panel, label="Salida", pos=(10, 160), size=(60, 40))
        # cada vez que tenga un evento de click al button actual, ejecuta la funcion self.(funcion)
        self.Bind(wx.EVT_BUTTON, self.closebutton, buttonSalir)

        #barra de estado, inferior
        status = self.CreateStatusBar()

        #barra de menu, superior
        menubar = wx.MenuBar()
        firstmenu = wx.Menu()
        secmenu = wx.Menu()
        # agregamos elementos al primer y segundo menu
        firstmenu.Append(wx.NewIdRef(), "Informacion")
        firstmenu.Append(wx.NewIdRef(), "Mas")
        secmenu.Append(wx.NewIdRef(), "Mobin Akhtar Khavari")
        # agregamos los menus creados a la barra de menus
        menubar.Append(firstmenu, "Detalles")
        menubar.Append(secmenu, "Creador")
        self.SetMenuBar(menubar)

        #text box
        boxYear = wx.TextEntryDialog(None, "Ingrese el año", "WebScraping w Python", "Ingrese el año")
        # preguntamos si selecciono aceptar o cancelar
        if boxYear.ShowModal() == wx.ID_OK:
            year = boxYear.GetValue()
            print(year)
        boxmonth = wx.TextEntryDialog(None, "Ingrese el mes", "WebScraping w Python", "Ingrese el mes")
        # preguntamos si selecciono aceptar o cancelar
        if boxmonth.ShowModal() == wx.ID_OK:
            month = boxmonth.GetValue()
            print(month)


    # funciones
    def closebutton(self, event):
        self.Close(True)



#definicion de la url
if ((year == 2010) or (year == 2011) or (year == 2012) or (year == 2013)):
    aux = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/ano1&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/ano1/a-mes-de-mes1'
    aux1 = aux.replace("ano1", year)
    url = aux1.replace("mes1", month)
if ((year == 2014) or (year == 2017) or (year == 2019)):
    aux = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/ano1/a-mes-de-enero&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/ano1/a-mes-de-mes1'
    aux1 = aux.replace("ano1", year)
    url = aux1.replace("mes1", month)
#no funciona correctamente, se debe ingresar la primera letra en mayuscula
if ((year == 2015) or (year == 2016)):
    aux = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/ano1/a-mes-de-enero&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/ano1/A_-_Mes_de_mes1'
    aux1 = aux.replace("ano1", year)
    url = aux1.replace("mes1", month)
    print(url)
if ((year == 2018) or (year == 2020)):
    aux = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/ano1/a-mes-de-enero&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/ano1/A%20-%20Mes%20de%20mes1'
    aux1 = aux.replace("ano1", year)
    url = aux1.replace("mes1", month)
    print(url)

# hacemos la peticion a la pagina de el html
page = requests.get(url)
# parseamos el html en la variable
soup = BeautifulSoup(page.text, 'html.parser')
# separar todos los table en otra variable
tabla = soup.find('table', align="center", border="1", cellpadding="0", cellspacing="0").tbody
titles = tabla.find('tr')  # titulos
valores = tabla.findAll('tr', class_="chico")  # valores

# Datos filtrados y estandarisados
parsed_titles = []
parsed_valores = []
# Limpiado de datos
[parsed_titles.append(title.text.strip()) for title in titles if title.get_text().strip() != ""]
for valor in valores:
    __parsed_valores_row = []
    __rows = valor.findAll('td')
    for value in __rows[1:]:
        __parsed_valores_row.append(value.get_text().strip())
    parsed_valores.append(__parsed_valores_row)

# Definiendo los helpers
def getCompraVentaDelDia(row):
    # Retorna la compra y venta de varias monedas
    # Recibe [ x1, x2, y1, y2 ] -> [x1, x2] then [y1, y2]
    for i in range(1, len(row), 2):
        yield [row[i-1], row[i]]

#formato en consola
#       "dolar"    :    "real"   :"Peso argentino"   : "yenes"    :    "euro" :        "libra"
# {compra : venta}{compra : venta}{compra : venta}{compra : venta}{compra : venta}{compra : venta}
#

def getCompraVentaDelMes(row):
    #print("\t\tDolares \t\t Reales \t    Peso Argentino \t  Yen \t\t   Euro \t\t\t Libra")
    #print("\t    Compra\tVenta \t   Compra \t Venta \t   Compra \t Venta \t   Compra \t Venta \tCompra \t Venta \tCompra \t Venta")
    for x in range(0, len(row)):
        generadorDelDia = getCompraVentaDelDia(parsed_valores[x])
        #print( f"dia {x}", next(generadorDelDia), next(generadorDelDia), next(generadorDelDia), next(generadorDelDia), next(generadorDelDia), next(generadorDelDia))




if __name__ == '__main__':
    # app object = corre el programa
    app = wx.App()
    # frame object = muestra el programa
    frame = Buck(parent=None, id=-1)
    frame.Show()
    app.MainLoop()


































