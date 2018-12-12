#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:03:42 2018

@author: Evie
"""

import operator
import random
import time
import matplotlib.pyplot as plt



#Define 'distance_between' function to find the distance between two 
#sets of co-ordinates using pythagoras.
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5



#Set the number of agents and iterations.
number_of_agents = 10
number_of_iterations = 100
agents = []

#Set the start co-ordinates to random points within a 100x100 grid.
for i in range(number_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

#Start the clock and time list.
time_list = []
start = time.perf_counter()


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



dist_list = []
#Loop the distance test.
for i in range (number_of_agents):
    for j in range (number_of_agents):
        if (i < j):
            distance = distance_between(agents[i], agents[j])
            dist_list.append(distance)
            print("distance between", agents[i], "and ", agents[j], distance)
            
#Stop the clock
end = time.perf_counter()
time_list.append(str(end-start))
print("time = " +str(end-start))

#Calculate maximum and minimum distances between the Agents.
max_dist = max(dist_list)
min_dist = min(dist_list)
print("maximum distance = ", max_dist)
print("minimum distance = ", min_dist)


#Calculate which agent is furthest east.
m = max(agents,key=operator.itemgetter(1))
print(m)


#Make a graph.
plt.ylim(0, 100)
plt.xlim(0, 100)
#Loop through agents to visulise all on a scatter plot
for i in range(number_of_agents):
    plt.scatter(agents[i][1],agents[i][0])
#Make the furthest east agent red.
plt.scatter(m[1], m[0], color='red')
plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.title('Presenting agents graphically')
plt.show()
