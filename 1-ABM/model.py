#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:12:18 2018

@author: Evie
"""

#Import 'random' module.
import random

#Set the start co-ordinates of x0,y0 to random locations within a 100x100 grid.
y0 = random.randint(0,100)
x0 = random.randint(0,100)

#Changing y0 based on random number selection.
random_number = random.random()
if random_number < 0.5:
    y0 += 1    
else:
    y0 -= 1

#Changing x0 based on random number selection.
random_number = random.random()
if random_number < 0.5:
    x0 += 1
else:
    x0 -= 1

#Repeat to move the co-ordinates again.
random_number = random.random()
if random_number < 0.5:
    y0 += 1
else:
    y0 -= 1
    
random_number = random.random()
if random_number < 0.5:
    x0 += 1
else:
    x0 -= 1

#Print the final co-ordinates.    
print ('y0,x0 = ', y0, x0)

#Set the start co-ordinates of x1,y1 to random locations within a 100x100 grid.
y1 = random.randint(0,100)
x1 = random.randint(0,100)


#Change x1,y1 based on random number selection.
random_number = random.random()
if random_number < 0.5:
    y1 += 1    
else:
    y1 -= 1
    
random_number = random.random()
if random_number < 0.5:
    x1 += 1
else:
    x1 -= 1

#Repeat to move the co-ordinates again.
random_number = random.random()
if random_number < 0.5:
    y1 += 1
    
else:
    y1 -= 1

random_number = random.random()
if random_number < 0.5:
    x1 += 1
else:
    x1 -= 1

#Print the final location of x1,y1.    
print ('x1,y1 = ', y1, x1)

#Calculate the change between the two sets of co-ordinates.
change = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print (change)

#Visualise on a graph.
import matplotlib.pyplot as plt

xpoints = [[x0],[x1]]
ypoints = [[y0], [y1]]

plt.scatter(xpoints,ypoints)
plt.plot(xpoints, ypoints)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Presenting x0,y0 and x1,y1 graphically')

plt.show()