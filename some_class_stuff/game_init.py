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

	# path = Path.joinpath(Path.cwd(), "save.json")
	
	# if Path.exists(path) and path.stat().st_size > 0:
	# 	loadPlayer = json.loads(path.read_text())
	# 	player = Player.load_player(loadPlayer)
	# else:
	player = Player('Warrior', 'Dean', 1, 0, 17, 10, 7, 100, None, None, 0,100)
	player.save_player()
  
	while condition:
		#init player
		#init monster
		monster = Monster(4)
		f.fight(player, monster)
		if player.Level == 99:
			condition = False
		else:
			print('Menu:')
			print('I for inventory')
			print('F for fight')
			userinput = input('Chose a command')
			if userinput.lower() == 'i':
				player.player_inventory_print()
			elif userinput.lower() != 'i':
				pass
			condition = True
		count += 1
	#print('Number of fights for this item rarity:', count)

if __name__ == "__main__":
	main()