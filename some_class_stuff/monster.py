import random as r
from item import Item

class Monster():
	Name = ['Dragon', 'Bat', 'Bug', 'Wolf', 'Spider', 'Lion', 'Dinosaur', 'Whale', 'Kakadu']
	Kind = ['Reptile', 'Arachnoid', 'Fish', 'Bird', 'Ancient', 'Notoriouts', 'Boss', 'Feral', 'Insect', 'Humanoid', 'Ghost', 'Energy']
	ElementType = ['Water', 'Electro', 'Air', 'Earth', 'Light', 'Dark', 'Holy', 'Unholy', 'God']
	Battle_class = ['Flying', 'Swimming', 'Normal', 'Furious', 'Tame', 'Aggressive', 'Anxious']
	Items = []
	Level = 1
	Money = 0
	Strength: int
	Agility: int
	Intelligence: int
	Health: int
	Health_default: int
	Mana: int
	Mana_default: int
	Rage: int
	Spirit: int
	Evasion: int
	Expirience_give: int
	Chance_to_drop_item: float
	Expirience: int
	Exp_needed_for_level_up: int
	Drop_seed = 200 
 
	def	__init__(self, max_level) -> None:
		self.Name = self.Name[r.randint(0, len(self.Name)-1)]
		self.Battle_class = self.Battle_class[r.randint(0, len(self.Battle_class)-1)]
		self.Kind = self.Kind[r.randint(0, len(self.Kind)-1)]
		self.ElementType = self.ElementType[r.randint(0, len(self.ElementType)-1)]
		self.Level = r.randint(1,max_level)
		self.Strength = self.Level * r.randint(1,self.Level *10)
		self.Agility = self.Level * r.randint(1,self.Level *7)
		self.Intelligence = self.Level * r.randint(1,self.Level *3)
		self.Health = r.randint(150,250)
		self.Health_default = self.Health
		self.Mana = self.Intelligence * self.Level
		self.Mana_default = self.Mana
		self.Expirience_give = 5000 #self.Level * self.Strength
		self.Money = self.Level * r.randint(10,30)
		self.Chance_to_drop_item = 100/r.randint(1, 200)
		self.item_pool_init()

	def health_reset(self):
		if self.Health_default >= self.Health:
			self.Health = self.Health_default

	def item_pool_init(self, level = 5):
		i = 0
		for i in range(level):
			item = Item()
			#fo Item_create
			#item = Item(self.weapon_names_warrior[r.randint(0,2)], r.randint(5,15), r.randint(1,5), r.randint(1,4), r.randint(1,2), r.randint(1,10) * 10, 0, r.randint(1,5), r.randint(1,100))
			self.Items.append(item)
			i += 1
	def monster_level_up(self):
		while self.Expirience > self.Exp_needed_for_level_up:
			self.Expirience -= self.Exp_needed_for_level_up
			if self.Level != 1:
				self.Exp_needed_for_level_up = self.Exp_needed_for_level_up + (self.Level - 1) * 100
			else:
				self.Exp_needed_for_level_up += 100
			self.Level += 1
			#print('Congratulations! You are now level', self.Level)
	# changing stats depends on playerclass
			strength = r.randint(1, 3)
			#print('Strength ', self.Strength, '->', (self.Strength + strength), ' => +', strength)
			self.Strength += strength
			self.Health_default = self.Strength * 15
			#self.health_curve_log(self.Health_default)
			intelligence = r.randint(1, 1)
			#print('Intelligence', self.Intelligence, '->', (self.Intelligence + intelligence), ' => +', intelligence)
			self.Intelligence += intelligence
			agility = r.randint(1, 2)
			#print('Agility', self.Agility, '->', (self.Agility + agility), ' => +', agility)
			self.Agility += agility
			#self.level_curve_log()