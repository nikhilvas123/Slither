import pygame
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

block_size = 20
FPS = 15

font = pygame.font.SysFont(None,25)

def snake(snakeList):
	for XnY in snakeList:
		pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color):
	textSurface = font.render(text,True,color)
	return textSurface, textSurface.get_rect()

def message_to_screen(msg,color):
	textSurf, textRect = text_objects(msg,color)
#	screen_text = font.render(msg,True,color)
#	gameDisplay.blit(screen_text,[display_width/2,display_height/2])
	textRect.center = (display_width/2), (display_height/2)
	gameDisplay.blit(textSurf,textRect)

clock = pygame.time.Clock()

def gameLoop():
	gameOver = False
	gameExit = False

	lead_x = display_width/2
	lead_y = display_height/2

	snakeList = []
	snakeLength = 1

	AppleThickness = 30

	lead_x_change = 0
	lead_y_change = 0

	randAppleX = round(random.randrange(0,display_width-AppleThickness))#/block_size)*block_size
	randAppleY = round(random.randrange(0,display_height-AppleThickness))#/block_size)*block_size

	while not gameExit:
		while gameOver:
			gameDisplay.fill(white)
			message_to_screen("You Lose... Press Q to quit and R to restart",red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					gameOver = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False

					elif event.key == pygame.K_r:
						gameLoop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if len(snakeList) == 1 or lead_x_change != block_size: 
						lead_x_change = -block_size
						lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					if len(snakeList) == 1 or lead_x_change != -block_size:
						lead_x_change = block_size
						lead_y_change = 0

				elif event.key == pygame.K_UP:
					if len(snakeList) == 1 or lead_y_change != block_size:
						lead_y_change = -block_size
						lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					if len(snakeList) == 1 or lead_y_change != -block_size:
						lead_y_change = block_size
						lead_x_change = 0

		# To Stop Moving the rectangle
		#	if event.type == pygame.KEYUP:
		#		if event.key == pygame.K_LEFT or pygame.K_RIGHT:
		#			lead_x_change = 0
		if lead_x >=display_width or lead_x <0 or lead_y >=display_height or lead_y <0:
			gameOver = True

		lead_x+= lead_x_change
		lead_y+= lead_y_change

		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])

		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)

		if len(snakeList) > snakeLength:
			del snakeList[0]

		for eachSegment in snakeList[:-1]:
			if eachSegment == snakeHead:
				gameOver = True	

		snake(snakeList)
		pygame.display.update()

#		if lead_x >= randAppleX and lead_x <= randAppleX+AppleThickness:
#			if lead_y >= randAppleY and lead_y <= randAppleY+AppleThickness:
#				randAppleX = round(random.randrange(0,display_width-block_size))#/block_size)*block_size
#				randAppleY = round(random.randrange(0,display_height-block_size))#/block_size)*block_size
#				snakeLength+= 1
	
		if lead_x > randAppleX and lead_x <randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
			if lead_y > randAppleY and lead_y <randAppleY + AppleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
				randAppleX = round(random.randrange(0,display_width-AppleThickness))#/block_size)*block_size
				randAppleY = round(random.randrange(0,display_height-AppleThickness))#/block_size)*block_size
				snakeLength+= 1

		clock.tick(FPS)

	pygame.quit()
	quit()

gameLoop()