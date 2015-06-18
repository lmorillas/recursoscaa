#!/bin/sh

rm slide.json
git checkout master

.  env/bin/activate
scrapy crawl arasaac -t json -o slide.json

./convierte_exhibit.py

