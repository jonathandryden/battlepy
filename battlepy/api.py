# battlepy
# Copyright 2016 Jonathan Dryden
# See LICENSE for details
import requests


class API(object):

    _host = 'api.battle.net'

    def __init__(self, api_key, region, locale):
        self._api_key = api_key
        self._region = region
        self._locale = locale

    def get(self, path):
        url = 'https://' + self._region + '.' + self._host + path + 'locale=' + self._locale + '&apikey=' + self._api_key
        return requests.get(url)