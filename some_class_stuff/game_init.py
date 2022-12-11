from player import Player
from monster import Monster
import fight as f

def main():

	#main
	count = 0
	condition = True
	player = Player("Dean")
	while condition:
		#init player
		#init monster
		monster = Monster(4)
		condition = f.fight(player, monster)
		count += 1
	print('Number of fights for this item rarity:', count)

if __name__ == "__main__":
	main()