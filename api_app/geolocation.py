import requests


def get_location(ip):
    URL = 'http://api.ipstack.com/'
    API_KEY = '?access_key=095ec7a9c9a1a21123c10d1119c11bdf'
    response = requests.get(URL+ip+API_KEY)
    data = response.content
    # data.pop('location', None)
    # print(data.keys())


# get_location('www.google')