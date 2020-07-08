import math
import turtle
import random
 
wn=turtle.Screen()
wn.bgcolor('azure')
wn.title('Hamiltonian Heist')
wn.setup(700,700)
wn.tracer(0)
 
#GIF imports
images = ['wizard_left.gif', 'wizard_right.gif',
          'wall2.gif',
         'boss_left.gif', 'boss_right.gif']
for image in images:
  turtle.register_shape(image)
 
# create pathway/walk area for player
class Pen(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape('square')
    self.color('white')
    self.penup()
    self.speed(0)
# create player
class Player(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape('wizard_right.gif')
    self.color('blue')
    self.penup()
    self.speed(0)
    self.diamond = 0
  # player moves up
  def go_up(self):
    move_to_x=self.xcor()
    move_to_y=self.ycor()+24
   
    if (move_to_x,move_to_y) not in walls:
      self.goto(move_to_x,move_to_y)
    # player moves down
  def go_down(self):
    move_to_x=self.xcor()
    move_to_y=self.ycor()-24
   
    if (move_to_x,move_to_y) not in walls:
      self.goto(move_to_x,move_to_y)
    # player moves left
  def go_left(self):
    move_to_x=self.xcor()-24
    move_to_y=self.ycor()
   
    self.shape('wizard_left.gif')
   
    if (move_to_x,move_to_y) not in walls:
      self.goto(move_to_x,move_to_y)
    # player moves right
  def go_right(self):
    move_to_x=self.xcor()+24
    move_to_y=self.ycor()
   
    self.shape('wizard_right.gif')
   
    if (move_to_x,move_to_y) not in walls:
      self.goto(move_to_x,move_to_y)
    # if player touches/collects with treasure
  def is_collision(self, other):
    a = self.xcor()-other.xcor()
    b = self.ycor()-other.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))
   
    if distance < 5:
      return True
    else:
      return False
  # create treasures                 
class Treasure(turtle.Turtle):
  def __init__(self, x, y):
    turtle.Turtle.__init__(self)
    self.shape('circle')
    self.color('gold')
    self.penup()
    self.speed(0)
    self.gold = 100
    self.goto(x, y)
   
  def destroy(self):
    self.goto(2000, 2000)
    self.hideturtle()
  # create enemies 
class Enemy(turtle.Turtle):
  def __init__(self, x, y):
    turtle.Turtle.__init__(self)
    self.shape('boss_left.gif')
    self.color('orange')
    self.penup()
    self.speed(0)
    self.gold = 25
    self.goto(x, y)
    self.direction = random.choice(['up', 'down', 'left', 'right'])
   # enemy moves randomly without control from user
   # prevents enemy from falling off screen or walking through the blocks
  def move(self):
    if self.direction == 'up':
      dx = 0
      dy = 24
    elif self.direction == 'down':
      dx = 0
      dy = -24
    elif self.direction == 'left':
      dx = -24
      dy = 0    
    elif self.direction == 'right':
      dx = 24
      dy = 0
    else:
      dx = 0
      dy = 0
     
    move_to_x = self.xcor() + dx
    move_to_y = self.ycor() + dy
   
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)
    else:
      self.direction = random.choice(['up', 'down', 'left', 'right'])
     
    turtle.ontimer(self.move, t=random.randint(100, 300))
     
  def destroy(self):
    self.goto (2000, 2000)
    self.hideturtle()
         
levels=['']
 
