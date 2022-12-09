class Item():
	name = None
	price = 0
	Strength = None
	Agility = None
	Intelligence = None
	Healthbonus = None
	Manabonus = None 
	Levelbonus = None
	Rarity = ['normal', 'magic', 'rare', 'epic', 'unique', 'legendary']

	def __init__(self) -> None:
		pass
	
	def __init__(self, name, price, strength, agility, intelligence, health, mana, level, rarity) -> None:
		self.name = name
		self.price = price
		self.Strength = strength
		self.Agility = agility
		self.Intelligence = intelligence
		self.Healthbonus = health
		self.Manabonus = mana
		self.Levelbonus = level
		self.Rarity = self.Rarity[rarity]
	
	def item_print(self):
		print('Name:',self.name, 'Price:',self.price, 'Gold:', 'Strength:',self.Strength, 'Agility:',self.Agility, 'Intelligence:',self.Intelligence, 'Healthbonus:',self.Healthbonus, 'Manabonus:',self.Manabonus, 'Levelbonus:',self.Levelbonus, 'Rarity:',self.Rarity)