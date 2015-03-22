# -*- coding: utf-8 -*-
import scrapy
from urlparse import urljoin, urlparse
from slideshare.items import SlideshareItem


BASE = 'http://es.slideshare.net/'



class ArasaacSpider(scrapy.Spider):
    name = "arasaac"
    allowed_domains = ["slideshare.net"]

    _urlbase2 = 'http://es.slideshare.net/search/slideshow?lang=es&page={}&q=arasaac&sort=relevance'
    _urlbase = 'http://es.slideshare.net/search/slideshow?ft=all&lang=%2A%2A&page={}&q=arasaac&qid=4941c245-759a-431d-9672-a730e03eb500&searchfrom=header&sort=&ud=year'
    start_urls = [
        'http://es.slideshare.net/search/slideshow?searchfrom=header&q=arasaac',
        ]
    start_urls.extend([_urlbase.format(x) for x in range(1, 300)])
    start_urls.extend([_urlbase2.format(x) for x in range(1, 300)])
    parsed = []

    def extract(self, dato, path):
        x = self.sel.xpath(path)
        if x:
            self.item[dato] = x[0].extract().strip()

    def parse(self, response):
        if 'slideshare.net/search/' in response.url:
            siguientes = response.selector.xpath(u'//a[contains(@class, "iso_slideshow_link")]/@href').extract()
            for s in siguientes:
                path = urlparse(s).path
                if path not in self.parsed:
                    self.parsed.append(path)
                    yield scrapy.Request(urljoin(BASE, path))
        else:

            self.sel = response.selector
            self.item = SlideshareItem()

            path = urlparse(response.url).path
            # item['url'] = path
            self.item['url'] = path
            self.extract('autor', '//a[@class="j-author-name"]/text()')
            self.extract('label', '//h1[@itemprop="headline"]/text()')
            # self.extract('fecha', '//time[@itemprop="datePublished"]/text()')
            self.extract('fecha', '//time[@datetime]/@datetime')
            if self.item['fecha']:
                self.item['fecha'] = self.item['fecha'][:10]

            self.extract('desc', '//p[contains(@class, "j-desc-expand")]/text()')
            if not self.item.get('desc'):
                self.extract('desc', '//div[contains(@class, "j-desc-more")]/text()')

            src_imagen = self.sel.xpath('//img[contains(@class, "slide_image")]/@src')
            if src_imagen:
                self.item['imagen'] = urlparse(src_imagen[0].extract()).path
            else:
                self.extract('imagen', '//meta[@itemprop="thumbnailUrl"]/@content')

            self.extract('lang', '//meta[@itemprop="inLanguage"]/@content')

            if self.item['lang'] == '' or '*' in self.item['lang'] \
                        or '!!' in self.item['lang']:
                self.item['lang'] = 'es'
            self.extract('plays', '//meta[@name="slideshow_view_count"]/@content')
            if self.item.get('plays'):
                self.item['plays'] = int(self.item['plays'])

            yield self.item
