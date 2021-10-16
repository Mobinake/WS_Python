import requests
from bs4 import BeautifulSoup

url = 'https://parascrapear.com/'

#hacemos la peticion a la pagina de el html
page = requests.get(url)

#parseamos el html en la variable
soup = BeautifulSoup(page.text, 'html.parser')

#separar todos los blockquotes en otra variable
blockquote_items = soup.find_all('blockquote')

#recorremos todos los datos obtenidos
for blockquote in blockquote_items:
    #buscamos dentro de la pagina las clases necesarias
    autor = blockquote.find(class_='author').text
    categoria = blockquote.find(class_='cat').text
    frase = blockquote.find('q').text

    print([autor, categoria, frase])



















