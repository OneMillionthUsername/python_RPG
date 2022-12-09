import random as r
import item as i

#level 1-5 gear
weapon_names_warrior = ["Sword", "Shield", "Axe"]
weapon_names_magician = ["Staff", "Wand", "Papyrus"]
weapon_names_bowmaster = ["Bow", "Crossbow", "Slingshot"]
pool = []

def item_pool_init():
	for j in range(10):
		item = i.Item(weapon_names_warrior[r.randint(0,2)], r.randint(5,15), r.randint(1,5), r.randint(1,4), r.randint(1,2), r.randint(1,10) * 10, 0, r.randint(1,5), r.randint(0,1))
		pool.append(item)
		j += 1

#sword = ("Sword", 10, 2,3,0,15,0,1,0)
#shield = ("Shield", 5, 1,1,0,50,0,1,2)
#helmet = ("Helmet", 4, 1, 3, 1, 5, 5, 1, 0)
#ool = [sword, shield, helmet]