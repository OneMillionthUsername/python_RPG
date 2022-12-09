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
player.player_add_item(sword)
shield = i.Item("Shield", 5, 1,1,0,50,0,1,2)
player.player_add_item(shield)

#current_item = player.player_get_item(shield)
#current_item.item_print()
player.player_inventory_print()


