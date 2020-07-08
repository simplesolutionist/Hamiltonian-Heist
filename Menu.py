import pygame
from pygame.locals import*
import sys
from options import options
from help2 import help2
from help3 import help3
from options2 import options2
from char import character
aqua = (0, 255, 255)
clock = pygame.time.Clock()
# initialize pygame and create window
pygame.init()
pygame.mixer.init() # initialize for sound


# initialize pygame background music
pygame.mixer.music.load('Kings_of_Yore.ogg')
pygame.mixer.music.play()
def Menu():
	SCREENWIDTH = 1000
	SCREENHEIGHT = 1000
	SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
	menu = pygame.image.load('menu.png').convert()
	menu = pygame.transform.scale(menu, (1000, 800))
	while True:
		SCREEN.blit(menu,(0,0))
		x, y = pygame.mouse.get_pos()
		# returns a single event from the queue
		event = pygame.event.wait()

		# if the 'close' buttom of the window is pressed
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		# for PLAY OPTIONS
		if(x>460 and y>250 and x<655 and y<350):

			X_for_h=250 #height for up and down lines
			Y_for_h=340 #left and right
			X_for_w=470 #up and down 
			Y_for_w=350 #height for side bars
			for height in range(0,9):
				pygame.draw.circle(SCREEN, aqua, (470,Y_for_h), 5)
				Y_for_h -= 10
			for width in range(0,19):
				pygame.draw.circle(SCREEN, aqua, (X_for_w,Y_for_w), 5)
				X_for_w += 10
			for height in range(0,9):
				Y_for_h += 10
				pygame.draw.circle(SCREEN, aqua, (650,Y_for_h), 5)
			for width in range(0,19):
				X_for_w -= 10
				pygame.draw.circle(SCREEN, aqua, (X_for_w,250), 5)
			if(event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
				print('play')
				character()
                # for OPTIONS OPTION
		elif (x>460 and y>370 and x<655 and y<470):
			X_for_h=700
			Y_for_h=460 #left and right height
			X_for_w=470 # up and down
			Y_for_w=470 # moves horizontal line up and down
			for height in range(0,8):
				pygame.draw.circle(SCREEN, aqua, (470,Y_for_h), 5)
				Y_for_h -= 10
			for width in range(0,19):
				pygame.draw.circle(SCREEN, aqua, (X_for_w,Y_for_w), 5)
				X_for_w += 10
			for height in range(0,8):
				Y_for_h += 10
				pygame.draw.circle(SCREEN, aqua, (650,Y_for_h), 5)
			for width in range(0,19):
				X_for_w -= 10
				pygame.draw.circle(SCREEN, aqua, (X_for_w,380), 5)
			if(event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
				print('options')
				options()
            
		     # for HELP OPTION 
		elif (x>460 and y>500 and x<655 and y<600):
			X_for_h=200
			Y_for_h=590 #left and right height
			X_for_w=470 # up and down
			Y_for_w=600 # moves horizontal line up and down
			for height in range(0,8):
				pygame.draw.circle(SCREEN, aqua, (470,Y_for_h), 5)
				Y_for_h -= 10
			for width in range(0,19):
				pygame.draw.circle(SCREEN, aqua, (X_for_w,Y_for_w), 5)
				X_for_w += 10
			for height in range(0,8):
				Y_for_h += 10
				pygame.draw.circle(SCREEN, aqua, (650,Y_for_h), 5)
			for width in range(0,19):
				X_for_w -= 10
				pygame.draw.circle(SCREEN, aqua, (X_for_w,510), 5)
			if(event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
				print('Help')
				help2()
		# for EXIT OPTION
		elif (x>460 and y>651 and x<655 and y<750):
			X_for_h=700
			Y_for_h=740
			X_for_w=475
			Y_for_w=750
			for height in range(0,8):
				pygame.draw.circle(SCREEN, aqua, (470,Y_for_h), 5)
				Y_for_h -= 10
			for width in range(0,18):
				pygame.draw.circle(SCREEN, aqua, (X_for_w,Y_for_w), 5)
				X_for_w += 10
			for height in range(0,8):
				Y_for_h += 10
				pygame.draw.circle(SCREEN, aqua, (650,Y_for_h), 5)
			for width in range(0,18):
				X_for_w -= 10
				pygame.draw.circle(SCREEN, aqua, (X_for_w,660), 5)
			if(event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
				pygame.quit()
				sys.exit()

		pygame.display.update()
		pygame.display.flip()
		clock.tick(60)

#def switch():
#	SCREENWIDTH = 800
#	SCREENHEIGHT = 800
#	SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
#	char = pygame.image.load('options2.png')
#	SCREEN.blit(char, (0,0))
#	char = pygame.transform.smoothscale(char, (100, 100))     
#	done = False
#	while not done:
#		char = pygame.image.load('options2.png')
#		SCREEN.blit(char, (0,0))
#		char = pygame.transform.scale(char, (100, 100))
#		pygame.display.flip()
#		event = pygame.event.wait()

#def switch2():
#	SCREENWIDTH = 800
#	SCREENHEIGHT = 800
#	SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
#	h = pygame.image.load('help.png')
#	SCREEN.blit(h, (0,0))
#	h = pygame.transform.smoothscale(h, (100, 100))     
#	done = False
#	while not done:
#		h = pygame.image.load('help.png')
#		SCREEN.blit(h, (0,0))
#		h = pygame.transform.scale(h, (100, 100))
#		pygame.display.flip()
#		event = pygame.event.wait()
		

if __name__ == "__main__":
	pygame.init() # Initialize all pygame's modules
	pygame.display.set_caption('Hamiltonian Heist')
	Menu()
	#pygame.display.update()
	title = pygame.image.load('options2.png').convert()
	options()
	#switch()
	#char = pygame.transform.scale(char, (800, 800)) 
	h = pygame.image.load('help.png').convert()
	help2()
	player = pygame.image.load('slide2.png').convert()
	character()

	#pygame.display.update()
	#pygame.display.flip()
    
	#char = pygame.image.load('options2.png')
	#char = pygame.transform.scale(char, (800, 800)) 
	#while True:
	#	SCREEN.blit(char,(0,0))
	#	x, y = pygame.mouse.get_pos()
		# returns a single event from the queue
	#	event = pygame.event.wait()

	#	if event.type == pygame.QUIT:
	#		pygame.quit()
	#		sys.exit()


	#switch2()
	#h = pygame.transform.scale(h, (800, 800)) 

	#pygame.display.update()
	#pygame.display.flip()
	#h = pygame.image.load('options2.png')
	#h = pygame.transform.smoothscale(h, (800, 800))

	#while True:
	#	SCREEN.blit(h,(0,0))
	#	x, y = pygame.mouse.get_pos()
	#	# returns a single event from the queue
	#	event = pygame.event.wait()

	#	if event.type == pygame.QUIT:
	#		pygame.quit()
	#		sys.exit()

