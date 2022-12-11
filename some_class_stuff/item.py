import random as r

class Item():
	Name = None
	Price = 0
	Strength = None
	Agility = None
	Intelligence = None
	Healthbonus = None
	Manabonus = None 
	Levelbonus = None
	Drop_chance = None
	Rarity = ['normal', 'magic', 'rare', 'epic', 'unique', 'legendary']
	weapon_names_warrior = ["Sword", "Shield", "Axe"]
	weapon_names_magician = ["Staff", "Wand", "Papyrus"]
	weapon_names_bowmaster = ["Bow", "Crossbow", "Slingshot"]
	pool = []
	
	def __init__(self, name, price, strength, agility, intelligence, health, mana, level, chance, rarity = 0) -> None:
		self.Name = name
		self.Price = price
		self.Strength = strength
		self.Agility = agility
		self.Intelligence = intelligence
		self.Healthbonus = health
		self.Manabonus = mana
		self.Levelbonus = level
		self.Drop_chance = chance
		self.set_item_rarity()
	
	def item_print(self):
		print('Name:',self.Name, 'Price:',self.Price, 'Gold:', 'Strength:',self.Strength, 'Agility:',self.Agility, 'Intelligence:',self.Intelligence, 'Healthbonus:',self.Healthbonus, 'Manabonus:',self.Manabonus, 'Levelbonus:',self.Levelbonus, 'Rarity:',self.Rarity, 'Dropchance:', self.Drop_chance)

	def set_item_rarity(self):
		if self.Drop_chance <= 2:
			self.Rarity = self.Rarity[5]
		elif self.Drop_chance <= 4:
			self.Rarity = self.Rarity[4]
		elif self.Drop_chance <= 8:
			self.Rarity = self.Rarity[3]
		elif self.Drop_chance <= 16:
			self.Rarity = self.Rarity[2]
		elif self.Drop_chance <= 32:
			self.Rarity = self.Rarity[1]
		else:
			self.Rarity = self.Rarity[0]

	def item_pool_init(self):
		j = 0
		for j in range(10):
			item = Item(self.weapon_names_warrior[r.randint(0,2)], r.randint(5,15), r.randint(1,5), r.randint(1,4), r.randint(1,2), r.randint(1,10) * 10, 0, r.randint(1,5), r.randint(1,100))
			self.pool.append(item)
			j += 1