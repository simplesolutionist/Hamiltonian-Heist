import pygame
from pygame.locals import*
import sys
import curses
from menu4 import menu4
SCREENWIDTH = 1000
SCREENHEIGHT = 1000
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
aqua = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init() # initialize for sound
# initialize background music
pygame.mixer.music.load('Journeys_End.ogg')
pygame.mixer.music.play()


def Ending():
	while True:
		SCREEN.blit(ending,(0,0))
		x, y = pygame.mouse.get_pos()
		# returns a single event from the queue
		event = pygame.event.wait()

		# if the 'close' buttom of the window is pressed
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		# create highlight border for option to play the game again
		if(x>475 and y>300 and x<635 and y<360):

			X_for_h=250 # height of side borders
			Y_for_h=352 #left and right
			X_for_w=487 #up and down 
			Y_for_w=355 #height for bottom line
			for height in range(0,5):
				pygame.draw.circle(SCREEN, aqua, (487,Y_for_h), 5)
				Y_for_h -= 10
			for width in range(0,15):
				pygame.draw.circle(SCREEN, aqua, (X_for_w,Y_for_w), 5)
				X_for_w += 10
			for height in range(0,5):
				Y_for_h += 10
				pygame.draw.circle(SCREEN, aqua, (627,Y_for_h), 5)
			for width in range(0,15):
				X_for_w -= 10
				pygame.draw.circle(SCREEN, aqua, (X_for_w,310), 5)
			if(event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
				menu4()
                # create highlight border in order to exit the game
		elif (x>460 and y>415 and x<655 and y<475):
			X_for_h=400
			Y_for_h=470 #left and right height
			X_for_w=488 # up and down
			Y_for_w=470 # moves horizontal line up and down
			for height in range(0,6):
				pygame.draw.circle(SCREEN, aqua, (480,Y_for_h), 5)
				Y_for_h -= 10
			for width in range(0,15):
				pygame.draw.circle(SCREEN, aqua, (X_for_w,Y_for_w), 5)
				X_for_w += 10
			for height in range(0,6):
				Y_for_h += 10
				pygame.draw.circle(SCREEN, aqua, (630,Y_for_h), 5)
			for width in range(0,15):
				X_for_w -= 10
				pygame.draw.circle(SCREEN, aqua, (X_for_w,420), 5)
			if(event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
				pygame.quit()
				sys.exit()
            
		pygame.display.update()

if __name__ == "__main__":
	pygame.init() # Initialize all pygame's modules
	pygame.display.set_caption('Hamiltonian Heist')
	ending = pygame.image.load('ending.png').convert()
	ending = pygame.transform.scale(ending, (1000, 900))

	Ending()
