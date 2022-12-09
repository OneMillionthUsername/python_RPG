import random as rnd

class Monster():
	def	__init__(self) -> None:
		pass
	level = 1
	items = []
	strength = level * rnd.randint(1,level *3)
	agility = level * rnd.randint(1,level *3)
	intelligence = level * rnd.randint(1,level *3)
	healthpoints = strength * level
	manapoints = intelligence * level
	expirience_give = level * strength

	def monster_add_items(self, item):
		self.items.append(item)

	def monster_set_loot_bag(self, item):
		self.items.append(item)

	def monster_get_loot_bag(self):
		return self.items
		