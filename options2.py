import pygame
from pygame.locals import*
import sys
import curses
from menu3 import menu3

SCREENWIDTH = 800
SCREENHEIGHT = 800
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))


title = pygame.image.load('options2.png').convert()
title = pygame.transform.scale(title, (800, 800))
pygame.init()
pygame.mixer.init() # initialize for sound
clock = pygame.time.Clock()
aqua = (0, 255, 255)
pygame.mixer.music.load('Kings_of_Yore.ogg')
pygame.mixer.music.play()
clock = pygame.time.Clock()

def options2():
    music_paused = False
    button = pygame.Rect(370, 220, 100, 50)
    while True:
        SCREEN.blit(title,(0,0))
        x, y = pygame.mouse.get_pos()
        # returns a single event from the queue
        event = pygame.event.wait()

        # if the 'close' buttom of the window is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()        
        # create option to go to Options page
        if(x>370 and y>210 and x<470 and y<265):

            X_for_h=250 #height for up and down lines
            Y_for_h=340 #left and right
            X_for_w=470 #up and down 
            Y_for_w=350 #height for side borders
            for height in range(0,9):
                Y_for_h -= 10
            for width in range(0,19):
                X_for_w += 10
            for height in range(0,9):
                Y_for_h += 10
            for width in range(0,19):
                X_for_w -= 10
            if(event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
                music_paused = False

                done = False
                while not done:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if button.collidepoint(event.pos):
                                # Toggle the boolean variable.
                                music_paused = not music_paused
                                if music_paused:
                                    pygame.mixer.music.pause()
                                else:
                                    pygame.mixer.music.unpause()

                    pygame.display.flip()
                    clock.tick(60)

        # create option to go back to main menu
        elif(x>25 and y>50 and x<245 and y<75):

            X_for_h=100 #height for up and down lines
            Y_for_h=100 #left and right
            X_for_w=50 #up and down 
            Y_for_w=55 #height for side borders
            for height in range(0,8):
                Y_for_h -= 10
            for width in range(0,19):
                X_for_w += 10
            for height in range(0,8):
                Y_for_h += 10
            for width in range(0,19):
                X_for_w -= 10
            if(event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
                print('help')
                menu3()

        pygame.display.update()

if __name__ == "__main__":
    pygame.init() # Initialize all pygame's modules
    pygame.display.set_caption('Hamiltonian Heist')
    title = pygame.image.load('options2.png').convert()
    title = pygame.transform.scale(title, (800, 800))
    options2()

    menu = pygame.image.load('menu.png').convert()
    menu3()
