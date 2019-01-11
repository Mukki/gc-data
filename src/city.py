import json
from urllib.request import urlretrieve

import xml.etree.ElementTree as ElementTree


class City:
    cities = {}

    def __init__(self, use_json=True, city_url='http://dd.weather.gc.ca/citypage_weather/xml/siteList.xml'):
        if use_json is True:
            with open('data/city/cities.json') as json_file:
                self.cities = json.load(json_file)

        else:
            urlretrieve(city_url, 'data/city/city.xml')

            city_tree = ElementTree.ElementTree()
            city_tree.parse('data/city/city.xml')
            cities = city_tree.findall("site")

            for city in cities:
                city_code = city.attrib["code"]

                self.cities[city_code] = {
                    'english_name': city.findtext('nameEn'),
                    'french_name': city.findtext('nameFr'),
                    'province': city.findtext("provinceCode"),
                }
