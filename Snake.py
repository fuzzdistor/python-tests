"""
11 AM Sábado 14/05/16

**Python challenge!**

Me desafío a hacer un juego de snake
para obtener y afianzar conocimientos
del lenguaje de programación Python.

Usaré Python 2.7 porque hasta donde
entiendo la librería PyGame no soporta
Python 3.3.

Ya es la hora! Ready?

"""
from collections import deque
import random
import pygame


#Constantes varias

#RESOLUCION BAJA
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 580

RECT_SIDE = 15
SPACE = 4

TILE = RECT_SIDE + SPACE

WHITE_MARGIN = 8
INFO_BOX = 82

#RESOLUCION ALTA
"""
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

RECT_SIDE = 25
SPACE = 5

TILE = RECT_SIDE + SPACE

WHITE_MARGIN = 12
INFO_BOX = 82
"""

#COLORES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

GAME_TEXT = ("Vidas",
			 "Puntuacion")

#Funciones para construcción "sencilla"
def makeRect(x, y, width=RECT_SIDE, height=RECT_SIDE):
	return pygame.Rect(x, y, width, height)

#Clase que contiene un deque con los rect que componen la serpiente
class Snake():
	segments = deque()
	prev_direction = "right"
	segment_num = 0

	def add_segment(self, x, y):
		self.segments.append(makeRect(x, y))

	def draw(self, window):
		for rectangle in self.segments:
			window.fill(CYAN, rectangle)
		window.fill(BLUE, self.segments[self.segment_num - 1])


	def move(self, direction):
		#self: Snake 
		#direction: String ("left, right, up, down")
		mem_segment = self.segments[0]

		if (direction == "left" and self.prev_direction != "right"):
			self.segments.appendleft(makeRect(self.segments[0].x - TILE, 
											  self.segments[0].y))

		if (direction == "right" and self.prev_direction != "left"):
			self.segments.appendleft(makeRect(self.segments[0].x + TILE, 
											  self.segments[0].y))

		if (direction == "up" and self.prev_direction != "down"):
			self.segments.appendleft(makeRect(self.segments[0].x, 
											  self.segments[0].y - TILE))

		if (direction == "down" and self.prev_direction != "up"):
			self.segments.appendleft(makeRect(self.segments[0].x, 
											  self.segments[0].y + TILE))

		if (mem_segment != self.segments[0]):
			self.prev_direction = direction
			self.segments.pop()
			return True
		else: 
			return False

	def start(self, BackGround, desired_segments):
		self.segment_num = desired_segments
		playground = BackGround.play_bg
		margins = BackGround.play_margins
	
		x = playground.x + margins['L'] + 4*TILE
		y = playground.y + margins['T'] + 4*TILE
	
		self.segments.clear()
		
		for count in range(0, desired_segments):
			self.add_segment(x, y)

def gridPlacement(Playground):

	x_res = Playground.width % TILE
	marginL = (x_res + SPACE) / 2
	y_res = Playground.height % TILE
	marginT = (y_res + SPACE) / 2

	x_tiles = Playground.width / TILE
	y_tiles = Playground.height / TILE

	return {'L':marginL, 'T':marginT, 'x':x_tiles, 'y':y_tiles}

class BackGround():
	white_bg = makeRect(SPACE, SPACE, WINDOW_WIDTH - 2*SPACE, WINDOW_HEIGHT - 2*SPACE)
	play_bg = makeRect(SPACE + WHITE_MARGIN, 
					   SPACE + 2*WHITE_MARGIN + INFO_BOX,  
					   WINDOW_WIDTH - 2*SPACE - 2*WHITE_MARGIN, 
					   WINDOW_HEIGHT - 2*SPACE - 3*WHITE_MARGIN - INFO_BOX)
	play_margins = gridPlacement(play_bg)
	info_box = makeRect(SPACE + WHITE_MARGIN, 
						SPACE + WHITE_MARGIN, 
						WINDOW_WIDTH - 2*SPACE - 2*WHITE_MARGIN,
						INFO_BOX) 

	def draw(self, window):
		window.fill(WHITE, self.white_bg)
		window.fill(BLACK, self.play_bg)
		window.fill(BLACK, self.info_box)




class Limes():
	limes = deque()	
	def makeLime():
		return0


		
def limeSpawn(Snake, BackGround, window):
	x = BackGround.play_bg.x + BackGround.play_margins['L']
	if (Snake.segments[0].x > 400):
		x = random.randrange(BackGround.play_bg.x + BackGround.play_margins['L'], 
							 BackGround.play_bg.right - BackGround.play_margins['L'] + SPACE,
							 TILE)
	lime = makeRect(x, BackGround.play_bg.y + BackGround.play_margins['T'])
	window.fill(YELLOW, lime)

def checkColision():
	return 0

def checkOutbounds(Snake, BackGround):
	head_segment = Snake.segments[0]
	playground = BackGround.play_bg

	return (head_segment.right >= playground.right
			or head_segment.left < playground.left
			or head_segment.bottom >= playground.bottom
			or head_segment.top < playground.top)

def main():

	refresh_time = 150
	done = False
	direction = "right"
	
	#Creo un objeto "Ventana" y le pongo un título
	window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
	pygame.display.set_caption('Python Wars')

	random.seed()
	pygame.init()
	pygame.time.set_timer(pygame.USEREVENT + 1, refresh_time)
	
	
	snake_1 = Snake()
	
	
	#PARATESTEAR
	myfont = pygame.font.Font("PressStart2P.ttf", 20)

	# render text
	label = myfont.render("Vidas", 0, WHITE)
	


	#Creo un objeto Clock para manejar los FPS en el ciclo del juego
	myClock = pygame.time.Clock()

	background = BackGround()

	snake_1.start(background, 9)
	
	while not done:	
		#event recive una lista de eventos que evalúo para distintos fines
		for event in pygame.event.get():
			#Como salir del loop cuando se cierra la ventana
			if event.type == pygame.QUIT:
				done = True
	
			if event.type == pygame.KEYDOWN:
				#O cuando se presiona la tecla ESCAPE
				if event.key == pygame.K_ESCAPE:
					done = True
				if event.key == pygame.K_LEFT:
					direction = "left"
				if event.key == pygame.K_RIGHT:
					direction = "right"
				if event.key == pygame.K_UP:
					direction = "up"
				if event.key == pygame.K_DOWN:
					direction = "down"

				#PARATESTEO
				if event.key == pygame.K_KP_PLUS:
					WHITE_MARGIN += 1 
				if event.key == pygame.K_KP_MINUS:
					refresh_time -= 50
							
			if event.type == pygame.USEREVENT + 1:
				pygame.time.set_timer(pygame.USEREVENT + 1, refresh_time)
				if not snake_1.move(direction):
					snake_1.move(snake_1.prev_direction)
		
		
		if (checkOutbounds(snake_1, background)):
			snake_1.start(background, 9)
		#Lleno la pantalla de negro
		window.fill(BLACK)
	
		#Llamo la función que muestra los rect en snake_1
		background.draw(window)
		limeSpawn(snake_1, background, window)
		snake_1.draw(window)
		window.blit(label, (35, 25))
		pygame.display.flip()
		myClock.tick(60)
	
	pygame.quit()

main()