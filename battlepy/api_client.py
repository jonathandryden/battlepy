# battlepy
# Copyright 2016 Jonathan Dryden
# See LICENSE for details
from battlepy.wow import WorldOfWarcraft


class Client(object):
    # Defaults here or pass them via constructor
    def __init__(self, api_key = '', region = '', locale = ''):
        self.wow = WorldOfWarcraft(api_key, region, locale)