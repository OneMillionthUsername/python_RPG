import player as p
import monster as m
import random as rnd

def fight(player, monster):
	while player.Health > 0 & monster.Health > 0:
		hit = ((player.Strength + rnd.randint(1,5))*3)%20
		monster.Health -= hit
		print(f'{player.Name} hits {monster.Name} for {hit} damage.')
		player.Health -= ((monster.Strength + rnd.randint(1,5))*3)%15
		print(f'{monster.Name} hits {player.Name} for {hit} damage.')

	if player.Health <= 0:
		print('Game over!')
	else:
		player.Expirience += monster.Expirience_give
		print(f'{player.Name} gains {monster.Expirience_give} expirience.')
		player.Money += monster.Money
		items_pool = monster.Items.copy()
		items_drop = items_pool[rnd.randint(0, len(items_pool))]
		player.Items.append(items_drop)
		print(f'You found {monster.Money} gold and a {items_drop.Rarity} {items_drop.Name}.')