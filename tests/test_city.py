from src.city import City

from xml.etree.ElementTree import ParseError

from unittest import TestCase


class TestCity(TestCase):
    def setUp(self):
        self.cities = City()

    def test_can_create_city_list_using_web_downloaded_xml(self):
        City(use_json=False)

    def test_city_with_json_are_same_as_city_with_xml(self):
        cities_with_json = self.cities
        cities_with_xml = City(use_json=False)

        self.assertListEqual(cities_with_json.cities, cities_with_xml.cities)

    def test_can_get_correct_city_with_name(self):
        dolbeau_mistassini_dict = {
            'id': 's0000270',
            'english_name': 'Dolbeau-Mistassini',
            'french_name': 'Dolbeau-Mistassini',
            'province': 'QC',
        }

        dolbeau_mistassini = self.cities.find_city('Dolbeau-Mistassini')

        self.assertEqual(dolbeau_mistassini, dolbeau_mistassini_dict)

    def test_cannot_get_City_that_doesnt_exist(self):
        incorrect_city = self.cities.find_city('ABCDEFG')

        self.assertIsNone(incorrect_city)

    def test_bad_city_url_raises_exception(self):
        with self.assertRaises(ParseError):
            City(use_json=False, url='http://www.google.com')
