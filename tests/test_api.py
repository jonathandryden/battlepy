import unittest
from battlepy.api_client import Client


class WowApiTests(unittest.TestCase):

    def create_client(self):
        return Client()

    def test_get_achievement(self):
        bnet = self.create_client().wow
        achievment_id = 2144
        resp = bnet.get_achievement(achievment_id)
        print(resp)
        self.assertTrue(achievment_id == resp['id'])

    def test_get_auctions(self):
        bnet = self.create_client().wow
        resp = bnet.get_auctions('medivh')

        self.assertTrue(len(resp['files'][0]) == 2)

    def test_get_bosses(self):
        bnet = self.create_client().wow
        resp = bnet.get_bosses()

        self.assertTrue(len(resp['bosses']) > 0)

    def test_get_boss(self):
        bnet = self.create_client().wow
        boss_id = 24723
        resp = bnet.get_boss(24723)

        self.assertTrue(boss_id == resp['id'])

    def test_get_realm_leaderboard(self):
        bnet = self.create_client().wow
        realm_id = 'Medivh'
        resp = bnet.get_realm_leaderboard(realm_id)

        self.assertTrue(realm_id == resp['challenge'][0]['realm']['name'])

    def test_get_region_leaderboard(self):
        bnet = self.create_client().wow
        realm_id = 'Medivh'
        resp = bnet.get_region_leaderboard()

        self.assertTrue(len(resp['challenge']) > 0)

    def test_get_character_profile(self):
        bnet = self.create_client().wow
        realm_id = 'Medivh'
        char_name = 'Bob'
        resp = bnet.get_character_data(realm_id, char_name)

        self.assertTrue(char_name == resp['name'])

    def test_get_character_achievements(self):
        bnet = self.create_client().wow
        realm_id = 'Medivh'
        char_name = 'Bob'
        resp = bnet.get_character_data(realm_id, char_name, 'achievements')

        self.assertTrue(resp['achievementPoints'] >= 0)