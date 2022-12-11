import item as i

class player():
	PlayClass = None
	Name = None
	Items = []
	Level = 1
	Money = 0
	Strength = None
	Agility = None
	Intelligence = None
	Health = None
	Health_default = None
	Mana = None
	Ragepoints = None
	Spiritpoints = None
	Evasionpoints = None
	Expirience = 0

	def __init__(self, name) -> None:
		self.Name = name
		#x = input(f'Welcome {self.name}! Select a class: W for warrior, M for Magician, B for Bowmaster\n')
		x = 'w'
		match x.lower():
			case 'w':
				self.PlayClass = 'Warrior'
				self.Strength = 17
				self.Agility = 10
				self.Intelligence = 7
				self.Health = self.Strength * 15
				self.Mana = self.Intelligence * 10
				self.Ragepoints = 100
			case 'm':
				self.PlayClass = 'Magician'
				self.Strength = 7
				self.Agility = 10
				self.Intelligence = 17
				self.Health = self.Strength * 10
				self.Mana = self.Intelligence * 15
				self.Spiritpoint = 100
			case 'b':
				self.PlayClass = 'Bowmaster'
				self.Strength = 10
				self.Agility = 17
				self.Intelligence = 7
				self.Health = self.Agility * 10
				self.Mana = self.Intelligence * 10
				self.Evasion = 100
		self.Health_default = self.Health

	def health_reset(self):
		if self.Health_default != None:
			self.Health = self.Health_default
	
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

