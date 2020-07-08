import math
import turtle
import random
 
wn=turtle.Screen()
wn.bgcolor('azure')
wn.title('Hamiltonian Heist')
wn.setup(700,700)
wn.tracer(0)
 

images = ['wizard_left.gif', 'wizard_right.gif',
          'wall2.gif',
         'boss_left.gif', 'boss_right.gif']
for image in images:
  turtle.register_shape(image)
 
 #creates pathway/walking area for player
class Pen(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape('square')
    self.color('white')
    self.penup()
    self.speed(0)
  #displays character selected
class Player(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape('wizard_right.gif')
    self.color('blue')
    self.penup()
    self.speed(0)
    self.diamond = 0
   #player moves up
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
     #player touches a treasure
  def is_collision(self, other):
    a = self.xcor()-other.xcor()
    b = self.ycor()-other.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))
   
    if distance < 5:
      return True
    else:
      return False
    #create/place treasures on the game      
class Treasure(turtle.Turtle):
  def __init__(self, x, y):
    turtle.Turtle.__init__(self)
    self.shape('circle')
    self.color('gold')
    self.penup()
    self.speed(0)
    self.gold = 100
    self.goto(x, y)
   # get rid of treasure if touched
  def destroy(self):
    self.goto(2000, 2000)
    self.hideturtle()
   # create enemy
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
   # allow random movements of enemy that are uncontrolled
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
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXX XXXXXX       XX    X",
"XXX P XXXX       XXX    X",
"XX    XX        XXXT    X",
"XXX     X    XXXXXXX    X",
"XXXE        XXXXXXX     X",
"XXXX    X     XXXX      X",
"XXX    XX     XXX    XXXX",
"XX    XXX     XXX     XXX",
"X     XXX     XXXXX     X",
"XX    XXXXX   XXXXXX    X",
"XXX  XXXX     XXX       X",
"X   XXXXX     XXXXE     X",
"X    XXXXXXXXXXXXXXX    X",
"XX      XXXXXXXXXXXX    X",
"XXX              XXXX   X",
"XXXX             XXXX   X",
"XXXXXXXXXXXXX    XXX    X",
"XXXXXXXXXXXXX    XXX    X",
"XXX       XXX    XXX    X",
"XE               XXX    X",
"XXXX       XXXXXXXX     X",
"XXXXXX   XXXXXXXX      XX",
"X                     XXX",
"X                   XXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]
level_2=[
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XP XX          XXXXXXXXX",
"X  XX E        XXXXXXXXX",
"X      XXXXXX  XXXXXXXXX",
"XXX    XXXXXX  XXXXXXXXX",
"XX   XXXX      XXXXXXXXX",
"X    XXXX  E   XXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXX",
"X  X           XXXXXXXXX",
"X  XXXXX XXXX  XXXXXXXXX",
"X E      X  X  XXXXXXXXX",
"XXXXXXX  X     XXXXXXXXX",
"X        XXXXXXXXXXXXXXX",
"X  XX          XXXXXXXXX",
"X  XXXX   T    XXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX"
  ]
 

 
levels.append(level_1)

levels.append(level_2)
level = 0
# switch to next level if previous level completed
def next_maze():
  pen.clear()
  global walls
  walls = []
  treasures = []
  global enemies
  enemies = []
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
     
      if character=='X':
        pen.goto(screen_x,screen_y)
        pen.shape('wall2.gif')
        pen.stamp()
        walls.append((screen_x,screen_y))
       
      if character=='P':
        player.goto(screen_x,screen_y)
       
      if character=='T':
        treasures.append(Treasure(screen_x, screen_y))
       
      if character == 'E':
        enemies.append(Enemy(screen_x, screen_y))
       
pen=Pen()
player=Player()
 

walls=[]
 
treasures = []
 
enemies = []
setup_maze(levels[1])

 

turtle.listen()
turtle.onkey(player.go_left,'Left')
turtle.onkey(player.go_right,'Right')
turtle.onkey(player.go_up,'Up')
turtle.onkey(player.go_down,'Down')
wn.tracer(0)
 # if player touches enemy, start over level
 #if player touches treasure, remove the treasure
for enemy in enemies:
  turtle.ontimer(enemy.move, t=250)
 
while True:
  for treasure in treasures:
    if player.is_collision(treasure):
      player.gold = treasure.gold
      
      treasure.destroy()
      treasures.remove(treasure)
      next_maze()
     
    for enemy in enemies:
      if player.is_collision(enemy):
          pen.clear()
          levels.append(level_1)
          setup_maze(levels[1])
     
  #Update screen      
  wn.update()
