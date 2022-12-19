import random as r
from colorama import Fore


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
	Rarity = [Fore.WHITE + 'normal', Fore.BLUE + 'magic', Fore.YELLOW + 'rare', Fore.MAGENTA + 'epic', Fore.CYAN + 'unique', Fore.RED + 'legendary']
	weapon_names_warrior = ["Sword", "Shield", "Axe"]
	weapon_names_magician = ["Staff", "Wand", "Papyrus"]
	weapon_names_bowmaster = ["Bow", "Crossbow", "Slingshot"]
	pool = []
 
	def __init__(self) -> None:
		self.Name = self.weapon_names_warrior[r.randint(0, len(self.weapon_names_warrior)-1)]
		self.Price = r.randint(10, 50)
		self.Strength = r.randint(1, 10)
		self.Agility = r.randint(1, 5)
		self.Intelligence = 0
		self.Healthbonus = r.randint(10,20)
		self.Manabonus = 0
		self.Levelbonus = 0
		self.Drop_chance = r.randint(1, 100)
		self.set_item_rarity()
	
	def Item_create(self, name, price, strength, agility, intelligence, health, mana, level, chance, rarity = 0):
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
		return str(f'### Name: {self.Name} ###\nPrice: {self.Price} Strength: {self.Strength} Agility: {self.Agility} Intelligence: {self.Intelligence} Healthbonus: {self.Healthbonus} Manabonus: {self.Manabonus} Levelbonus: {self.Levelbonus} Rarity: {self.Rarity} Dropchance: {self.Drop_chance}\n')

	def set_item_rarity(self):
		if self.Drop_chance <= 2:
			self.Rarity = self.Rarity[5]
		elif self.Drop_chance <= 4: #error - drop chance is 2% not 4
			self.Rarity = self.Rarity[4]
		elif self.Drop_chance <= 8: #drop chance is 4% not 8
			self.Rarity = self.Rarity[3]
		elif self.Drop_chance <= 16:
			self.Rarity = self.Rarity[2]
		elif self.Drop_chance <= 32:
			self.Rarity = self.Rarity[1]
		else:
			self.Rarity = self.Rarity[0]

	def item_pool_init(self, level = 5):
		j = 0
		for j in range(level):
			item = Item()
			#fo Item_create
			#item = Item(self.weapon_names_warrior[r.randint(0,2)], r.randint(5,15), r.randint(1,5), r.randint(1,4), r.randint(1,2), r.randint(1,10) * 10, 0, r.randint(1,5), r.randint(1,100))
			self.pool.append(item)
			j += 1