import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework8 as agentframework
import csv




#Retrieve environment information from text file.
f = open("in.txt")

environment = []

for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
#print(environment)
f.close()


#Define the figure.
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0, 0, 1, 1])




#Define the number of agents and iterations.
#Set the neighbourhood.
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []




#Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(agents, environment))


carry_on = True

#Define 'update' for the animation to show each new move.
def update(frame_number):
    fig.clear()
    global carry_on   
    
    
    
    #Move the agents.
    #Have them eat and share their store with neighbours.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            random.shuffle(agents)
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
 
    
#Include stopping condition.    
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
            
            
#Make a plot.            
    width = len(environment)
    height = len(environment[0])
    matplotlib.pyplot.xlim(0, width)
    matplotlib.pyplot.ylim(0, height)
    matplotlib.pyplot.title("Agents")
    for i in range(num_of_agents):
        matplotlib.pyplot.imshow(environment)
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    
    
    #Print out agent information.
    #for i in range(num_of_agents):
        #print(agents[i].__str__())
    

#Define the 'gen_function'.
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a
        a = a + 1
    
    


#Create an animation including the stopping condition.
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()



#Store the list of agents.
storelist =[]
for agent in agents:
    storelist.append(agent.getstore())
totalstore = sum(storelist)   


#Using one agent to find another agents information.
print (agents[0].agent_list[1]._x)
     

#Saving store list information
f = open("store.txt", 'a')
writer = csv.writer(f)
f.write(str(totalstore)+ ', ')
f.close()

#Saving environment information
f2 = open("environment.txt", 'w')
writer = csv.writer(f2, delimiter=' ')
f2.write(str(environment))
f2.close()


