# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

'''
"imagen": "http://image.slidesharecdn.com/mapadelasestaciones-150313011821-conversion-gate01/95/mapa-de-las-estaciones-del-ao-en-formato-ppt-1-638.jpg?cb=1426227529",
        "url": "http://es.slideshare.net/JosManuelMarcos/mapa-de-las-estaciones-del-ao-en-formato-ppt",
        "fecha": "13 de marzo de 2015",
        "label": "Mapa de las estaciones del a\u00f1o (en formato ppt).",
        "autor": ["Jos\u00e9 Manuel Marcos Rodrigo"],
        "id": "mapa-de-las-estaciones-del-ao-en-formato-ppt",
        "desc": "Mapa sencillo para explicar el paso de las Estaciones asociado al movimiento de traslaci\u00f3n de la Tierra alrededor del Sol."
    }
    '''

import scrapy


class SlideshareItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    label = scrapy.Field()
    fecha = scrapy.Field()
    url = scrapy.Field()
    autor = scrapy.Field()
    id = scrapy.Field()
    desc = scrapy.Field()
    imagen = scrapy.Field()
    lang = scrapy.Field()
    plays = scrapy.Field()







