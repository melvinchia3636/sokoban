import time
import os
import keyboard
import random

WIDTH = 1000
HEIGHT = 1000
BLOCK_SIZE = 50

player = [random.randint(1, WIDTH // BLOCK_SIZE -2), random.randint(1, HEIGHT // BLOCK_SIZE -2)]
destination = []
block_push = []

def generate(num):
	if num > 0:
		x, y = random.randint(2, WIDTH // BLOCK_SIZE -3), random.randint(2, HEIGHT // BLOCK_SIZE -3)
		if [x, y] != player and [x, y] not in block_push:
			block_push.append([x, y])
			return generate(num-1)
		else:
			return generate(num)

def generate_des(num):
	if num > 0:
		x, y = random.randint(1, WIDTH // BLOCK_SIZE -2), random.randint(1, HEIGHT // BLOCK_SIZE -2)
		if [x, y] != player and [x, y] not in destination and [x, y] not in block_push:
			destination.append([x, y])
			print(destination)
			return generate_des(num-1)
		else:
			return generate_des(num)

run = True

def detect_move():
	global player, move_ticker, block_push, run
	if move_ticker == 0:
		if player[0] > 0:
			if keyboard.is_pressed('a'):
				move_ticker = 50000
				if [player[0]-1, player[1]] in block_push and [player[0]-2, player[1]] not in block_push:
					if player[0]-2 > 0:
						block_push[block_push.index([player[0]-1, player[1]])][0] -= 1
						player[0] -= 1
				elif [player[0]-1, player[1]] not in block_push:
				    player[0] -= 1
				update()
		
		if player[0] < WIDTH // BLOCK_SIZE -1:
			if keyboard.is_pressed('d'):  
				move_ticker = 50000
				if [player[0]+1, player[1]] in block_push and [player[0]+2, player[1]] not in block_push:
					if player[0]+2 < WIDTH // BLOCK_SIZE -1:
						block_push[block_push.index([player[0]+1, player[1]])][0] += 1
						player[0] += 1
				elif [player[0]+1, player[1]] not in block_push:
				    player[0] += 1
				update()

		if player[1] > 0:
			if keyboard.is_pressed('w'):
				move_ticker = 50000
				if [player[0], player[1]-1] in block_push and [player[0], player[1]-2] not in block_push:
					if player[1]-2 > 0:
						block_push[block_push.index([player[0], player[1]-1])][1] -= 1
						player[1] -= 1
				elif [player[0], player[1]-1] not in block_push:
				    player[1] -= 1
				update()
		
		if player[1] < HEIGHT // BLOCK_SIZE -1:
			if keyboard.is_pressed('s'):
				move_ticker = 50000
				if [player[0], player[1]+1] in block_push and [player[0], player[1]+2] not in block_push:
					if player[1]+2 < HEIGHT // BLOCK_SIZE -1:
						block_push[block_push.index([player[0], player[1]+1])][1] += 1
						player[1] += 1
				elif [player[0], player[1]+1] not in block_push:
				    player[1] += 1
				update()

	if sorted(block_push) == sorted(destination):
		run = False

def update():
	os.system('cls')
	for i in range(HEIGHT // BLOCK_SIZE):
		for j in range(WIDTH // BLOCK_SIZE):
			if [j, i] == player:
				print('\u25CF', end='')
			elif [j, i] in block_push:
				if [j, i] not in destination:
					print('\u2612', end='')
				else:
					print('\u25A0', end='')
			elif [j, i] in destination:
				print('\u2605', end='')
			else:
				print('\u25A1', end='')

		print()

move_ticker = 50000

generate(5)
generate_des(5)
update()

while run:
	detect_move()
	if move_ticker > 0:
		move_ticker -= 0.5
