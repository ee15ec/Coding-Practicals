#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:17:37 2018

@author: Evie
"""
import random
import operator
import matplotlib.pyplot
import agentframework7 as agentframework
import csv
import sys




#Get the environment data from file.
f = open("in.txt")

environment = []

for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
f.close()

#Define the number of agents, iterations and the neighbourhood based on 
#information entered in the command line.
num_of_agents = int(sys.argv[1])
num_of_iterations = int(sys.argv[2])
neighbourhood = int(sys.argv[3])
agents = []

#Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(agents, environment))

#Move the agents, have them eat and share their store with neighbours.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        random.shuffle(agents)
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

#Make a plot.        
width = len(environment)
height = len(environment[0])
matplotlib.pyplot.xlim(0, width)
matplotlib.pyplot.ylim(0, height)
for i in range(num_of_agents):
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()


#Show the agent x,y and store values.
for i in range(num_of_agents):
    print(agents[i].__str__())

#Calculate the total store.
storelist =[]
for agent in agents:
    storelist.append(agent.getstore())
totalstore = sum(storelist)   

#Use one agent to find another agents information.
print (agents[0].agent_list[1]._x)
    

#Save store values to a file.
f = open("store.txt", 'a')
writer = csv.writer(f)
f.write(str(totalstore)+ ', ')
f.close()

#Save environment values to a file.
f2 = open("environment.txt", 'w')
writer = csv.writer(f2, delimiter=' ')
f2.write(str(environment))
f2.close()


