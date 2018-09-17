import pygame
import time
import random
#Windows: søk CMD: Skriv 'D:': Skriv 'cd Andreas\Kode dingse boms': så kjør programmet ved å skrive 'Halla.py'


pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)



bg_width = 9992
bg_height = 600

ship_width = 52
ship_height = 52


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Escape')
clock = pygame.time.Clock()

shipImg = pygame.image.load('Spaceship.png')

bg = pygame.image.load('Background1.png')



def background(xa, ya):
	gameDisplay.blit(bg, (xa,ya))



def live_score(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Score: " + str(count), True, black)
	gameDisplay.blit(text, (0, 0))


def obstacles(ox, oy, ow, oh, color):
	pygame.draw.rect(gameDisplay, color, [ox, oy, ow, oh])


def quitgame():
	pygame.quit()
	quit()	


def ship(x,y):
	gameDisplay.blit(shipImg, (x,y))
#00 er øverst i venstre hjørne

def text_objects(text, font):
	TextSurface = font.render(text, True, black)
	return TextSurface, TextSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 50)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

def destroy():
	message_display('Your ship was Destroyed!')
	time.sleep(2)
	game_loop()



def game_loop():

	xa = 0
	ya = 0



	x = (display_width * 0.1)
	y = (display_height * 0.45)

	x_change = 0
	y_change = 0

	obstacle_startx = 850
	obstacle_starty = random.randrange(0, display_width)
	obstacle_speed = 4
	obstacle_width = 100
	obstacle_height = 100
	score = 0

	score = 0

	gameExit = False

 
	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					y_change = -5
				elif event.key == pygame.K_DOWN:
					y_change = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0


		y += y_change

		background(xa, ya)
		xa -= 1
		#obstacles(ox, oy, ow, oh, color):
		obstacles(obstacle_startx, obstacle_starty, obstacle_width, obstacle_height, white)
		obstacle_startx -= obstacle_speed

		live_score(score)

		ship(x,y)

		if y > display_height - ship_width or y < 0:
			y_change = 0

		if obstacle_startx < 0 - obstacle_width:
			obstacle_startx = display_width + obstacle_width
			obstacle_starty = random.randrange(0, display_height - obstacle_height)
			
			tall = random.randrange(0,1200)

			if tall < 200:
				obstacle_speed = 4
			elif tall >= 300 and tall < 400:
				obstacle_speed = 5
			elif tall >= 400 and tall < 500:
				obstacle_speed = 6
			elif tall >= 500 and tall < 600:
				obstacle_speed = 7
			elif tall >= 600 and tall < 700:
				obstacle_speed = 8
			elif tall >= 700 and tall < 800:
				obstacle_speed = 9
			elif tall >= 800 and tall < 900:
				obstacle_speed = 10
			elif tall >= 1000 and tall < 1100:
				obstacle_speed = 11
			elif tall >= 1100 and tall < 1200:
				obstacle_speed = 12
			score += 1

		




		if x + ship_width >= obstacle_startx and y + ship_height > obstacle_starty and y < obstacle_starty + obstacle_height and x < obstacle_startx + obstacle_width:
			destroy()


		


		pygame.display.update()
		clock.tick(60)





game_loop()
quitgame()

# This is copyright material by An2Ba prouductions. It belongs fully and only by An2Ba and them alone. Copying and/or duplicateing "Space Escape" violates this policy.

