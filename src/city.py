import json
from urllib.request import urlretrieve
import xml.etree.ElementTree as ElementTree


class City:
    _url = 'http://dd.weather.gc.ca/citypage_weather/xml/siteList.xml'

    def __init__(self):
        self.cities = []

    def __getitem__(self, item):
        return self._find(item)

    def __iter__(self):
        for city in self.cities:
            yield city

    def __contains__(self, item):
        return self._find(item)

    def __len__(self):
        return len(self.cities)

    def _load_from_xml(self, cities_xml='city.xml'):
        city_tree = ElementTree.ElementTree()

        city_tree.parse(cities_xml)
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

    def _find(self, city_name):
        for city in self.cities:
            if city_name == city['english_name'] or city_name == city['french_name']:
                return city

        return None

    def fetch(self):
        urlretrieve(self._url, 'city.xml')

        self._load_from_xml(cities_xml='city.xml')
