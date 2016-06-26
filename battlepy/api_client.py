# battlepy
# Copyright 2016 Jonathan Dryden
# See LICENSE for details
from battlepy.wow import WorldOfWarcraft


class Client(object):

    def __init__(self, api_key = '', region = 'us', locale = 'en_US'):
        self.wow = WorldOfWarcraft(api_key, region, locale)