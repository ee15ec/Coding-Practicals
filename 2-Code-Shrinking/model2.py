#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:12:18 2018

@author: Evie
"""
import operator
import random
import matplotlib.pyplot as plt

#Set number of agents and iterations.
number_of_agents = 10
number_of_iterations = 100
agents = []

#Set the start co-ordinates to random points within a 100x100 grid.
for i in range(number_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])



#Move the Agents twice for each iteration.
for j in range(number_of_iterations):
    for i in range(number_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


    


#Calculate which agent is furthest east.
print(max(agents, key=operator.itemgetter(1)))
m = max(agents,key=operator.itemgetter(1))


#Plot a graph.
plt.ylim(0, 100)
plt.xlim(0, 100)
for i in range(number_of_agents):
    plt.scatter(agents[i][1],agents[i][0])
#Set the furthest east to appear red. 
plt.scatter(m[1], m[0], color='red')
plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.title('Presenting agents graphically')
plt.show()
