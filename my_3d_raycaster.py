from ion import *
from ulab import numpy as np
from kandinsky import *
from time import *

maps = [[1,2,2,2,2,1],
        [1,0,0,0,0,1],
        [1,3,0,3,0,1],
        [1,0,0,0,0,1],
        [1,2,2,2,2,1]]
#1 is for purple walls
#2 is for dark purple walls
#3 is for red walls

posx, posy = (1,1) #default player pos
rot=np.pi/4 #default rotation

def deg2rad(x):
  return x*np.pi/180 #function to convert degrees into radians

while True:
  fill_rect(0,0,320,222,(0,0,0)) #clears background
  for i in range(60):
    rot_i = rot+deg2rad(i-30) #rotation
    x, y = (posx,posy) 
    sin1, cos1 = (0.02*np.sin(rot_i), 0.02*np.cos(rot_i)) #fake cos and sin variables
    n=0
    while True:
      x, y = (x+cos1, y+sin1)
      n=n+1
      if maps[int(x)][int(y)] != 0: #check if it should add wall
        h = 1/(0.02*n) #adds wall
        break
    if maps[int(x)][int(y)]==2: #colors
      c=(50,10,50)
    if maps[int(x)][int(y)]==1: #colors
      c=(70,10,70)
    if maps[int(x)][int(y)]==3: #colors
      c=(150,10,10)      
    fill_rect(i+50,100+int((h)*20),1,-int((h)*20),c) #bottom walls
    fill_rect(i+50,100-int((h)*20),1,int((h)*20),c) #top walls
    fill_rect(i+50,80-int((h-1)*20),1,int((h-1)*20),(93,128,255)) #sky
    fill_rect(i+50,119+int((h-1)*20),1,-int((h-1)*20),(13,175,15)) #floor
    fill_rect(i+50,0,1,80,(0,0,0)) #black rect to remove mistakes
    fill_rect(i+50,119,1,200,(0,0,0))#black rect to remove 
  sleep(0.3) #Sets a max framerate
  
  x,y=(posx,posy) #temprary playerX and playerY 
  if (keydown(KEY_UP)): #movement code
    x,y=(x+0.3*np.cos(rot), y+0.3*np.sin(rot))
  elif (keydown(KEY_DOWN)):
    x,y=(x+0.3*np.cos(rot), y+0.3*np.sin(rot))
  elif (keydown(KEY_LEFT)):
    rot=rot-np.pi/8
  elif (keydown(KEY_RIGHT)):
    rot=rot+np.pi/8
    
  if maps[int(x)][int(y)]==0:
    posx,posy=(x,y) #moves the player if there are no walls
