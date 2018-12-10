from urllib.request import urlretrieve

import xml.etree.ElementTree as ET


class City:
    cities = {}

    def __init__(self, city_url='http://dd.weather.gc.ca/citypage_weather/xml/siteList.xml'):
        try:
            # TODO: Should open the file that we save instead of downloading it again
            raise FileNotFoundError

        except FileNotFoundError:
            try:
                urlretrieve(city_url, 'data/city/city.xml')

            except IOError:
                raise IOError('Can\'t access the list of city from the Government of Canada website')

        city_tree = ET.ElementTree()
        city_tree.parse('data/city/city.xml')
        cities = city_tree.findall("site")

        for city in cities:
            city_code = city.attrib["code"]

            self.cities[city_code] = {
                'english_name': city.findtext('nameEn'),
                'french_name': city.findtext('nameFr'),
                'province': city.findtext("provinceCode"),
            }
