#!/usr/bin/env python

import json


k = []
items = []

historico = json.load(open('historico.json'))
hurls = [h.get('url') for h in historico]
try:
    nuevas = json.load(open('slide.json'))

    for x in nuevas:
        l = x.get('url')
        if l not in hurls:
            historico.append(x)
            hurls.append(l)

    #save historico
    json.dump(historico, open('historico.json', 'w'))

    # add id
    for n, i in enumerate(historico):
        i['id'] = n

    datos = {"items": historico,
            "types": {
                "Item": {
                    "label": "recurso",
                    "pluralLabel": "recursos"
                }
            },
            "properties": {"plays": {"valueType": "number"}}
            }

    json.dump(datos, open('misdatos.json', 'w'))
except:
    print "No hay datos en slide.json"
