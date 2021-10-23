import requests
from bs4 import BeautifulSoup
import wx
import wx.grid as grid



# url por defecto
url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/a-mes-de-enero'
year = 0
month = 0

# debe estar en una clase cuando se trabaja con wx
class SpiderInterface(wx.Frame):
    #constructor
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Primera ventana', size=(1200, 820))
        self.InitUI()
        self.Show(True)

    #interfaz
    def InitUI(self):
        # panel
        panel = wx.Panel(self)



        # botones
        # creacion de un button salida en la pos                     x   y ,tamaÃ±o  m    n
        buttonPromedio = wx.Button(panel, label="Promedio de monedas", pos = (10,10), size=(160, 30))
        buttonMay = wx.Button(panel, label="Mayor precio a menor precio", pos = (10,40), size=(200, 30))
        buttonMen = wx.Button(panel, label="Menor precio a mayor precio", pos = (10,70), size=(200, 30))
        buttonSalir = wx.Button(panel, label="Salida", pos = (10,100), size=(60, 30))
        # cada vez que tenga un evento de click al button actual, ejecuta la funcion self.(funcion)
        self.Bind(wx.EVT_BUTTON, self.promedio, buttonPromedio)
        self.Bind(wx.EVT_BUTTON, self.may, buttonMay)
        self.Bind(wx.EVT_BUTTON, self.men, buttonMen)
        self.Bind(wx.EVT_BUTTON, self.closebutton, buttonSalir)




        # #barra de estado, inferior
        # status = self.CreateStatusBar()

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

        # #text box
        # boxYear = wx.TextEntryDialog(None, "Ingrese el año", "WebScraping w/Python", "Ingrese el año")
        # # preguntamos si selecciono aceptar o cancelar
        # if boxYear.ShowModal() == wx.ID_OK:
        #     year = boxYear.GetValue()
        # boxmonth = wx.TextEntryDialog(None, "Ingrese el mes", "WebScraping w/Python", "Ingrese el mes")
        # # preguntamos si selecciono aceptar o cancelar
        # if boxmonth.ShowModal() == wx.ID_OK:
        #     month = boxmonth.GetValue()

    # funciones
    def promedio(self, event):
        pass
    def may(self, event):
        pass
    def men(self, event):
        pass
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
if ((year == 2018) or (year == 2020)):
    aux = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/ano1/a-mes-de-enero&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/ano1/A%20-%20Mes%20de%20mes1'
    aux1 = aux.replace("ano1", year)
    url = aux1.replace("mes1", month)

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
#       "dolar"    :    "real"
# {compra : venta}{compra : venta}
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
    #frame object = muestra el programa
    frame = SpiderInterface(parent=None, id=-1)
    frame.Show()
    app.MainLoop()


































