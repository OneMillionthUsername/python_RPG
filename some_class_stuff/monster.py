import random as rnd
import item_init as ip

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
	Health_default = None
	Mana = None
	Rage = None
	Spirit = None
	Evasion = None
	Expirience_give = None
	Chance_to_drop_item = None
	Drop_seed = 200 
 
	def	__init__(self, name, battle_class, max_level) -> None:
		self.Name = name
		self.Battle_class = battle_class
		self.Level = rnd.randint(1,max_level)
		self.Strength = self.Level * rnd.randint(1,self.Level *10)
		self.Agility = self.Level * rnd.randint(1,self.Level *7)
		self.Intelligence = self.Level * rnd.randint(1,self.Level *3)
		self.Health = rnd.randint(150,250)
		self.Health_default = self.Health
		self.Mana = self.Intelligence * self.Level
		self.Expirience_give = self.Level * self.Strength
		self.Money = self.Level * rnd.randint(10,30)
		self.Chance_to_drop_item = 100/rnd.randint(1, 200)

	def health_reset(self):
		if self.Health_default != None:
			self.Health = self.Health_default

	def monster_add_items(self, item):
		self.items.append(item)

	def set_loot_bag(self, item):
		self.Items = item.copy()