level_1 = [
'XXXXXXXXXXXXXXXXXXXXXXXXX',
'X  XXXXXXX          XXXXX',
'X  XXXXXXX  XXXXXX  XXXXX',
'X       XX  XXXXXX  XXXXX',
'X       XX  XXX        XX',
'XXXXXX  XX  XXX        XX',
'XXXXXX  XX  XXXXXX  XXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXX',
'XPTTTTTTTXXXXXXXTTTTTTTTX',
'XTXXXXXXTXXXXXXXTXXXXXXTX',
'XTXXXXXXTXXXXXXXTXXXXXXTX',
'XTXXXXXXTXXXXXXXTXXXXXXTX',
'XTXXXXXXTTTTTTTTTXXXXXXTX',
'XTXXXXXXXXXXXXXXXXXXXXXTX',
'XTXXXXXXXXXXXXXXXXXXXXXTX',
'XTTTTTTTTTTTTTTTTTTTTTTTX',
'XXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXX  XXXXXXXXXXXXX',
'XXXXXXXXXX              X',
'XX   XXXXX              X',
'XX   XXXXXXXXXXXXX  XXXXX',
'XX     XXXXXXXXXXX  XXXXX',
'XX          XXXX        X',
'XXXX                    X',
'XXXXXXXXXXXXXXXXXXXXXXXXX']
level_2=[
'XXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXX',
'XP          T    E     TX',
'X   XXXXXX  E  XXXXXX   X',
'X X  XXXX  XXX  XXXX  X X',
'X XX  XX  XXXXX  XX  XX X',
'X XXX    XXXXXXX    XXX X',
'X XXX T XXXXXXXXX T XXX X',
'X XX  X  XXXXXXX  X  XX X',
'X X  XXX  XXXXX  XXX  XEX',
'X   XXXXX  XXX  XXXXX   X',
'XT XXXXXXX  T  XXXXXXX TX',
'X   XXXXX  XXX  XXXXX   X',
'X X  XXX  XXXXX  XXX  X X',
'XEXX  X  XXXXXXX  X  XX X',
'X XXX   XXXXXXXXX   XXX X',
'X XXXT   XXXXXXX   TXXX X',
'X XX  XX  XXXXX  XX  XX X',
'X X  XXXX  XXX  XXXX  X X',
'X   XXXXXX     XXXXXX   X',
'XT    E      T         TX',
'XXXXXXXXXXXXXXXXXXXXXXXXX',                       
'XXXXXXXXXXXXXXXXXXXXXXXXX',                      
'XXXXXXXXXXXXXXXXXXXXXXXXX',
]
 
treasures = []
 
enemies = []
 
levels.append(level_1)

levels.append(level_2)
level = 0
# move to next level
def next_maze():
  pen.clear()
  global walls
  walls = []
  global treasures
  treasures = []
  global level
  level += 1
  setup_maze(level_2)

 # create maze
def setup_maze(level):
  for y in range(len(level)):
    for x in range(len(level[y])):
      character=level[y][x]
      screen_x=-288+(x*24)
      screen_y=288-(y*24)
     # walls are X
      if character=='X':
        pen.goto(screen_x,screen_y)
        pen.shape('wall2.gif')
        pen.stamp()
        walls.append((screen_x,screen_y))
       # player is P
      if character=='P':
        player.goto(screen_x,screen_y)
       # treasures are T
      if character=='T':
        treasures.append(Treasure(screen_x, screen_y))
       #enemies are E
      if character == 'E':
        enemies.append(Enemy(screen_x, screen_y))
       
pen=Pen()
player=Player()
 
collect = 0
walls=[]
 

setup_maze(levels[1])

 

turtle.listen()
turtle.onkey(player.go_left,'Left')
turtle.onkey(player.go_right,'Right')
turtle.onkey(player.go_up,'Up')
turtle.onkey(player.go_down,'Down')
wn.tracer(0)
 
for enemy in enemies:
  turtle.ontimer(enemy.move, t=250)
 # if player doesn't collect all treasures, restart level
 # if player doesn't end up at starting position, restart level
 # if player touches enemy, restart level
 # if player touches a treasure twice, restart level
 # if all conditions do not apply, move onto next level
while True:
  for treasure in treasures:
    if player.is_collision(treasure):
      player.gold = treasure.gold
      
      treasure.destroy()
      treasures.remove(treasure)
      collect += 1
      if collect == 65:
        next_maze()
     
    for enemy in enemies:
      if player.is_collision(enemy):
          collect == 0
          pen.clear()
          levels.append(level_2)
          setup_maze(levels[1])
     
  #Update screen      
  wn.update()
