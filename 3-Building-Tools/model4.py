#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:56:17 2018

@author: Evie
"""

import operator
import random
import time

#Starting time list.
time_list = []
#Start list of the number of agents created.
magnitude_list = []

#Define 'distance_between' function to find the distance between two 
#sets of co-ordinates using pythagoras.
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    
    
for p in range (4, 8):
    #Set number of agents and iterations.
    number_of_agents = 2**p
    magnitude_list.append(number_of_agents)
    print("magnitude list = ", magnitude_list)
    number_of_iterations = 10
    agents = []
    
    #Set the start co-ordinates to random points within a 100x100 grid.
    for i in range(number_of_agents):
        agents.append([random.randint(0,99),random.randint(0,99)])
    
    #Start the clock.
    start = time.perf_counter()    
   
    #Move the agents randomly twice per each iteration.
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
    
    
   
    #Test the and record the distance between all agents.
    dist_list = []
    for i in range (number_of_agents):
        for j in range (number_of_agents):
            if (i < j):
                distance = distance_between(agents[i], agents[j])
                dist_list.append(distance)
    #Stop the clock.
    end = time.perf_counter()
    time_list.append(end-start)
    print("time = " +str(end-start))
    
    #Calculate the maximum and minimum distances.
    max_dist = max(dist_list)
    min_dist = min(dist_list)
    print("maximum distance = ", max_dist)
    print("minimum distance = ", min_dist)
    
    
    
    
     
#Make a graph.
import matplotlib.pyplot as plt
plt.ylim(0, 50)
plt.xlim(0, 150)
plt.scatter(magnitude_list,time_list)
plt.plot(magnitude_list,time_list)
plt.xlabel('Number of Agents')
plt.ylabel('Time Taken (s)')
plt.title('Time of Runs as a Function of the Number of Agents')
plt.show()
