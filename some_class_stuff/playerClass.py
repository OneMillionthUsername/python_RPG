import player as p

class Warrior(p.player):
	def __init__(self) -> None:
		super().__init__()
	strength = 17
	agility = 10
	intelligence = 7
	healthpoints = strength * 15
	manapoints = intelligence * 10
	ragepoints = 100

class Magician(p.player):
	def __init__(self) -> None:
		super().__init__()
	strength = 7
	agility = 10
	intelligence = 17
	healthpoints = strength * 10
	manapoints = intelligence * 15
	spiritpoint = 100

class Bowmaster(p.player):
	def __init__(self) -> None:
		super().__init__()
	strength = 10
	agility = 17
	intelligence = 7
	healthpoints = agility * 10
	manapoints = intelligence * 10
	evasionpoints = 100