#!/bin/sh
rm slide.json
scrapy crawl arasaac -t json -o slide.json
