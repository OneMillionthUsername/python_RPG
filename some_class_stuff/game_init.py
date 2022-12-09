import player as p
import playerClass as pc
import monster as m
import fight
import item as i
import random as rnd

#init player
player = p.player()
#init items
sword = i.Item("Sword", 10, 2,3,0,15,0,1,0)
shield = i.Item("Shield", 5, 1,1,0,50,0,1,2)
helmet = i.Item("Helmet", 4, 1, 3, 1, 5, 5, 1, 0)


player.player_add_item(sword)
player.player_add_item(shield)

m.Monster.monster_set_loot_bag(sword)
m.Monster.monster_set_loot_bag(shield)
m.Monster.monster_set_loot_bag(helmet)


