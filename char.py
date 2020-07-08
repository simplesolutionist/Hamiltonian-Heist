import pygame
from pygame.locals import*
import sys
import curses
SCREENWIDTH = 1000
SCREENHEIGHT = 800
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
aqua = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init() # initialize for sound
# initialize background music and background image
pygame.mixer.music.load('Wizard_City.ogg')
pygame.mixer.music.play()
player = pygame.image.load('slide2.png').convert()
player = pygame.transform.scale(player, (800, 800))

def character():
	pygame.init()
	pygame.mixer.init() # initialize for sound

	pygame.mixer.music.load('Wizard_City.ogg')
	pygame.mixer.music.play()
	while True:
		SCREEN.blit(player,(0,0))
		x, y = pygame.mouse.get_pos()
		# returns a single event from the queue
		event = pygame.event.wait()
                
		# if the 'close' buttom of the window is pressed
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		# create a highlight border to allow user to know to choose warrior
		if(x>480 and y>550 and x<680 and y<650):
			X_for_h=250 #height of side borders
			Y_for_h=628 #left and right
			X_for_w=505 #up and down 
			Y_for_w=635 #height of up and down lines
			for height in range(0,9):
				Y_for_h -= 10
			for width in range(0,19):
				X_for_w += 10
			for height in range(0,9):
				Y_for_h += 10
			for width in range(0,19):
				X_for_w -= 10
			if(event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
				print('warrior')
                # create a highlight border to allow user to know to choose wizard
		elif (x>200 and y>530 and x<400 and y<630):
			X_for_h=700
			Y_for_h=633 #left and right height
			X_for_w=230 # up and down
			Y_for_w=635 # moves horizontal line up and down
			for height in range(0,10):
				Y_for_h -= 10
			for width in range(0,19):
				X_for_w += 10
			for height in range(0,10):
				Y_for_h += 10
			for width in range(0,19):
				X_for_w -= 10
			if(event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
				print('wizard')
		# create a highlight border to allow user to know to choose alien
		elif (x > 45 and y > 530 and x < 155 and y < 630):
			X_for_h=700
			Y_for_h=633 #left and right height
			X_for_w=40 # up and down
			Y_for_w=635 # moves horizontal line up and down
			for height in range(0,10):
				Y_for_h -= 10
			for width in range(0,13):
				X_for_w += 10
			for height in range(0,10):
				Y_for_h += 10
			for width in range(0,13):
				X_for_w -= 10
			if(event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
				print('alien')

		pygame.display.update()



if __name__ == "__main__":
	pygame.init() # Initialize all pygame's modules
	pygame.display.set_caption('Hamiltonian Heist')
	player = pygame.image.load('slide2.png').convert()
	player = pygame.transform.scale(player, (1000, 790))
	character()

