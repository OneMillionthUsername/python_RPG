import player as p
import monster as m
import fight as f

def main():
	#init player
	player = p.player("Dean")
	#init monster
	monster = m.Monster("Bat", "flying", 4)
	#monster.items = monster.set_loot_bag(items)
	#main
	condition = True
	while condition:
		condition = f.fight(player, monster)

if __name__ == "__main__":
	main()