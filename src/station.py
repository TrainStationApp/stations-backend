import requests
import json


class DigiTrafficStation:

    def __init__(self):
        self.url = 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'
        self.headers = {'Content-Type': 'application/graphql'}

    def get_stops(self):
        stopnum = '4040'
        query = ("{stops(name: \"%s\") {"
                 "   id"
                 "   name"
                 "   wheelchairBoarding"
                 "   }"
                 "}") % (stopnum)
        data = json.loads(self.get_query(query))
        data = data['data']['stops']
        stops = []
        for n in data:
            stops.append(n['name'])
        return stops

    def get_query(self, query):
        response = requests.post(self.url, data=query, headers=self.headers)
        return response.text


