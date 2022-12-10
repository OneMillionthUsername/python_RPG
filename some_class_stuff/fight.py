import player as p
import monster as m
import random as rnd
import time

def fight(player, monster):
	player.health_reset()
	monster.health_reset()
	while player.Health > 0 and monster.Health > 0:
		hit = ((player.Strength + rnd.randint(1,5))*3)%40
		monster.Health -= hit
		print(f'{player.Name} hits {monster.Name} for {hit} damage.')
		hit = ((monster.Strength + rnd.randint(1,5))*3)%10
		player.Health -= hit
		print(f'{monster.Name} hits {player.Name} for {hit} damage.')
		print(f'{player.Name} HP: {player.Health}')
		print(f'{monster.Name} HP: {monster.Health}')
		time.sleep(1)

	if player.Health <= 0:
		print('Game over!')
		return False
	else:
		print(f'{monster.Name} falls to the ground.')
		player.Expirience += monster.Expirience_give
		print(f'{player.Name} gains {monster.Expirience_give} expirience.')
		player.Money += monster.Money
		items_pool = monster.Items.copy()
		items_drop = items_pool[rnd.randint(0, len(items_pool) - 1)]
		if items_drop.Drop_chance == True:
			player.Items.append(items_drop)
			print(f'You found {monster.Money} gold and a {items_drop.Rarity} {items_drop.Name}.')
			print(items_drop.item_print())
			return False
		else:
			print(f'You found {monster.Money} gold.')
			return True