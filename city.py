import json
import urllib.request
from urllib.request import urlretrieve
import time


import xml.etree.ElementTree as ElementTree


class City:
    cities = {}

    def __init__(self, use_json=False, city_url="http://dd.weather.gc.ca/citypage_weather/xml/siteList.xml"):
        if use_json is True:
            with open('data/city/cities.json') as json_file:
                self.cities = json.load(json_file)

        else:
            try:
                urlretrieve(city_url, "../../data/city/city.xml")

            except IOError:
                raise IOError('Can\'t access the list of city from the Government of Canada website')

            city_tree = ElementTree.ElementTree()
            city_tree.parse('../../data/city/city.xml')
            cities = city_tree.findall("site")

            for city in cities:
                city_code = city.attrib["code"]

                self.cities[city_code] = {
                    'english_name': city.findtext('nameEn'),
                    'french_name': city.findtext('nameFr'),
                    'province': city.findtext("provinceCode"),
                }
     
    def getXMLSitePages(self):                 #Requests the .xml file for each city, waits 1 second before requesting next
        province_url='http://dd.weather.gc.ca/citypage_weather/xml'
        for key in self.cities:
            code = key
            filename = "../../data/city/" + code + ".xml"
            province = self.cities[code]["province"]
            cityUrl = province_url + "/"+ province + "/" + code + "_e.xml"
            page = urlretrieve(cityUrl, filename)
            print("retrieved :" + cityUrl)
            time.sleep(1)
            
    def getTemperature(self):                 #Examines the .xml files extracted with the getXMLSitePages method and extracts the temperature one by one
        for  key in self.cities:              #Not fully functional - most .xml files do not have data inside temperature tags or maybe I'm retarded
            filename = "../../data/city/" + key + ".xml"
            info_tree = ElementTree.ElementTree()
            info_tree.parse(filename)
            cityInfo = info_tree.findall("currentCondition")
            temperature = cityInfo[5][5].text
            print(key + " : " + temperature)
