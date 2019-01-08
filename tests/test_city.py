from src.models.city import City

from unittest import TestCase


class TestCity(TestCase):

    def test_can_create_city_list_using_json(self):
        City()

    def test_can_create_city_list_using_web_downloaded_xml(self):
        City(use_json=False)

    def test_city_with_json_are_same_as_city_with_xml(self):
        cities_with_json = City()
        cities_with_xml = City(use_json=False)

        self.assertEqual(cities_with_json.cities, cities_with_xml.cities)
