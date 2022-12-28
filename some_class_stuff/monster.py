import random as r
from item import Item

class Monster():
	Name = ['Dragon', 'Bat', 'Bug', 'Wolf', 'Spider', 'Lion', 'Dinosaur', 'Whale', 'Kakadu']
	Kind = ['Reptile', 'Arachnoid', 'Fish', 'Bird', 'Ancient', 'Notoriouts', 'Boss', 'Feral', 'Insect', 'Humanoid', 'Ghost', 'Energy']
	ElementType = ['Water', 'Electro', 'Air', 'Earth', 'Light', 'Dark', 'Holy', 'Unholy', 'God']
	Battle_class = ['Flying', 'Swimming', 'Normal', 'Furious', 'Tame', 'Aggressive', 'Anxious']
	Items = []
	Level: int
	Experience: int
	Exp_needed_for_level_up: int
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
	Drop_seed = 200 
 
	def	__init__(self, level) -> None:
		self.Name = self.Name[r.randint(0, len(self.Name)-1)]
		self.Battle_class = self.Battle_class[r.randint(0, len(self.Battle_class)-1)]
		self.Kind = self.Kind[r.randint(0, len(self.Kind)-1)]
		self.ElementType = self.ElementType[r.randint(0, len(self.ElementType)-1)]
		self.Level = round(level)
		self.Strength = self.Level * r.randint(1,self.Level *10)
		self.Agility = self.Level * r.randint(1,self.Level *7)
		self.Intelligence = self.Level * r.randint(1,self.Level *3)
		self.Health = r.randint(150,250)
		self.Health_default = self.Health
		self.Mana = self.Intelligence * self.Level
		self.Mana_default = self.Mana
		self.Expirience_give = self.Level * self.Strength
		self.Money = self.Level * r.randint(10,30)
		self.Chance_to_drop_item = 100/r.randint(1, 200)
		self.item_pool_init()

	def health_reset(self):
		if self.Health_default >= self.Health:
			self.Health = self.Health_default

	def item_pool_init(self, level = 5):
		i = 0
		self.Items = []
		for i in range(level):
			item = Item()
			self.Items.append(item)
			i += 1

	def monster_stats_log(self):
		f = open("monster_stats.txt", "a")
		f.write(f'{self.Level}; {self.Strength}; {self.Agility}; {self.Intelligence}; {self.Health}; {self.Mana} \n')
		f.close()