from item import Item
import json
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class Player():
	PlayClass: str
	Name: str
	Items = []
	Level: int
	Money: int
	Strength: int
	Agility: int
	Intelligence: int
	Health: int
	Health_default: int
	Mana: int
	Ragepoints: int
	Spiritpoints: int
	Evasionpoints: int
	Expirience = 0
	Exp_needed_for_level_up = 100

#create player
	def __init__(self) -> None:
		#x = input(f'Welcome {self.name}! Select a class: W for warrior, M for Magician, B for Bowmaster\n')
		self.Name = "Dean"
		x = 'w'
		match x.lower():
			case 'w':
				self.PlayClass = 'Warrior'
				self.Strength = 17
				self.Agility = 10
				self.Intelligence = 7
				self.Health = self.Strength * 15
				self.Health_default = self.Health
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

	def health_reset(self):
		if self.Health_default >= self.Health:
			self.Health = self.Health_default
	
	def player_add_item(self, item):
		self.items.append(item)
	
	def player_get_item(self, item) -> Item:
		if item in self.items:
			return item

	#def level_curve_log(self):
		#f = open("exp_table.txt", "a")
		#f.write(f'{self.Level}; {self.#Exp_needed_for_level_up}\n')
		#f.close()
		
	def player_level_up(self):
		while self.Expirience > self.Exp_needed_for_level_up:
			self.Expirience -= self.Exp_needed_for_level_up
			if self.Level != 1:
				self.Exp_needed_for_level_up = self.Exp_needed_for_level_up + (self.Level - 1) * 100
			else:
				self.Exp_needed_for_level_up += 100
			self.Level += 1
			#self.level_curve_log()
			print('Congratulations! You are now level', self.Level)

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

	@classmethod
	def load_player(self, data) -> 'Player':
		self.Name = str(data.get("Name"))
		self.Health_default = int(data.get("Health_default"))
		self.PlayClass = str(data.get("PlayClass"))
		self.Strength = int(data.get("Strength"))
		self.Agility = int(data.get("Agility"))
		self.Intelligence = int(data.get("Intelligence"))
		self.Health = int(data.get("Health"))
		self.Mana = int(data.get("Mana"))
		self.Ragepoints = int(data.get("Ragepoints"))
		self.Expirience = int(data.get("Expirience"))
		self.Exp_needed_for_level_up = int(data.get("Exp_needed_for_level_up"))
		self.Level = int(data.get("Level"))
		self.Money = int(data.get("Money"))
		return Player()

	def save_player(self):
		savePlayer = json.dumps(self.__dict__)
		with open("save.json", "w") as outfile:
			outfile.write(savePlayer)