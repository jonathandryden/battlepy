import unittest
from battlepy.api_client import Client


class WowApiTests(unittest.TestCase):

    def create_client(self):
        return Client()

    def test_get_achievement(self):
        bnet = self.create_client().wow
        achievment_id = 2144
        resp = bnet.get_achievement(achievment_id)

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

    # def test_realm_status(self):
    #     bnet = self.create_client().wow
    #     resp = bnet.get_realm_status()
    #
    #     self.assertTrue(resp.status_code == 200)