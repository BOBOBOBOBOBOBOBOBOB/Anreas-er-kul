import pygame
import time
import random
from button import *
#Windows: søk CMD: Skriv 'D:': Skriv 'cd Andreas\Kode dingse boms': så kjør programmet ved å skrive 'Halla.py'

textbox = pygame.image.load("Textbox.png")
textbox1 = pygame.image.load("Textbox1.png")
textbox2 = pygame.image.load("Textbox2.png")


pygame.init()
class level:
	def __init__(self,x,y,music,speed,endx,num,textbox):
		self.x = x
		self.y = y
		self.music = music
		self.speed = speed
		self.endx = endx
		self.num = num
		self.textbox = textbox

levels = [level(0,0,"start_music.wav",10,-2400,0,textbox),
level(-2400,0,"asteroidbelt.wav",0.765,-5250 + 800,1,textbox1),
level(-5250 + 800, 0,"gas_giants.wav",1.3,-9992 + 800,2,textbox2)]

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)



bg = pygame.image.load('Background1.png')
bg1 = pygame.image.load('Background2.png')
menu_background = pygame.image.load("Space 1.png")
bg_width = 9992
bg_height = 600
bg1_width = 9992
bg1_height = 600

shipImg = pygame.image.load('Spaceship.png')
shipImg2 = pygame.image.load('S1.png')
shipImg3 = pygame.image.load('S2.png')
ship_width = 52
ship_height = 52


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Escape')
clock = pygame.time.Clock()

ragequit = pygame.image.load('ragequit.png')


#button = pygame.Rect((display_width * 0.4), (display_height * 0.5), 120, 65)
button = button(335,450,w=150,h=50,color=red)


asteroid1 = pygame.image.load('Asteroid1.png')
asteroid2 = pygame.image.load('Asteroid2.png')
asteroids = (asteroid1, asteroid2)

current_asteroid = random.choice(asteroids)
current_asteroid1 = random.choice(asteroids)

number = random.randrange(0, 1000)

smx = 335
smy = 470

def background(xa, ya):
	gameDisplay.blit(bg, (xa,ya))

def live_score(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Score: " + str(count), True, white)
	gameDisplay.blit(text, (0, 0))

def obstacles(ox, oy, ow, oh):
	global current_asteroid1
	gameDisplay.blit(current_asteroid1, (ox, oy, ow, oh))

def quitgame():
	pygame.quit()
	quit()	


def ship(x,y):
	gameDisplay.blit(shipImg, (x,y))
#00 er øverst i venstre hjørne

def text_objects(text, font):
	TextSurface = font.render(text, True, white)
	return TextSurface, TextSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 50)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()




def destroy():
	pygame.mixer.music.stop()
	message_display('Your ship was Destroyed!')	
	gameDisplay.blit(ragequit,(335, 470))
	time.sleep(0.15)
	gameDisplay.blit(ragequit,(335, 470))

	time.sleep(2)
	menu_screen()
def getLevelNumber():
	with open("levelnumber.txt","r") as f:
		return int(f.read())
def setLevelNumber(num):
	with open("levelnumber.txt","w") as f:
		f.write(str(num))

def menu_screen(levelup = False):
	pygame.mixer.init()
	pygame.mixer.music.load("menu_music.wav")
	pygame.mixer.music.play(loops=-1, start=0.0)
	pygame.mixer.music.set_volume(0.5)
	if (levelup):
		setLevelNumber(getLevelNumber()+1)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1 and button.collidepoint(event.pos[0],event.pos[1]):
					game_loop(levels[getLevelNumber()])

		gameDisplay.blit(menu_background,(0,0))
		pygame.draw.rect(gameDisplay,button.color,button.rect)
		pygame.display.update()
		clock.tick(30)

def level_complete(level):
	pygame.mixer.music.stop()
	setLevelNumber(level.num + 1)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1 and button.collidepoint(event.pos[0],event.pos[1]):
					game_loop(levels[getLevelNumber()])

		
		background(level.endx,0)
		gameDisplay.blit(level.textbox,(100,60))
		pygame.draw.rect(gameDisplay,button.color,button.rect)
		pygame.display.update()
		clock.tick(30)


def game_loop(level):
	global current_asteroid, current_asteroid1
	xa = level.x
	ya = level.y

	angle = 0
	angle_add = 0


	x = (display_width * 0.1)
	y = (display_height * 0.45)


	tx = 100
	ty = 30

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

	pygame.mixer.music.load(level.music)
	pygame.mixer.music.play(loops=-1, start=0.0)
	pygame.mixer.music.set_volume(0.5)

 
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
		xa -= level.speed

		angle += angle_add
		if angle >= 360:
			angle = 0

		#pygame.draw.rect(gameDisplay, color, [ox, oy, ow, oh])
		obstacles(obstacle_startx, obstacle_starty, obstacle_width, obstacle_height)
		obstacle_startx -= obstacle_speed


		live_score(score)

		current_asteroid1 = pygame.transform.rotate(current_asteroid, angle)

		ship(x,y)

		if y > display_height - ship_width or y < 0:
			y_change = 0

		if obstacle_startx < 0 - obstacle_width:
			current_asteroid = random.choice(asteroids)
			angle_add = random.randrange(-3, 3)

			obstacle_width = current_asteroid.get_size()[0]
			obstacle_height = current_asteroid.get_size()[1]


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

			if obstacle_speed == 4:
				angle_add = random.randrange(-1, 1)

		if (xa <= level.endx):
			level_complete(level)
		if x + ship_width >= obstacle_startx and y + ship_height > obstacle_starty and y < obstacle_starty + obstacle_height and x < obstacle_startx + obstacle_width:
			destroy()
			restart()
		


		pygame.display.update()
		clock.tick(60)




menu_screen()
quitgame()

# This is copyright material by An2Ba prouductions. It belongs fully and only by An2Ba and them alone. Copying and/or duplicateing "Space Escape" violates this policy.

