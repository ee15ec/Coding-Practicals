#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:07:55 2018

@author: Evie
"""

import random
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.pyplot as plt
import matplotlib.animation
import agentframework11 as agentframework
import requests
from bs4 import BeautifulSoup
import csv
!brew install imagemagick


#Retieve data from the webpage.
r = requests.get ('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = BeautifulSoup(content, 'html.parser')
#Retrieve x and y values from the webpage text.
td_x = (soup.find_all(attrs={"class" :  "x"}))
td_y = (soup.find_all(attrs={"class" : "y"}))



#Get environment information from text file.
textfile = open("in.txt")

environment = []

for line in textfile:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
textfile.close()


#Define the figure.
fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0, 0, 1, 1])


#Define the number of iterations, agents, wolves, and neighbourhood.
num_of_agents = 5
num_of_wolves = 5
num_of_iterations = 100
neighbourhood = 20
agents = []
wolves = []



#Make the agents from the webpage data.
for i in range(num_of_agents):
    y = int(td_y[i].text)
    x = int(td_x[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
    
#Make the wolves based on the environment parameters.
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(environment))



carry_on = True

#Define 'update' for the animation to show each new move.
def update(frame_number):
    fig.clear()
    global carry_on   
    
    

    
    # Move the agents, they eat pixels and share with their neighbour.
    for j in range(num_of_iterations):
        for k in range(len(agents)):
            random.shuffle(agents)
            agents[k].move()
            agents[k].eat()
            agents[k].share_with_neighbours(neighbourhood)
       
        #Move the wolves.
        for i in range(num_of_wolves):
            wolves[i].move()       
            #If the location of agents and the wolves are the same, the agent is eaten and removed.
            for k in range(num_of_agents):
                if k < len(agents) :
                    if wolves[i].getx() == agents[k].getx() and wolves[i].gety() == agents[k].gety():
                        agents.pop(k)
                        print("wolf eating agent")
                    else:
                        pass
    
      
      
    #Include stopping condition.   
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
            
         
    #Make the plot.            
    width = len(environment)
    height = len(environment[0])
    plt.xlim(0, width)
    plt.ylim(0, height)
    plt.title("Agents and Wolves")
    agents_x = []
    agents_y = []
    for k in range(len(agents)):
        agents_x.append(agents[k].getx())
        agents_y.append(agents[k].gety())
    wolf_x = []
    wolf_y = []
    for i in range(num_of_wolves):  
        wolf_x.append(wolves[i].getx())
        wolf_y.append(wolves[i].gety())
        
    #Plot agents and wolves on a scatter graph.
    plt.imshow(environment)
    plt.scatter(agents_x,agents_y, c="blue", label = "Agents")    
    plt.scatter(wolf_x, wolf_y, c="red", label = "Wolves")
    #Add a legend.
    plt.legend(loc='upper left')
      

#Define the 'gen_function' for the animation. 
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a
        a = a + 1
 



  
#Making the model in a new page.    
root = tkinter.Tk()    
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#Define the command 'run' in the model menu to start the animation.
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False) 
    canvas.draw()

#Add a menu.   
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label='Model', menu=model_menu)
model_menu.add_command(label="Run model", command=run)



#Calculate the total store of all the agents.
storelist =[]
for agent in agents:
    storelist.append(agent.getstore())
totalstore = sum(storelist)   

#Save the agent information for each run to a file. 
agentfile = open("agent.txt", 'a')
writer = csv.writer(agentfile)
for i in range(num_of_agents):
    agentfile.write('Agent '+ str(agents[i].__str__())+', ')
agentfile.write("Total store = " + str(totalstore) +',')    
agentfile.close()

#Save the wolf information for each run to a file. 
wolffile = open("wolf.txt", 'a')
writer = csv.writer(wolffile)
for i in range(num_of_wolves):
    wolffile.write('Wolf '+ str(wolves[i].__str__()) + ', ')
wolffile.write("Total store = " + str(totalstore) +',')    
wolffile.close()

#Save the environment data to a file.
envirofile = open("environment.txt", 'w')
writer = csv.writer(envirofile, delimiter=' ')
envirofile.write(str(environment))
envirofile.close()

tkinter.mainloop()
