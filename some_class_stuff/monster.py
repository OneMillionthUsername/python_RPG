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

	def monster_add_items(self, item):
		self.items.append(item)