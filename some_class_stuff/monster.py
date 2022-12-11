import random as rnd
from item import Item

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
	Mana_default = None
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
		self.Mana_default = self.Mana
		self.Expirience_give = self.Level * self.Strength
		self.Money = self.Level * rnd.randint(10,30)
		self.Chance_to_drop_item = 100/rnd.randint(1, 200)
		self.item_pool_init()

	def health_reset(self):
		if self.Health_default != None:
			self.Health = self.Health_default

	def item_pool_init(self, level = 5):
		i = 0
		for i in range(level):
			item = Item()
			#fo Item_create
			#item = Item(self.weapon_names_warrior[r.randint(0,2)], r.randint(5,15), r.randint(1,5), r.randint(1,4), r.randint(1,2), r.randint(1,10) * 10, 0, r.randint(1,5), r.randint(1,100))
			self.Items.append(item)
			i += 1