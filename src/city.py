import json
from urllib.request import urlretrieve
import xml.etree.ElementTree as ElementTree


class City:
    def __init__(self, use_json=True, url='http://dd.weather.gc.ca/citypage_weather/xml/siteList.xml'):
        self.cities = []

        if not self.cities:
            self.get_cities(url, use_json)

    def get_cities(self, url, use_json):
        if use_json:
            with open('data/cities.json') as json_file:
                self.cities = json.load(json_file)
        else:
            urlretrieve(url, 'data/city.xml')

            city_tree = ElementTree.ElementTree()
            city_tree.parse('data/city.xml')
            cities = city_tree.findall("site")

            for city in cities:
                self.cities.append(
                    {
                        'id': city.attrib["code"],
                        'english_name': city.findtext('nameEn'),
                        'french_name': city.findtext('nameFr'),
                        'province': city.findtext("provinceCode"),
                    }
                )

    def find_city(self, city_name):
        for city in self.cities:
            if city_name == city['english_name'] or city_name == city['french_name']:
                return city

        return None
