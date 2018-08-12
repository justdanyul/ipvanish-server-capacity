import requests
from json import load
from io import TextIOWrapper
from ipvanish.model import Server


class DataLoader:
    def load(self, url: str):
        try:
            request = requests.get(url)
            return self.deserialize_response(request.json())
        except requests.exceptions.RequestException:
            print("There was a problem connecting to IPVanish")

    @staticmethod
    def get_data(json: object):
        if isinstance(json, TextIOWrapper):
            return load(json)
        elif isinstance(json, list):
            return json
        else:
            raise TypeError()

    def deserialize_response(self, json: object):
        data = self.get_data(json)
        servers = []
        for entry in data:
            server = Server(entry['properties']['hostname'],
                            entry['properties']['capacity'],
                            entry['properties']['country'],
                            entry['properties']['city'])
            servers.append(server)
        return servers


class IPVanishService:
    def __init__(self):
        self.loader = DataLoader()

    def search(self, url, args):
        data = self.loader.load(url)
        if args and args.country:
            data = self.filter_by_country(data, args.country)
        return self.sort_by_capacity(data)

    @staticmethod
    def filter_by_country(server_list: list, country: str):
        return list(filter(lambda server: server.country == country, server_list))

    @staticmethod
    def sort_by_capacity(server_list: list):
        return sorted(server_list, key=lambda x: x.capacity)
