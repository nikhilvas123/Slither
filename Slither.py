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

icon = pygame.image.load("apple.png")
pygame.display.set_icon(icon)

img = pygame.image.load('snakeHead.png')
apple = pygame.image.load('apple.png')

AppleThickness = 30
block_size = 20
FPS = 15

direcion = "right"

smallfont = pygame.font.SysFont("brookeshappell8",25)
mediumfont = pygame.font.SysFont("brookeshappell8",50)
largefont = pygame.font.SysFont("brookeshappell8",80)

clock = pygame.time.Clock()

def randAppleGen():
	randAppleX = round(random.randrange(0,display_width-AppleThickness))#/block_size)*block_size
	randAppleY = round(random.randrange(0,display_height-AppleThickness))#/block_size)*block_size
	return randAppleX,randAppleY

def game_intro():

	intro = True

	while intro:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					intro = False

				if event.key == pygame.K_q:
					pygame.quit()
					quit()

		gameDisplay.fill(white)
		message_to_screen("Welcome to Slither",green,-100,"large")
		message_to_screen("The objective of the game is to eat red apples",black,-70)
		message_to_screen("The more apples you eat, the longer you get",black,-50)
		message_to_screen("If you run into yourself, or the edges, you die!",black,-30)
		message_to_screen("Press C to start or Q to quit",black,y_disp=-10)

		pygame.display.update()

		clock.tick(FPS)

def snake(snakeList):

	if direcion=="right":
		head = pygame.transform.rotate(img,270)

	if direcion=="left":
		head = pygame.transform.rotate(img,90)

	if direcion=="up":
		head = img;

	if direcion=="down":
		head = pygame.transform.rotate(img,180)

	gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))

	for XnY in snakeList[:-1]:
		pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
	if size=="small":
		textSurface = smallfont.render(text,True,color)
	elif size=="medium":
		textSurface = mediumfont.render(text,True,color)
	elif size=="large":
		textSurface = largefont.render(text,True,color)

	return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,y_disp=0,size="small"):
	textSurf, textRect = text_objects(msg,color,size)
	textRect.center = (display_width/2), (display_height/2)+y_disp
	gameDisplay.blit(textSurf,textRect)

def gameLoop():
	global direcion
	direcion = "right"
	gameOver = False
	gameExit = False

	lead_x = display_width/2
	lead_y = display_height/2

	snakeList = []
	snakeLength = 1

	lead_x_change = 10
	lead_y_change = 0

	randAppleX,randAppleY = randAppleGen()

	while not gameExit:
		while gameOver:
			gameDisplay.fill(white)
			message_to_screen("Game Over",red,y_disp=-50,size="large")
			message_to_screen("Press C to restart or Q to quit",black,y_disp=50,size="medium")
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					gameOver = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False

					elif event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if len(snakeList) == 1 or lead_x_change != block_size: 
						lead_x_change = -block_size
						lead_y_change = 0
						direcion = "left"

				elif event.key == pygame.K_RIGHT:
					if len(snakeList) == 1 or lead_x_change != -block_size:
						lead_x_change = block_size
						lead_y_change = 0
						direcion = "right"

				elif event.key == pygame.K_UP:
					if len(snakeList) == 1 or lead_y_change != block_size:
						lead_y_change = -block_size
						lead_x_change = 0
						direcion = "up"

				elif event.key == pygame.K_DOWN:
					if len(snakeList) == 1 or lead_y_change != -block_size:
						lead_y_change = block_size
						lead_x_change = 0
						direcion = "down"

		# To Stop Moving the rectangle
		#	if event.type == pygame.KEYUP:
		#		if event.key == pygame.K_LEFT or pygame.K_RIGHT:
		#			lead_x_change = 0
		if lead_x >=display_width or lead_x <0 or lead_y >=display_height or lead_y <0:
			gameOver = True

		lead_x+= lead_x_change
		lead_y+= lead_y_change

		gameDisplay.fill(white)
#		pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])
		gameDisplay.blit(apple,(randAppleX,randAppleY))

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
				randAppleX,randAppleY = randAppleGen()
				snakeLength+= 1

		clock.tick(FPS)

	pygame.quit()
	quit()

game_intro()
gameLoop()