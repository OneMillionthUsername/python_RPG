import player as p
import monster as m
import fight as f

def main():

	#main
	count = 0
	condition = True
	player = p.player("Dean")
	while condition:
		#init player
		#init monster
		monster = m.Monster("Bat", "flying", 4)
		condition = f.fight(player, monster)
		count += 1
	print('Number of fights for this item rarity:', count)

if __name__ == "__main__":
	main()