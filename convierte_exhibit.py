import json



k = []
items = []

text = open('slide.json').read()

text = text.replace('][', ',')
n = json.loads(text)

for x in n:
    l = x.get('url')
    if l not in k:
        items.append(x)
        k.append(l)


# add id
for n, i in enumerate(items):
    i['id'] = n

datos = {"items": items,
        "types": {
            "Item": {
                "label": "recurso",
                "pluralLabel": "recursos"
            }
        },
        "properties": {"plays": {"valueType": "number"}}
        }

json.dump(datos, open('slide.js', 'w'))
