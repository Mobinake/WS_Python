__author__ = 'MOBIN'

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

#extraer informacion de starckoverflow: preguntas

#definimos una clase para almacenar los items
class Pregunta(Item):
    #objeto tipo campo
    pregunta = Field()
    # representar el numero de la pregunta
    id = Field()

#implementamos el spider
class StackOverflowSpider(Spider):

    #nombre al spider
    name = "MiSpider"

    # el url semilla, de donde sacara la informacion
    start_urls = ['https://stackoverflow.com/questions']

    #implementamos un metodo que recibe el responde del link,
    def parse(self, response, **kwargs):

        #creamos un selector que recibe el response como argumento, luego vemos la estructura de la pagina,
        sel = Selector(response)
        #y almacenammos la direccion de las preguntas dentro de la variable (path o css)
        preguntas = sel.xpath('//div[@id="questions"]/div')

        # iterar sobre todas las preguntas, enumerando cada pregunta
        for i, elem in enumerate(preguntas):
            #creamos el item, le pasamos la estructura del item, y el elemento donde esta el xpath
            item = ItemLoader(Pregunta(), elem)

            #agregamos los textos de la pregunta en los items, filtrando segun la estructura de la pagina
            #primero le pasamos a que campo queremos agregar el campo, y luego le damos el xpath
            item.add_xpath('pregunta','.//h3/a/text()')

            #agregamos el id al item
            item.add_value('id', i)

            #una sentencia que retorana el item
            yield item.load_item()




























