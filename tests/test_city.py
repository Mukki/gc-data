from src.city import City

from unittest import TestCase


class TestCity(TestCase):
    def setUp(self):
        self.cities = City()
        self.cities._load_from_xml(cities_xml='tests/data/city.xml')

    def test_can_fetch_cities_from_the_web(self):
        self.cities.fetch()
        self.assertGreater(len(self.cities), 0)

    def test_can_get_correct_city_with_name(self):
        athabasca_dict = {
            'id': 's0000001',
            'english_name': 'Athabasca',
            'french_name': 'Athabasca',
            'province': 'AB',
        }

        athabasca = self.cities['Athabasca']

        self.assertEqual(athabasca, athabasca_dict)

    def test_cannot_get_city_that_doesnt_exist(self):
        incorrect_city = self.cities['Atlantis']

        self.assertIsNone(incorrect_city)

    def test_can_iterate_on_all_cities(self):
        expected_cities = [
            {
                "id": "s0000001",
                "english_name": "Athabasca",
                "french_name": "Athabasca",
                "province": "AB"
            },
            {
                "id": "s0000002",
                "english_name": "Clearwater",
                "french_name": "Clearwater",
                "province": "BC"
            },
            {
                "id": "s0000003",
                "english_name": "Valemount",
                "french_name": "Valemount",
                "province": "BC"
            },
            {
                "id": "s0000004",
                "english_name": "Grand Forks",
                "french_name": "Grand Forks",
                "province": "BC"
            },
        ]

        cities_list = [city for city in self.cities]

        self.assertListEqual(expected_cities, cities_list)

    def test_can_check_if_city_is_in_cities(self):
        self.assertIn('Athabasca', self.cities)
        self.assertNotIn('Atlantis', self.cities)
