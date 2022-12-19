import random as r
import time

def fight(player, monster) -> bool:
	player.health_reset()
	monster.health_reset()
	items_pool = monster.Items.copy()
#set item to be dropped
	if len(items_pool) > 0:
		item_drop = items_pool[r.randint(0, len(items_pool) - 1)]
	else:
		item_drop = None
	
	while player.Health > 0 and monster.Health > 0:
		hit = ((player.Strength + r.randint(1,5))*3)
		monster.Health -= hit
		# print(f'{player.Name} hits {monster.Name} for {hit} damage.')
		hit = ((monster.Strength + r.randint(1,5))*3)%10
		player.Health -= hit
		# print(f'{monster.Name} hits {player.Name} for {hit} damage.')
		# print(f'{player.Name} HP: {player.Health}')
		# print(f'{monster.Name} HP: {monster.Health}')
		# time.sleep(1)

	if player.Health <= 0:
		print('Game over!')
		return False
	else:
		#print(f'{monster.Name} falls to the ground and gives {monster.Expirience_give} expirience.')
		player.Expirience += monster.Expirience_give
		if player.Expirience >= player.Exp_needed_for_level_up:
			player.player_level_up()
		else:
			pass
			#print(f'{player.Name} gains {monster.Expirience_give} expirience.\n{player.Exp_needed_for_level_up - player.Expirience} exp for level up.')
		player.Money += monster.Money
	
		if item_drop != None and item_drop.Drop_chance >= r.randint(1,100):
			player.Items.append(item_drop)
			#print(f'You found {monster.Money} gold and a {item_drop.Rarity} {item_drop.Name}.')
			#item_drop.item_print()
			player.save_player()
			if item_drop.Rarity == 'legendary':
				return False
			else:
				return True
		else:
			#print(f'You found {monster.Money} gold.')
			player.save_player()
			return True