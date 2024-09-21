import scrapy


class BookItem(scrapy.Item):

    isbn = scrapy.Field()
    titulo = scrapy.Field()
    autor = scrapy.Field()
    editorial = scrapy.Field()
    materia = scrapy.Field()
    fecha = scrapy.Field()

class BookDetailItem(scrapy.Item):

    isbn = scrapy.Field()
    autor = scrapy.Field()
    autores = scrapy.Field()
    colaborador = scrapy.Field()
    colaboradores = scrapy.Field()
    editorial = scrapy.Field()
    materia = scrapy.Field()
    publico_objetivo = scrapy.Field()
    publicado = scrapy.Field()
    numero_de_edicion = scrapy.Field()
    numero_de_paginas = scrapy.Field()
    tamano = scrapy.Field()
    precio = scrapy.Field()
    soporte = scrapy.Field()
    formato = scrapy.Field()
    idioma = scrapy.Field()