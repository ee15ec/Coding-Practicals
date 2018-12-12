#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:03:55 2018

@author: Evie
"""
import random

#Create the Agent class.
class Agent():
    def __init__ (self):
        #Set start location based on a random number.
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
   
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def setx(self, value):
        self._x = value
    def sety(self, value):
        self._y = value
    def delx(self):
        del self._x
    def dely(self):
        del self._y
    x = property(getx, setx, delx)
    y = property (gety, sety, dely)
    
    #Define the 'move' function which moves the agent
    #but ensuring they are kept within the bounds of the plot.       
    def move (self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100