__author__ = 'MOBIN'

import scrapy
from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider
from scrapy.spiders import  Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import Join
from bs4 import BeautifulSoup

#extraer noticias de una pagina web, el titulo y el contenido

#definimos la clase que tendra los items
class ABCItem(Item):
    #campos de lo que quiero guardar de cada artuculo
    titulo = Field()
    contenido = Field()

#definimos la clase del spider
class CrawlerNoticia(CrawlSpider):
    #le damos el nombre
    name = 'crawlernoticia'
    #los dominios los cuales se visite
    allowed_domains = ['abc.com.py']
    #url inicial
    start_urls = ['https://www.abc.com.py']

    #reglas de comportamiento del crawlspider
    rules = (
        #objetos tipo rule
        #regla para crawlind horizontal, para seguir la paginacion
        #linkextractor= extractor de la info del link
        Rule(LinkExtractor(allow=r'/'), follow=True),

        #regla para el seguir el detalle de las paginas, la info de cada articulo, y con cada articulo llamamos a una
        # funcion
        Rule(LinkExtractor(allow=r'/nacionales'), follow=False, callback='parse_items')
    )
    #funcion que sera llamada
    def parse_items(self, response):

        #instanciamos el item
        item = scrapy.loader.ItemLoader(ABCItem(), response)

        #buscamos el titulo dentro de la pagina
        item.add_xpath('titulo', '//h1/text()')

        #variable que usaremos para parsear la pagina, le pasamos el responde.body de la pagina
        soup = BeautifulSoup(response.body)

        #creamos una variable y unsamos una funcion para buscar una determinada clase
        article = soup.find(class_="article-container")

        #ahora extraemos el texto de esa clase, eliminando caracteres especiales y saltos de linea
        contenido = article.text #.replace('\n', ' ').replace('\r', ' ')

        #agregamos al campo contenido, lo que hay en la variable contenido(el texto del article
        item.add_value('contenido', contenido)

        yield item.load_item()























