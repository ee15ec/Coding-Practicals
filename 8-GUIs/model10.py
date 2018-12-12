import random
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.pyplot as plt
import matplotlib.animation
import agentframework10 as agentframework




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


#Define the figure.
fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0, 0, 1, 1])


#Define the number iterations, agents, wolves, and neighbourhood.
num_of_agents = 10
num_of_wolves = 10
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
    
    

    #Move the agents, have them eat and share with their store with neighbours.
    for j in range(num_of_iterations):
        for k in range(len(agents)):
            random.shuffle(agents)
            agents[k].move()
            agents[k].eat()
            agents[k].share_with_neighbours(neighbourhood)
        
        #Move the wolves.
        for i in range(num_of_wolves):
            wolves[i].move()
            for k in range(num_of_agents):
                #If the location of agents and wolves are the same, the agent is eaten and removed.
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
    #Add agents to a list.
    agents_x = []
    agents_y = []
    for k in range(len(agents)):
        agents_x.append(agents[k].getx())
        agents_y.append(agents[k].gety())
    #Add wolves to a list.
    wolf_x = []
    wolf_y = []
    for i in range(num_of_wolves):  
        wolf_x.append(wolves[i].getx())
        wolf_y.append(wolves[i].gety())
        
    #Add agents and wolves to scatter plot.
    plt.imshow(environment)
    plt.scatter(agents_x,agents_y, c="blue", label = "Agents")    
    plt.scatter(wolf_x, wolf_y, c="red", label = "Wolves")
    #Include a legend.
    plt.legend(loc='upper left')
 
    
#Define 'gen_function' for the animation.   
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a
        a = a + 1
 



  
#Making a model in a new page.
root = tkinter.Tk()    
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#Define the command 'run' in the model menu to start the animation. 
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False) 
    canvas.draw()

#Make a menu in the new page.    
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label='Model', menu=model_menu)
model_menu.add_command(label="Run model", command=run)



tkinter.mainloop()





