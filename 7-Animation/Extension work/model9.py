import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework9 as agentframework
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



#Define the number of agents, wolves and iterations.
#Set the neighbourhood.
num_of_agents = 10
num_of_wolves = 20
num_of_iterations = 100
neighbourhood = 20
agents = []
wolves = []



#Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(agents, environment))

#Make the wolves.
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(environment))



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
        
        #Move the wolves.
        for i in range(num_of_wolves):
            wolves[i].move()
            for i in range(num_of_agents):
                #If the wolves are in the same location, have them empty the agent store.
                if wolves[i].getx() == agents[i].getx() and wolves[i].gety() == agents[i].gety():
                    wolves[i].store += agents[i].store
                    agents[i].store = 0            
                else:
                    pass

        
    
#Include stopping condition.    
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
            
            
#Make the plot.            
    width = len(environment)
    height = len(environment[0])
    matplotlib.pyplot.xlim(0, width)
    matplotlib.pyplot.ylim(0, height)
    for i in range(num_of_agents):
        matplotlib.pyplot.imshow(environment)
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c = 'blue')
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, c = 'red')
    
    
    #print out agent info 
    #for i in range(num_of_agents):
        #print(agents[i].__str__())
    
#Define the 'gen_function'.    
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a
        a = a + 1
    
    
#Create animation including the stopping condition.
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()



#Store the list of agents.
storelist =[]
for agent in agents:
    storelist.append(agent.getstore())
totalstore = sum(storelist)   


#Use one agent to find another agents information.
print (agents[0].agent_list[1]._x)
     

#Save the store list information.
f = open("store.txt", 'a')
writer = csv.writer(f)
f.write(str(totalstore)+ ', ')
f.close()

#Save the environment information.
f2 = open("environment.txt", 'w')
writer = csv.writer(f2, delimiter=' ')
f2.write(str(environment))
f2.close()
