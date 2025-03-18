from ion import * #used for keypress checks
from kandinsky import fill_rect, draw_string #used to draw everything
from time import sleep #used for framerate
from math import * #used for sin and cos
from random import * #used for random map generation

#Custom pi function cause the math.pi one caused issues
def pi():
  return 3.141592653589793
  
#Basic function to convert degrees into radians
def deg2rad(x): 
  return x*pi()/180

#Makes a list of random floats within a set range
def uniform2(low: float = ..., high: float = ..., size: int = 1) -> List[float]:
    return [uniform(low, high) for _ in range(size)]

def startingScreen():
  while True:
    fill_rect(0,0,322,220,(0,0,0))
    draw_string("Insider", 120, 30)
    draw_string("Press OK to start", 70, 85)
    draw_string("Created by Nitaki - 2023", 0, 205)
    if (keydown(KEY_OK)):
      break
    
startingScreen()

roomCount=0 #room counter

#Function that runs the whole game
def main():
  res=0.3 #Details (from 0.8 to 0.02)
  
  size=15 #map size (bigger=laggier)
  
  #This creates an 15x15 map filled with walls
  maps=[]
  for i in range(size):
    maps.append([])
    for j in range(size):
      maps[i].append(list(uniform2(0,1,3)))
  
  #Randomize the player starting pos
  posx, posy = (1, randint(1, size-1))
  rot=pi()/4 #Default rotation
  x,y=(posx,posy)
  maps[x][y]=0 #sets player's spawn to air
  
  while True:
    testx, testy = (x,y)
    if random()>0.5: #If random num (between 0 and 1) is >0.5,
      testx = testx + choice([-1,1]) #then add -1 or 1 to testx randomly.
    else:
      testy = testy + choice([-1,1]) #otherwise add -1 or 1 to testy randomly.
    #Checks if testx and testy are within the map boundaries
    if testx>0 and testx<size-1 and testy>0 and testy<size-1:
      x,y=(testx,testy) #update x and y
      maps[x][y] = 0 #replaces wall with air
      if x==size-2:
        exitx, exity = (x,y) #Creates the exit point
        break
  
  scaleX=3   #Strech the screen
  scaleY=50  #Idk how to explain it
  
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
          h = (1/(res*n))*2 #Changes the height of the wall
          if (int((h-1)*scaleY)<0):
            c = (5, int((h-1)*scaleY), 117) #Wall depth
          else:
            c = (5,255,117) #Close walls
          break
      
      fill_rect(i+nn+6,10,4,150,c) #Draws the walls
      
      fill_rect(i+nn+6,100-90-int((h-1)*scaleY),4,int((h-1)*scaleY),(4,110,108)) #sky
      fill_rect(i+nn+6,100+30+int((h-1)*scaleY),4,-int((h-1)*scaleY),(110,110,110)) #floor
      
      fill_rect(0,0,322,15,(0,0,0)) #Clears background
      fill_rect(0,125,322,100,(0,0,0)) #Clears background
  
      draw_string("Player x:" + str(int(posx)) + " y:" + str(int(posy)),0,140)
      draw_string("Next room: x " + str(int(exitx)) + " y " + str(int(exity)), 0, 180)
  
  fill_rect(0,0,320,222,(0,0,0)) #clears screen
  
  while True: #Keypress loop
    x,y=(posx,posy) #Temporary player position
    if (keydown(KEY_UP)): #Moves the temporary player up
      x,y=(x+0.3*cos(rot), y+0.3*sin(rot))
    elif (keydown(KEY_DOWN)): #Moves the temporary player down
      x,y=(x-0.3*cos(rot), y-0.3*sin(rot))
    elif (keydown(KEY_LEFT)): #Rotates the temporary player left
      rot=rot-pi()/8
    elif (keydown(KEY_RIGHT)): #Rotates the temporary player right
      rot=rot+pi()/8   
    
    if (keydown(KEY_UP) or keydown(KEY_DOWN) or keydown(KEY_LEFT) or keydown(KEY_RIGHT)):
      render(res)
      
    if maps[int(x)][int(y)]==0: #Checks if there are no walls
      if int(posx) == exitx and int(posy) == exity: #check if player is at exit point
        break
      posx,posy=(x,y) #Moves the player if there are no walls

def shouldEnterNewRoom():
  while True: #Enter new room screen
    fill_rect(0,0,322,220,(0,0,0))
    draw_string("Press OK to enter room "+str(roomCount),40,5)
    if (keydown(KEY_OK)):
      break


if (roomCount<5): #change the 5 to the winning room point
  main() #main game
  roomCount=roomCount+1 #adds room to room counter
  shouldEnterNewRoom() #New room screen
else:
   #Winning screen
  fill_rect(0,0,322,220,(0,0,0))
  draw_string("You won! (reached room "+str(roomCount) + ")",40,5)
