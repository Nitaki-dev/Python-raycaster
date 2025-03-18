from ion import * #used for keypress checks
from kandinsky import fill_rect, draw_string #used to draw everything
from time import sleep #used for framerate
from math import * #used for sin and cos
from random import * #used for random map generation

#Custom pi function cause the math.pi one caused issues
pi2 = 3.141592653589793
  
#Basic function to convert degrees into radians
def deg2rad(x): 
  return x*2/180

#Makes a list of random floats within a set range
def uniform2(low: float = ..., high: float = ..., size: int = 1) -> List[float]:
    return [uniform(low, high) for _ in range(size)]

def startingScreen():
  while True:
    fill_rect(0,0,322,222,(0,0,0))
    draw_string("Insider", 120, 30, (255,0,0), (0,0,0))
    draw_string("Press OK to start", 70, 85, (255,255,255), (0,0,0))
    draw_string("Created by Nitaki - 2023", 0, 205, (255,255,255), (0,0,0))
    if keydown(KEY_OK) or keydown(KEY_UP):
      fill_rect(0,0,322,222,(0,0,0))
      break
    
startingScreen()
roomCount=0 #room counter

#Function that runs the whole game
def main():
  res=0.2 #Details (from 0.8 to 0.02)
  size=15 #map size (bigger=laggier)
  
  maps=[[list(uniform2(0,1,3))]*size for i in range(size)]
  for i in range(size-2):
    for j in range(size-2):
      if random()>0.33:
        maps[i+1][j+1]=0
    
  #Randomize the player starting pos
  posx, posy = (1, randint(1, size-1))
  rot=pi2/4 #Default rotation
  x,y=(posx,posy)
  maps[x][y]=0 #sets player's spawn to air
  
  count=0
  while True:
    testx, testy = (x,y)
    if random()>0.5:
      testx=testx+choice([-1,1])
    else:
      testy=testy+choice([-1,1])
    if testx>0 and testx < size-1 and testy>0 and testy<size-1:
      if maps[testx][testy]==0 or count>5:
        count=0
        x,y=(testx, testy)
        maps[x][y]=0
        if x==size-2:
          exitx,exity=(x,y)
          maps[x][y]=2
          break
      else:
        count=count+1
        
  scaleX=3   #Strech the screen
  scaleY=50  #Idk how to explain it
  depth_test=8         #depth fad out
  max_draw_distance=0.4 #render distance

  def render(res):
    nn=0
    for i in range(75):
      rot_i = rot+deg2rad(i-30) #
      x, y = (posx,posy)
      #Custom cos and sin relative to the resolution and the player's rotation
      sin1, cos1 = (res*sin(rot_i), res*cos(rot_i))
      n=0
      nn=nn+scaleX #Strech on X axis
      while True:
        x, y = (x+cos1, y+sin1)
        n=n+1
        if maps[int(x)][int(y)] != 0: #Changes h variable
          if (1/(res*n))*2<max_draw_distance:
            h=15
          else:
            h=(1/(res*n))*2
          if (h==15):
            c=(0,0,0)
          elif (int((h-1)*scaleY)<0):
            c = (255-(-int(((h-1)*depth_test)*scaleY)), 
                 255-(-int(((h-1)*depth_test)*scaleY)),
                 255-(-int(((h-1)*depth_test)*scaleY))) #Change wall color base on depth
          else:
            c=(255,255,255)
          break
      
      fill_rect(i+nn+6,10,4,100+30+int((h-1)*scaleY),c) #Draws the walls
      fill_rect(i+nn+6, 0, 4, -int((h-1)*scaleY), (0,0,0)) #Draws the ceiling
      fill_rect(i+nn+6,100+30+int((h-1)*scaleY),4,150,(0,0,0)) #Draws the floor
      draw_string("You're at x:" + str(int(posx)) + " y:" + str(int(posy)), 7,140, (255,255,255), (0,0,0))
      draw_string("Get to x:" + str(int(exitx)) + " y:" + str(int(exity)), 7, 180, (255,255,255), (0,0,0))
      draw_string("Room " + str(roomCount), 250, 180, (255,255,255), (0,0,0))
  
  while True: #Keypress loop
    x,y=(posx,posy) #Temporary player position
    if (keydown(KEY_UP)): #Moves the temporary player up
      x,y=(x+0.3*cos(rot), y+0.3*sin(rot))
    elif (keydown(KEY_DOWN)): #Rotates the temporary player left
      x,y=(x-0.3*cos(rot), y-0.3*sin(rot))
    elif (keydown(KEY_LEFT)): #Rotates the temporary player left
      rot=rot-pi2/16      #SLOW TURNING
    elif (keydown(KEY_RIGHT)): #Rotates the temporary player right
      rot=rot+pi2/16      #SLOW TURNING
    
    if maps[int(x)][int(y)]==0: #Checks if there are no walls
      if int(posx) == exitx and int(posy) == exity: #check if player is at exit point
        break
      posx,posy=(x,y) #Moves the player if there are no walls
    
    if (keydown(KEY_UP) or keydown(KEY_DOWN) or keydown(KEY_LEFT) or keydown(KEY_RIGHT)):
      render(res)

def shouldEnterNewRoom():
  while True: #Enter new room screen
    fill_rect(0,0,322,220,(0,0,0))
    draw_string("Press OK to enter room "+str(roomCount),40,5, (255,255,255), (0,0,0))
    if (keyboard.is_pressed("up")):
      fill_rect(0,0,322,222,(0,0,0))
      return

roomCount=roomCount+1
main() #main game

if (roomCount<5): #change the 5 to the winning room point
  main() #main game
  roomCount=roomCount+1 #adds room to room counter
  shouldEnterNewRoom() #New room screen
else:
  #Winning screen
  fill_rect(0,0,322,220,(0,0,0))
  draw_string("You won! (reached room "+str(roomCount) + ")",40,5, (255,255,255), (0,0,0))
