import item as i

class player():
	playClass = None
	items = []
	level = 1
	money = 0
	Strength = None
	Agility = None
	Intelligence = None
	Health = None
	Mana = None
	Expirience = None

	def __init__(self) -> None:
		#x = input('Welcome! Select a class: W for warrior, M for Magician, B for Bowmaster\n')
		x = 'w'
		match x.lower():
			case 'w':
				self.playClass = 'Warrior'
			case 'm':
				self.playClass = 'Magician'
			case 'b':
				self.playClass = 'Bowmaster'
	
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