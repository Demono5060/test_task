import requests
import json


class Api:
    def __init__(self, url: str, api_key: str):
        self.url = url
        self.api_key = api_key

    def find_address(self, address: str) -> dict | None:
        r = requests.post(self.url, json={'query': address},
                          headers={'Authorization': 'Token ' + self.api_key,
                                   'Content-Type': 'application/json',
                                   'Accept': 'application/json'})
        if r.status_code == 200:
            return json.loads(r.text).get('suggestions')
        elif r.status_code == 403:
            raise 'Wrong api-key'
