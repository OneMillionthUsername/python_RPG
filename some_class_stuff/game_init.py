import player as p
import playerClass as pc
import monster as m
import fight
import item as i
import random as rnd
import item_pool as ip

#init player
player = p.player()
#init items
ip.item_pool_init()
items = ip.pool
monster = m.Monster(4)
monster.items = monster.monster_set_loot_bag(items)



