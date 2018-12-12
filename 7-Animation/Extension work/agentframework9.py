#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:03:55 2018

@author: Evie
"""
import random

#Define Agent class.
class Agent():
    def __init__ (self, agent_list, environment):
        #Set the Agent list.        
        self.agent_list = agent_list
        #Connect the environment of the Agent with the environment data.
        self.environment = environment
        self.width = len(environment)
        self.height = len(environment[0])
        #Set the Agent store.       
        self.store = 0
        #Set the start co-ordinates randomly.
        self._y = random.randint(0,self.width)
        self._x = random.randint(0,self.height)

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
  
    #Define 'getstore' function which returns the value of the store.
    def getstore(self):
        return self.store
       
    #Define the 'eat' function which makes the agent add to it's store if its 
    #location has a value more than 50.      
    def eat(self): 
        if self.environment[self._y][self._x] > 50:
            self.environment[self._y][self._x] -= 50
            self.store += 50
        else:
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
   
    #Define the 'move' function which moves the agent
    #within the parameters of the environment.                  
    def move (self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % self.height
        else:
            self._y = (self._y - 1) % self.height

        if random.random() < 0.5:
            self._x = (self._x + 1) % self.width
        else:
            self._x = (self._x - 1) % self.width
    
    #Define '__str__' function which returns the x, y, and store values for the agent.                       
    def __str__ (self):
        return ('x = ' + str(self._x), 'y = '+ str(self._y), 'store = ' + str(self.store))
    
    #Define the 'distance_between' function which calculates the pythagorean 
    #distance between two agents.
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
    
    #Define 'share_with_neighbours' which shares the agents stores with another 
    #if they are within a certain distance of each other.      
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agent_list:
            distance = self.distance_between(agent)
            
            if distance <= neighbourhood and distance != 0:
                total_store = self.store + agent.store
                av = total_store/2
                self.store = av
                agent.store = av
                #print("sharing " + str(distance) + " " + str(av))

#Define the Wolf class similarly to the Agent class.                
class Wolf():
    def __init__ (self, environment):
        self.environment = environment
        self.width = len(environment)
        self.height = len(environment[0])
        self.store = 0
        self._y = random.randint(0,self.width)
        self._x = random.randint(0,self.height)
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
   
    #Define the 'getstore' function which returns the value of the store.                         
    def getstore(self):
        return self.store
   
    #Define the 'move' function which moves the wolves within the parameters 
    #of the environment.        
    def move (self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % self.height
        else:
            self._y = (self._y - 1) % self.height

        if random.random() < 0.5:
            self._x = (self._x + 1) % self.width
        else:
            self._x = (self._x - 1) % self.width
        