import pygame
pygame.init()

import random

WIDTH = 500
HEIGHT = 500
BLOCK_SIZE = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
			return generate_des(num-1)
		else:
			return generate_des(num)

run = True

def detect_move():
	global player, move_ticker, block_push, run
	keys=pygame.key.get_pressed()
	if move_ticker == 0:
		if player[0] > 0:
			if keys[pygame.K_LEFT]:
				move_ticker = 10
				if [player[0]-1, player[1]] in block_push and [player[0]-2, player[1]] not in block_push:
					if player[0]-2 > 0:
						block_push[block_push.index([player[0]-1, player[1]])][0] -= 1
						player[0] -= 1
				elif [player[0]-1, player[1]] not in block_push:
				    player[0] -= 1
		
		if player[0] < WIDTH // BLOCK_SIZE -1:
			if keys[pygame.K_RIGHT]:  
				move_ticker = 10
				if [player[0]+1, player[1]] in block_push and [player[0]+2, player[1]] not in block_push:
					if player[0]+2 < WIDTH // BLOCK_SIZE -1:
						block_push[block_push.index([player[0]+1, player[1]])][0] += 1
						player[0] += 1
				elif [player[0]+1, player[1]] not in block_push:
				    player[0] += 1

		if player[1] > 0:
			if keys[pygame.K_UP]:
				move_ticker = 10
				if [player[0], player[1]-1] in block_push and [player[0], player[1]-2] not in block_push:
					if player[1]-2 > 0:
						block_push[block_push.index([player[0], player[1]-1])][1] -= 1
						player[1] -= 1
				elif [player[0], player[1]-1] not in block_push:
				    player[1] -= 1
		
		if player[1] < HEIGHT // BLOCK_SIZE -1:
			if keys[pygame.K_DOWN]:
				move_ticker = 10
				if [player[0], player[1]+1] in block_push and [player[0], player[1]+2] not in block_push:
					if player[1]+2 < HEIGHT // BLOCK_SIZE -1:
						block_push[block_push.index([player[0], player[1]+1])][1] += 1
						player[1] += 1
				elif [player[0], player[1]+1] not in block_push:
				    player[1] += 1

	if sorted(block_push) == sorted(destination):
		run = False

def update():
	screen.fill((0, 0, 0))
	for i in destination:
		pygame.draw.rect(screen, (255, 0, 0), (i[0]*BLOCK_SIZE, i[1]*BLOCK_SIZE, BLOCK_SIZE-1, BLOCK_SIZE-1))
	for i in block_push:
		if i not in destination:
			pygame.draw.rect(screen, (0, 255, 255), (i[0]*BLOCK_SIZE, i[1]*BLOCK_SIZE, BLOCK_SIZE-1, BLOCK_SIZE-1))
		else:
			pygame.draw.rect(screen, (255, 0, 255), (i[0]*BLOCK_SIZE, i[1]*BLOCK_SIZE, BLOCK_SIZE-1, BLOCK_SIZE-1))
	pygame.draw.rect(screen, (255, 255, 0), (player[0]*BLOCK_SIZE, player[1]*BLOCK_SIZE, BLOCK_SIZE-1, BLOCK_SIZE-1))
	
clock = pygame.time.Clock()
move_ticker = 10

generate(5)
generate_des(5)

while run:
	for eve in pygame.event.get():
		if eve.type==pygame.QUIT:
			run = False
	detect_move()
	update()
	if move_ticker > 0:
		move_ticker -= 1
	pygame.display.update()
	clock.tick(60)
