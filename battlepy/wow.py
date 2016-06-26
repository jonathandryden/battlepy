# battlepy
# Copyright 2016 Jonathan Dryden
# See LICENSE for details
from battlepy.api import API


class WorldOfWarcraft(API):

    def get_achievement(self, achievement_id):
        return self.get('/wow/achievement/{}?'.format(achievement_id))

    def get_auctions(self, realm):
        return self.get('/wow/auction/data/{}?'.format(realm))

    def get_bosses(self):
        return self.get('/wow/boss/?')

    def get_boss(self, boss_id):
        return self.get('/wow/boss/{}?'.format(boss_id))

    def get_realm_leaderboard(self, realm):
        return self.get('/wow/challenge/{}?'.format(realm))

    def get_region_leadboard(self, region):
        return self.get('/wow/challenge/region?')

    def get_character_data(self, realm, character_name, data_set = ''):
        return self.get('/wow/character/{}/{}?fields={}&'.format(realm,
            character_name, data_set))

    def get_pvp_leaderboards(self, bracket):
        return self.get('/wow/leaderboard/{}?'.format(bracket))

    def get_quest(self, quest_id):
        return self.get('/wow/quest/{}?'.format(quest_id))

    def get_realm_status(self):
        return self.get('/wow/realm/status?')

    def get_recipe(self, recipe_id):
        return self.get('/wow/recipe/{}?'.format(recipe_id))

    def get_spell(self, spell_id):
        return self.get('/wow/spell/{}?'.format(spell_id))

    def get_zone_list(self, spell_id):
        return self.get('/wow/zone/?')

    def get_zone(self, zone_id):
        return self.get('/wow/zone/{}?'.format(zone_id))

    def get_battlegroups(self):
        return self.get('/wow/data/battlegroups/?')

    def get_races(self):
        return self.get('/wow/data/races?')

    def get_classes(self):
        return self.get('/wow/data/classes?')

    def get_achievements(self):
        return self.get('/wow/data/character/achievements?')

    def get_guild_rewards(self):
        return self.get('/wow/data/guild/rewards?')

    def get_guild_perks(self):
        return self.get('/wow/data/guild/perks?')

    def get_guild_achievements(self):
        return self.get('/wow/data/guild/achievements?')

    def get_item_classes(self):
        return self.get('/wow/data/item/classes?')

    def get_talents(self):
        return self.get('/wow/data/talents?')

    def get_pet_types(self):
        return self.get('/wow/data/pet/types?')