import unittest
from unittest.mock import MagicMock

from ipvanish.services import Server, IPVanishService, DataLoader
from os.path import dirname
from json import load


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.full_test_data = open(dirname(__file__) + '/test-data-full.json')
        self.file = open(dirname(__file__) + '/test-data-small.json')

    def test_deserialize_response_with_full_file(self):
        loader = DataLoader()
        result = loader.deserialize_response(self.full_test_data)
        self.assertEqual(1079, len(result))

    def test_deserialize_response_with_small_file(self):
        parser = DataLoader()
        result = parser.deserialize_response(self.file)
        self.assertEqual(16, len(result))

    def test_deserialize_response_should_create_valid_server_entity(self):
        server = Server('ams-a22.ipvanish.com', 18, 'Netherlands', 'Amsterdam')
        loader = DataLoader()
        result = loader.deserialize_response(self.file)
        self.assertEqual(server, result[2])

    def test_get_data_should_return_list_when_given_a_file(self):
        data = DataLoader.get_data(self.file)
        self.assertTrue(isinstance(data, list))

    def test_get_data_should_return_list_when_given_json(self):
        data = DataLoader.get_data(load(self.file))
        self.assertTrue(isinstance(data, list))

    def test_get_data_should_raise_exception_when_type_is_wrong(self):
        with self.assertRaises(TypeError):
            DataLoader.get_data(None)

    def tearDown(self):
        self.full_test_data.close()
        self.file.close()


class TestIPVanishParser(unittest.TestCase):
    def setUp(self):
        self.servers = [
            Server('host1', 30, 'Netherlands', 'Amsterdam'),
            Server('host2', 25, 'Denmark', 'Copenhagen'),
            Server('host3', 10, 'Netherlands', 'Amsterdam'),
            Server('host4', 7, 'Denmark', 'Copenhagen'),
            Server('host5', 62, 'Netherlands', 'Amsterdam'),
            Server('host6', 5, 'United Kingdom', 'London'),
            Server('host7', 4, 'United Kingdom', 'London')
        ]

    def test_search_should_return_all_results_given_no_arguments(self):
        ip_vanish = IPVanishService()
        ip_vanish.loader.load = MagicMock(return_value=self.servers)
        results = ip_vanish.search("", None)
        self.assertEqual(7, len(results))

    def test_search_should_apply_country_filter_given_relevant_argument(self):
        ip_vanish = IPVanishService()
        ip_vanish.loader.load = MagicMock(return_value=self.servers)
        arg = MagicMock()
        arg.country = "Denmark"
        results = ip_vanish.search(None, arg)
        self.assertEqual(2, len(results))
        self.assertEqual('host4', results[0].name)

    def test_filter_by_country_should_only_return_servers_where_country_name_matches(self):
        ip_vanish = IPVanishService()
        result = ip_vanish.filter_by_country(self.servers, 'Netherlands')
        self.assertEqual(3, len(result))

    def test_filter_by_country_should_only_return_servers_where_country_name_matches_bi_gram(self):
        ip_vanish = IPVanishService()
        result = ip_vanish.filter_by_country(self.servers, 'United Kingdom')
        self.assertEqual(2, len(result))

    def test_filter_by_country_should_not_return_anything_when_server_list_is_empty(self):
        ip_vanish = IPVanishService()
        result = ip_vanish.filter_by_country([], 'Netherlands')
        self.assertEqual(0, len(result))


class TestServer(unittest.TestCase):
    def test_str_should_return_correctly_formatted_string(self):
        server = Server("server-name", 12, "Denmark", "Copenhagen")
        self.assertEqual("Server server-name in Copenhagen,Denmark is at 12%", str(server))

    def test_eq_should_return_true_when_identity_is_the_same(self):
        server = Server("server-name", 12, "Denmark", "Copenhagen")
        similar_server = Server("server-name", 12, "Denmark", "Copenhagen")
        self.assertEqual(server, similar_server)

    def test_eq_should_not_return_true_when_names_does_not_match(self):
        server = Server("server-name", 12, "Denmark", "Copenhagen")
        similar_server = Server("server-name-2", 12, "Denmark", "Copenhagen")
        self.assertNotEqual(server, similar_server)

    def test_eq_should_not_return_true_when_capacity_is_different(self):
        server = Server("server-name", 12, "Denmark", "Copenhagen")
        similar_server = Server("server-name", 10, "Denmark", "Copenhagen")
        self.assertNotEqual(server, similar_server)

    def test_eq_should_not_return_true_when_country_is_different(self):
        server = Server("server-name", 12, "Denmark", "Copenhagen")
        similar_server = Server("server-name", 12, "Sweden", "Copenhagen")
        self.assertNotEqual(server, similar_server)

    def test_eq_should_not_return_true_when_city_is_different(self):
        server = Server("server-name", 12, "Denmark", "Copenhagen")
        similar_server = Server("server-name", 12, "Denmark", "Greve")
        self.assertNotEqual(server, similar_server)