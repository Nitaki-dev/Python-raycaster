from ion import * #used for keypress checks
from ulab import numpy as np #used for every calculation
from kandinsky import * #used to draw everything
from time import * #used for framerate

maps = [[1,2,2,2,2,1], #You can edit this map however you want
        [1,0,0,0,0,1],
        [1,3,0,3,0,1],
        [1,0,0,0,0,1],
        [1,2,2,2,2,1]]
        
#1 is for purple walls
#2 is for dark purple walls
#3 is for red walls

posx, posy = (1,1) #Default position
rot=np.pi/4 #Default rotation

def deg2rad(x):
  return x*np.pi/180 #Function to convert degrees into radians

while True:
  fill_rect(0,0,320,222,(0,0,0)) #Clears background
  for i in range(75):
    rot_i = rot+deg2rad(i-30) #
    x, y = (posx,posy) 
    sin1, cos1 = (0.02*np.sin(rot_i), 0.02*np.cos(rot_i)) #Create fake cos and sin variables
    n=0
    while True:
      x, y = (x+cos1, y+sin1)
      n=n+1
      if maps[int(x)][int(y)] != 0: #Changes h variable 
        h = 1/(0.02*n) #Changes the height of the wall
        break
    if maps[int(x)][int(y)]==2: #Dark purple
      c=(50,10,50)
    if maps[int(x)][int(y)]==1: #Purple
      c=(70,10,70)
    if maps[int(x)][int(y)]==3: #Red
      c=(150,10,10)
      
    fill_rect(i+123,100+int((h)*20),1,-int((h)*20),c) #draws bottom walls
    fill_rect(i+123,100-int((h)*20),1,int((h)*20),c) #drawstop walls
    
    fill_rect(i+123,100-20-int((h-1)*20),1,int((h-1)*20),(93,128,255)) #sky
    fill_rect(i+123,100+19+int((h-1)*20),1,-int((h-1)*20),(13,175,15)) #floor
    
    fill_rect(i+123,0,1,100-20,(0,0,0)) #Remove mistakes
    fill_rect(i+123,100+19,1,200,(0,0,0)) #Remove mistakes
    
  sleep(0.3) #Sets a max framerate
  
  x,y=(posx,posy) #Temporary player position
  
  if (keydown(KEY_UP)): #Moves the temporary player up
    x,y=(x+0.3*np.cos(rot), y+0.3*np.sin(rot))
  elif (keydown(KEY_DOWN)): #Moves the temporary player down
    x,y=(x+0.3*np.cos(rot), y+0.3*np.sin(rot))
  elif (keydown(KEY_LEFT)): #Rotates the temporary player left
    rot=rot-np.pi/8
  elif (keydown(KEY_RIGHT)): #Rotates the temporary player right
    rot=rot+np.pi/8
    
  if maps[int(x)][int(y)]==0: #Checks if there are no walls
    posx,posy=(x,y) #Moves the player if there are no walls
