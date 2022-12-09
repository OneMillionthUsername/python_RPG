import player as p
import monster as m
import fight as f
import item as i
import random as rnd
import item_pool as ip

#init player
player = p.player("Dean")
#init items
ip.item_pool_init()
items = ip.pool
monster = m.Monster("Bat", "flying", 4)
monster.items = monster.set_loot_bag(items)

f.fight(player, monster)

