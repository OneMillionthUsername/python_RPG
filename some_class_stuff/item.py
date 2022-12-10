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

	def __init__(self) -> None:
		pass
	
	def __init__(self, name, price, strength, agility, intelligence, health, mana, level, rarity) -> None:
		self.Name = name
		self.Price = price
		self.Strength = strength
		self.Agility = agility
		self.Intelligence = intelligence
		self.Healthbonus = health
		self.Manabonus = mana
		self.Levelbonus = level
		self.Rarity = self.Rarity[rarity]
		self.Drop_chance = self.item_calc_dropchance()
	
	def item_print(self):
		print('Name:',self.Name, 'Price:',self.Price, 'Gold:', 'Strength:',self.Strength, 'Agility:',self.Agility, 'Intelligence:',self.Intelligence, 'Healthbonus:',self.Healthbonus, 'Manabonus:',self.Manabonus, 'Levelbonus:',self.Levelbonus, 'Rarity:',self.Rarity, 'Dropchance:', self.Drop_chance)

	def item_calc_dropchance(self) -> bool:
		self.Drop_chance = r.randint(1,100)
		if self.Drop_chance in range(1, 15):
			return True
		else:
			return False