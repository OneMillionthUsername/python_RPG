from player import Player
from monster import Monster
import fight as f
from pathlib import Path
import json
from types import SimpleNamespace
from dataclasses import dataclass, asdict

def main():

	#main
	count = 0
	condition = True

	path = Path.joinpath(Path.cwd(), "save.json")
	
	if Path.exists(path):
		pass
		#player = Player.load_player(json.loads(path.read_text()))
	else:
		pass
	player = Player()
	while condition:
		#init player
		#init monster
		monster = Monster(4)
		f.fight(player, monster)
		if player.Level == 99:
			condition = False
		else:
			condition = True
		count += 1
	#print('Number of fights for this item rarity:', count)

if __name__ == "__main__":
	main()