from item import Item
import json
from dataclasses import dataclass
import random as r

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
	Expirience: int
	Exp_needed_for_level_up: int

	def __init__(self, playclass, name, level,money, str, agi, int, rage,spirit, eva, exp, exp_for_level_up) -> None:
		#x = input(f'Welcome {self.name}! Select a class: W for warrior, M for Magician, B for Bowmaster\n')
		self.Name = name
		self.Level = level
		self.Money = money
		self.Expirience = exp
		self.Exp_needed_for_level_up = exp_for_level_up
		x = 'w' #str(input("Wählen Sie eine Klasse: "))
		match x.lower():
			case 'w':
				self.PlayClass = playclass
				self.Strength = str
				self.Agility = agi
				self.Intelligence = int
				self.Health = self.Strength * 15
				self.Health_default = self.Health
				self.Mana = self.Intelligence * 10
				self.Ragepoints = rage
			case 'm':
				self.PlayClass = playclass
				self.Strength = str
				self.Agility = agi
				self.Intelligence = int
				self.Health = self.Strength * 10
				self.Mana = self.Intelligence * 15
				self.Spiritpoints = spirit
			case 'b':
				self.PlayClass = playclass
				self.Strength = str
				self.Agility = agi
				self.Intelligence = int
				self.Health = self.Agility * 10
				self.Mana = self.Intelligence * 10
				self.Evasion = eva

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
  
# 	def health_curve_log(self, health):
# # 1/3 health bonus from level, 1/3 from gear, 1/3 from combination.
# # max_health = 9999 => ~ 3333 from level, 3333 from gear, 3333 from combination.
# 		f = open("health_table.txt", "a")
# 		f.write(f'{self.Level}; {health}\n')
# 		f.close()
  
	def inventory_log(self):
		#f = open("inventory_table.txt", "w")
		for i in self.Items:
			print(i.item_print())
			#f.write(i.item_print())
		#f.close()
  		
	def player_level_up(self):
		while self.Expirience > self.Exp_needed_for_level_up:
			self.Expirience -= self.Exp_needed_for_level_up
			if self.Level != 1:
				self.Exp_needed_for_level_up = self.Exp_needed_for_level_up + (self.Level - 1) * 100
			else:
				self.Exp_needed_for_level_up += 100
			self.Level += 1
			print('Congratulations! You are now level', self.Level)
# changing stats depends on playerclass
			strength = r.randint(1, 3)
			print('Strength ', self.Strength, '->', (self.Strength + strength), ' => +', strength)
			self.Strength += strength
			self.Health_default = self.Strength * 15
			#self.health_curve_log(self.Health_default)
			intelligence = r.randint(1, 1)
			print('Intelligence', self.Intelligence, '->', (self.Intelligence + intelligence), ' => +', intelligence)
			self.Intelligence += intelligence
			agility = r.randint(1, 2)
			print('Agility', self.Agility, '->', (self.Agility + agility), ' => +', agility)
			self.Agility += agility
			#self.level_curve_log()

	def player_get_class(self):
		return self.playClass

	def player_get_money(self):
		return self.money
	
	def player_add_money(self, m):
		self.money += m

	def player_spend_money(self, m):
		self.money -= m

	def player_inventory_print(self):
		print(self.Items)

	@classmethod
	def load_player(self, data) -> 'Player':
		name = str(data.get("Name"))
		playclass = str(data.get("PlayClass"))
		strength = int(data.get("Strength"))
		agi = int(data.get("Agility"))
		intelligence = int(data.get("Intelligence"))
		exp = int(data.get("Expirience"))
		exp_for_level_up = int(data.get("Exp_needed_for_level_up"))
		if data.get("Ragepoints") != None:
			rage = int(data.get("Ragepoints"))
		else:
			rage = 0
		if data.get("Spiritpoints") != None:
			spirit = int(data.get("Spiritpoints"))
		else:
			spirit = 0
		if data.get("Evasion") != None:
			eva = int(data.get("Evasion"))
		else:
			eva = 0
		level = int(data.get("Level"))
		money = int(data.get("Money"))
		return Player(playclass, name, level, money, strength, agi, intelligence, rage, spirit, eva, exp, exp_for_level_up)

	def save_player(self):
		savePlayer = json.dumps(self.__dict__)
		with open("save.json", "w") as outfile:
			outfile.write(savePlayer)