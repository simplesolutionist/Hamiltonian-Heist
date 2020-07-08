import pygame
from pygame.locals import*
import sys
import curses
from menu3 import menu3

SCREENWIDTH = 800
SCREENHEIGHT = 800
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

# upload background image
h = pygame.image.load('help.png').convert()
h = pygame.transform.scale(h, (800, 800))

pygame.init()
pygame.mixer.init() # initialize for sound
clock = pygame.time.Clock()
aqua = (0, 255, 255)
pygame.mixer.music.load('Kings_of_Yore.ogg')
pygame.mixer.music.play()
clock = pygame.time.Clock()

def help3():

	while True:
		SCREEN.blit(h,(0,0))
		x, y = pygame.mouse.get_pos()
		# returns a single event from the queue
		event = pygame.event.wait()

		# if the 'close' buttom of the window is pressed
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		# create option to go back to main menu
		if(x>40 and y>30 and x<220 and y<50):

			X_for_h=100 #heihgt for up and down lines
			Y_for_h=100 #left and right
			X_for_w=50 #up and down 
			Y_for_w=55 #height for side borders
			for height in range(0,9):
				Y_for_h -= 10
			for width in range(0,19):
				X_for_w += 10
			for height in range(0,9):
				Y_for_h += 10
			for width in range(0,19):
				X_for_w -= 10
			if(event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
				print('play')
				menu3()
                # for Help OPTION
            
		pygame.display.update()

if __name__ == "__main__":
	pygame.init() # Initialize all pygame's modules
	pygame.display.set_caption('Hamiltonian Heist')
	h = pygame.image.load('help.png').convert()
	h = pygame.transform.scale(h, (800, 800))
	help3()

	
	
