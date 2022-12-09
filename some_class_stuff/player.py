import item as i

class player():
	playClass = None
	name = None
	items = []
	level = 1
	money = 0
	Strength = None
	Agility = None
	Intelligence = None
	Health = None
	Mana = None
	Ragepoints = None
	Spiritpoints = None
	Evasionpoints = None
	Expirience = None

	def __init__(self, name) -> None:
		self.name = name
		#x = input(f'Welcome {self.name}! Select a class: W for warrior, M for Magician, B for Bowmaster\n')
		x = 'w'
		match x.lower():
			case 'w':
				self.playClass = 'Warrior'
				self.Strength = 17
				self.Agility = 10
				self.Intelligence = 7
				self.Health = self.Strength * 15
				self.Mana = self.Intelligence * 10
				self.ragepoints = 100
			case 'm':
				self.playClass = 'Magician'
				self.Strength = 7
				self.Agility = 10
				self.Intelligence = 17
				self.Healthpoints = self.Strength * 10
				self.Manapoints = self.Intelligence * 15
				self.Spiritpoint = 100
			case 'b':
				self.playClass = 'Bowmaster'
				self.Strength = 10
				self.Agility = 17
				self.Intelligence = 7
				self.Healthpoints = self.Agility * 10
				self.Manapoints = self.Intelligence * 10
				self.Evasionpoints = 100
	
	def player_add_item(self, item):
		self.items.append(item)
	
	def player_get_item(self, item) -> i.Item:
		if item in self.items:
			return item

	def player_add_level(self):
		self.level += 1

	def player_get_class(self):
		return self.playClass

	def player_get_money(self):
		return self.money
	
	def player_add_money(self, m):
		self.money += m

	def player_spend_money(self, m):
		self.money -= m

	def player_inventory_print(self):
		print('Inventory')
		for i in self.items:
			i.item_print()