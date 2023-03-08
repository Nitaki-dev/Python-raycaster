from ion import * #used for keypress checks
from kandinsky import * #used to draw everything
from time import sleep #used for framerate
from math import * #used for sin and cos

#You can modify this map freely
#0 is for air
#1 is for purple walls
#2 is for dark purple walls
#3 is for red walls
maps = [[1,2,2,2,2,2,2,1],
        [1,0,0,0,0,0,0,1],
        [1,0,0,3,3,0,0,1],
        [1,0,0,0,0,0,0,1],
        [1,2,2,2,2,2,2,1]]

def pi(): #Custom pi function
  return 3.141592653589793

def deg2rad(x): #Function to convert degrees into radians
  return x*pi()/180

posx, posy = (2,2) #Default position
rot=pi()/4 #Default rotation
res=0.02 #Drawing accuracy [form 0.01 to 0.3]

def render(res):
  fill_rect(0,0,121,222,(0,0,0)) #Clears background
  fill_rect(200,0,120,222,(0,0,0)) #Clears background

  for i in range(75):
    rot_i = rot+deg2rad(i-30) #
    x, y = (posx,posy) 
    sin1, cos1 = (res*sin(rot_i), res*cos(rot_i)) #Create fake
    n=0
    while True:
      x, y = (x+cos1, y+sin1)
      n=n+1
      if maps[int(x)][int(y)] != 0: #Changes h variable 
        h = 1/(res*n) #Changes the height of the wall
        break
    if maps[int(x)][int(y)]==2: #Dark grey
      c=(30,30,30)
    if maps[int(x)][int(y)]==1: #Grey
      c=(45,45,45)
    if maps[int(x)][int(y)]==3: #Red
      c=(150,10,10)
    
    fill_rect(i+123,80,1,40,c) #Draws the walls

    fill_rect(i+123,100-20-int((h-1)*20),1,int((h-1)*20),(93,128,255)) #sky
    fill_rect(i+123,100+19+int((h-1)*20),1,-int((h-1)*20),(13,175,15)) #floor
    
    fill_rect(0,0,322,100-20-2,(0,0,0)) #Remove mistakes
    fill_rect(0,100+19+2,322,104,(0,0,0)) #Remove mistakes

    fill_rect(121,78,77,2,(255,255,255)) #Draws the frame
    fill_rect(121,119,77,2,(255,255,255)) #Draws the frame
    
print("Press UP, DOWN, LEFT or")
print("RIGHT to start the raycaster")

while True:
  x,y=(posx,posy) #Temporary player position
  if (keydown(KEY_UP)): #Moves the temporary player up
    render(res)
    x,y=(x+0.3*cos(rot), y+0.3*sin(rot))
  elif (keydown(KEY_DOWN)): #Moves the temporary player down
    render(res)
    x,y=(x-0.3*cos(rot), y-0.3*sin(rot))
  elif (keydown(KEY_LEFT)): #Rotates the temporary player left
    render(res)
    rot=rot-pi()/8
  elif (keydown(KEY_RIGHT)): #Rotates the temporary player right
    render(res)
    rot=rot+pi()/8   
  if maps[int(x)][int(y)]==0: #Checks if there are no walls
    posx,posy=(x,y) #Moves the player if there are no walls
