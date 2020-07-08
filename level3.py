
import turtle
import math

import pygame

levels = ['']
level_4 = [


'XXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXX',
'X                       X',
'XP          T          TX',
'X   XXXXXX     XXXXXX   X',
'X X  XXXX  XXX  XXXX  X X',
'X XX  XX  XXXXX  XX  XX X',
'X XXX    XXXXXXX    XXX X',
'X XXX T XXXXXXXXX T XXX X',
'X XX  X  XXXXXXX  X  XX X',
'X X  XXX  XXXXX  XXX  X X',
'X   XXXXX  XXX  XXXXX   X',
'XT XXXXXXX  T  XXXXXXX TX',
'X   XXXXX  XXX  XXXXX   X',
'X X  XXX  XXXXX  XXX  X X',
'X XX  X  XXXXXXX  X  XX X',
'X XXX   XXXXXXXXX   XXX X',
'X XXXT   XXXXXXX   TXXX X',
'X XX  XX  XXXXX  XX  XX X',
'X X  XXXX  XXX  XXXX  X X',
'X   XXXXXX     XXXXXX   X',
'XT          T          TX',
'X                       X',
'X                       X',
'XXXXXXXXXXXXXXXXXXXXXXXXX',
]
levels.append(level_4)
 
# Screen
 
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Hamiltonian Heist Level 3')
wn.setup(700, 700)
 
# allow imported images in game
turtle.register_shape("wizard_right.gif")
turtle.register_shape("wizard_left.gif")
turtle.register_shape("wall2.gif")


# create treasures
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

# Pen
 #creates pathway/ walking area for player
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('silver')
        self.penup()
        self.speed(0)
 
# Player
   #displays character selected
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wizard_right.gif")
        self.color('blue')
        self.penup()
        self.speed(0)
        self.gold = 0
         #player moves up
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            # player moves down
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            #player moves left
    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        self.shape("wizard_left.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            #player moves right
    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        self.shape("wizard_right.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
# player touches a treasure
    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 5:
            return True
        else:
            return False    
 
# Functions
 #create maze
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall2.gif")
                pen.stamp() 
                walls.append((screen_x, screen_y))
            if character == "P":
                player.goto(screen_x, screen_y)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
               
pen = Pen()
player = Player()

#Create wall coordinate list
walls = []


treasures = []

setup_maze(levels[1])
 
# Keyboard Bindings
 
wn.listen()
wn.onkey(player.go_up, "Up")
wn.onkey(player.go_down, "Down")
wn.onkey(player.go_left, "Left")
wn.onkey(player.go_right, "Right")
 
wn.tracer(0)
# if player touches treasure, remove/collect the treasure
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            treasure.destroy()
            treasures.remove(treasure)


    wn.update()
