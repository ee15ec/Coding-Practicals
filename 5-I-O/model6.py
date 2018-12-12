import random
import operator
import matplotlib.pyplot
import agentframework6 as agentframework
import csv




#Get environment information from a text file.
f = open("in.txt")

environment = []

for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
f.close()



#Define 'distance_between' function to return the distance between 
#two sets of co-ordinates using pythagoras
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

#Set the number of agents and iterations.
num_of_agents = 10
num_of_iterations = 100
agents = []

#Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

#Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
 
#Make a plot.       
width = len(environment)
height = len(environment[0])
matplotlib.pyplot.xlim(0, width)
matplotlib.pyplot.ylim(0, height)
for i in range(num_of_agents):
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

#Calculate the distance between agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

#Show the x,y, and store values for each agent.
for i in range(num_of_agents):
    print(agents[i].__str__())

#Calculate the total store of all the agents.
storelist =[]
for agent in agents:
    storelist.append(agent.getstore())
totalstore = sum(storelist)   




#Save the total store for each run to a file. 
f = open("store.txt", 'a')
writer = csv.writer(f)
f.write(str(totalstore)+ ', ')
f.close()

#Save the environment data to a file.
f2 = open("environment.txt", 'w')
writer = csv.writer(f2, delimiter=' ')
f2.write(str(environment))
f2.close()