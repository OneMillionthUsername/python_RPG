import player as p
import monster as m
import fight as f

def main():

	#main
	count = 0
	condition = True
	while condition:
		#init player
		player = p.player("Dean")
		#init monster
		monster = m.Monster("Bat", "flying", 4)
		condition = f.fight(player, monster)
		count += 1
	print('Number of fights for legendary item:', count)

if __name__ == "__main__":
	main()