import requests
from bs4 import BeautifulSoup

# definimos las variables
year = int(input("Ingrese el año de la cotizacion: "))
month = input("Ingrese el mes de la cotizacion: ")

# url por defenco
url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/a-mes-de-enero'


while((year >= 2010) and (year < 2021)):
    if year == 2010:
        if month.lower() == "enero":
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/a-mes-de-enero'
            year = 0
        elif month.lower() == "febrero":
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/b-mes-de-febrero'
            year = 0
        elif month.lower() == "marzo":
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/c-mes-de-marzo'
            year = 0
        elif month.lower() == "abril":
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/d-mes-de-abril'
            year = 0
        elif month.lower() == "mayo":
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/e-mes-de-mayo'
            year = 0
        elif month.lower() == "junio":
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/f-mes-de-junio'
            year = 0
        elif month.lower() == "julio":
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/g-mes-de-julio'
            year = 0
        elif month.lower() == "agosto":
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/h-mes-de-agosto'
            year = 0
        elif month.lower() == "septiembre":
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/i-mes-de-setiembre'
            year = 0
        elif month.lower() == "octubre":
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/j-mes-de-octubre'
            year = 0
        elif month.lower() == "noviembre":
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/k-mes-de-noviembre'
            year = 0
        elif month.lower() == "diciembre":
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/detail?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos/2010&content-id=/repository/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/cotizaciones/2010/l-mes-de-diciembre'
            year = 0
        else:
            year = 0
            year = input("Ingrese un año correcto(2010 al 2020): ")
            url = 'https://www.set.gov.py/portal/PARAGUAY-SET/InformesPeriodicos?folder-id=repository:collaboration:/sites/PARAGUAY-SET/categories/SET/Informes%20Periodicos/cotizaciones-historicos'


# hacemos la peticion a la pagina de el html
page = requests.get(url)

# parseamos el html en la variable
soup = BeautifulSoup(page.text, 'html.parser')

# separar todos los blockquotes en otra variable
tabla = soup.find('table', align="center", border="1",
                  cellpadding="0", cellspacing="0").tbody

titles = tabla.find('tr')  # titulos
valores = tabla.findAll('tr', class_="chico")  # valores


# Datos filtrados y sanitizados
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

#
# {parsed_titles
#   "dolar": {"compra": [ ], "venta": [  ]},
#   "real" : {"compra": [ ], "venta": [  ]},
#   "euro" : {"compra": [ ], "venta": [  ]},
#   "yenes": {"compra": [ ], "venta": [  ]},
# }
#

def getCompraVentaDelMes(row):
    for x in range(0, len(row)):
        generadorDelDia = getCompraVentaDelDia(parsed_valores[x])
        print("Dolares", f"dia {x}", next(generadorDelDia))
        print("Reales" , f"dia {x}", next(generadorDelDia))
        print("Peso" , f"dia {x}", next(generadorDelDia))
        print("Yen" , f"dia {x}", next(generadorDelDia))
        print("Euro" , f"dia {x}", next(generadorDelDia))
        print("Libra" , f"dia {x}", next(generadorDelDia))

getCompraVentaDelMes(parsed_valores)
