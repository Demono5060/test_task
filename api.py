import requests
import json


class Api:
    def __init__(self, url: str, api_key: str):
        self.url = url
        self.api_key = api_key

    def find_address(self, address: str) -> dict:
        return json.loads(requests.post(self.url, json={'query': address},
                                        headers={'Authorization': 'Token ' + self.api_key,
                                                 'Content-Type': 'application/json',
                                                 'Accept': 'application/json'}).text).get('suggestions')
