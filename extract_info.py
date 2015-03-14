from amara.bindery import html
from amara.lib import U
from urlparse import urljoin


doc = html.parse('http://es.slideshare.net/JosManuelMarcos/presentations')
doc2 = html.parse('http://es.slideshare.net/JosManuelMarcos/presentations/2')

links = []
datos = []

def extract_links(doc):
    return doc.xml_select('//ul[@class="thumbnailFollowGrid"]/li//a')

links.extend(extract_links(doc))
links.extend(extract_links(doc2))

print len(links), 'recursos a extraer ...'

def encode_data(d):
    for k in d.keys():
        d[k] = d[k].encode('utf-8')
    return d

def extract_data(link):
        item = {}
        _link = urljoin('http://es.slideshare.net/', U(link.href))
        _doc = html.parse(_link)
        if doc:
            print _link
            item['url'] = _link
            item['id'] = _link.split('/')[-1]
            item['autor'] = []
            _label = U(_doc.xml_select('//h1[contains(@class, "slideshow-title-text")]')).strip()
            if u'Romero' in _label:
                item['autor'].append('David Romero')
            item['autor'].append(U(_doc.xml_select('//a[@class="j-author-name"]')).strip())
            item['label'] = _label.split('-')[0].strip()
            item['fecha'] = U(_doc.xml_select('//time[@itemprop="datePublished"]')).strip()

            _desc = U(_doc.xml_select('//p[contains(@class, "j-desc-expand")]')).strip()
            if _desc:
                item['desc'] = _desc
            else:
                item['desc'] = U(_doc.xml_select('//div[contains(@class, "j-desc-more")]')).strip()
            item['imagen'] = _doc.xml_select(u'//img[contains(@class, "slide_image")]')[0].src

        return item

datos = [extract_data(l) for l in links]

import json
json.dump({'items': datos}, open('datos.json', 'w'))


'''
    d2 = html.parse(urljoin('http://es.slideshare.net/', l)
print d2.xml_encode()
d2.xml_select('//time')
map(d2.xml_select('//time'), lambda x: print x)
map( lambda x: print x, d2.xml_select('//time'))
lambda x: print x
__version__
version
_version_
print  d2.xml_select('//time')[0]
print  d2.xml_select('//time')[1]
print  d2.xml_select('//time[@itemprop="datePublished"]')
print  d2.xml_select('//time[@itemprop="datePublished"]')[0]
print  d2.xml_select('//time[@itemprop="datePublished"]')[0]
print  d2.xml_select('//a[@class="j-author-name"]/text()')
print  d2.xml_select('//a[@class="j-author-name"]')
print  d2.xml_select('//a[@class="j-author-name"]')
from amara.lib import U
print  U(d2.xml_select('//a[@class="j-author-name"]')).strip()
print  U(d2.xml_select('//div[contains(@class, "j-desc-more")]')).strip()
print  U(d2.xml_select('//a[contains(@class, "j-download")]')).strip()
history
'''