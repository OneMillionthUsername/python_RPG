from player import Player
from monster import Monster
import fight as f
import keyboard

def main():

	#main
	count = 0
	condition = True

	# path = Path.joinpath(Path.cwd(), "save.json")
	
	# if Path.exists(path) and path.stat().st_size > 0:
	# 	loadPlayer = json.loads(path.read_text())
	# 	player = Player.load_player(loadPlayer)
	# else:
	player = Player('Warrior', 'Toto', 1, 0, 17, 10, 7, 100, None, None, 0,100)
	player.save_player()
  
	while condition:
		count += 1
		#init player
		#init monster
		monster = Monster(player.Level / 2 + 1)

		monster.monster_stats_log()
		f.fight(player, monster)
		if player.Level == 99:
			condition = False
			player.inventory_log()
		# else:
		# 	print('Continue?')
		# 	# print('I for inventory')
		# 	# print('F for fight')
		# 	if keyboard.read_key().lower() == 'y': 
		# 		condition = True
		# 	elif keyboard.read_key().lower() == 'n':
		# 	 	condition = False
    
if __name__ == "__main__":
	main()