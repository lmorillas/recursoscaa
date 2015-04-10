#!/bin/sh

rm slide.json

.  env/bin/activate
scrapy crawl arasaac -t json -o slide.json
