import random as rnd
import item_pool as ip

class Monster():
	Name = None
	Items = []
	Level = 1
	Money = 0
	Battle_class = None
	Strength = None
	Agility = None
	Intelligence = None
	Health = None
	Mana = None
	Rage = None
	Spirit = None
	Evasion = None
	Expirience_give = None
	
	def	__init__(self, name, battle_class, max_level) -> None:
		self.Name = name
		self.Battle_class = battle_class
		self.Level = rnd.randint(1,max_level)
		self.Strength = self.Level * rnd.randint(1,self.Level *10)
		self.Agility = self.Level * rnd.randint(1,self.Level *7)
		self.Intelligence = self.Level * rnd.randint(1,self.Level *3)
		self.Health = rnd.randint(150,250)
		self.Mana = self.Intelligence * self.Level
		self.Expirience_give = self.Level * self.Strength
		self.Money = self.Level * rnd.randint(10,30)

	def monster_add_items(self, item):
		self.items.append(item)

	def set_loot_bag(self, item):
		self.Items = item.copy()
		