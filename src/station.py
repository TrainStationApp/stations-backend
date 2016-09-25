import requests
import json


class DigiTrafficStation:

    def __init__(self):
        self.url = 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'
        self.headers = {'Content-Type': 'application/graphql'}

    def get_stops(self):
        pass

    def get_query(self, query):
        response = requests.post(self.url, data=query, headers=self.headers)
        return response.text


station_info = DigiTrafficStation()
station_info.get_stops()