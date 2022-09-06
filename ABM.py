from collections import Counter
import random
import pandas as pd

class Agent:
    def __init__(self, state):
        self.state = state
        self.inftick = 0

    def contact(self, other):
        if (self.state == 's' and other.state == 'i') or (self.state == 'i' and other.state == 's'):
            self.state = 'i'
            self.inftick = 0

    def fight(self):
        if self.state == 'i':
            for x in range (10):
                self.inftick += 1
            if self.inftick >= 7:
                self.state = 'r'
                self.inftick = None

daily_rate = []

def population(listofagents, population):
    for x in range(population):
        a = Agent('s')#creates 99 instances of class agent with attribute state s
        listofagents.append(a)#agent stored in listofagents
        stateofagents.append(a.state)#agent state stored in stateofagents
    a = Agent('i')#creates an isntance of class agent with attribute state i
    listofagents.append(a)#agent stored in listofagents
    stateofagents.append(a)#agent state stored in stateofagents
    #print(stateofagents)#Testing purpose
    return listofagents

def total_SIR_count(listofagent):
    #print(Counter(stateofagents))#Testing purpose
    return listofagents

def spread(listofagents):
    for x in range (10):#Loops the spead mechanism 20 times 
        n1 = random.choice(listofagents)#picks one random agent and stores them as n1
        n2 = random.choice(listofagents)#picks one random agent and stores them as n2
        #print(n1, n2)#Testing purpose
        Agent.contact(n1, n2)#n1 and n2 are put throught the contact method
    n3 = random.choice(listofagents)#picks one random agent and stores them as n3
    if (n3.state == 'i'):
        Agent.fight(n3)# if state of n3 = i the Agent undergoes the fight method
    return listofagents

def continue_spread(listofagents, runs, population):
    while runs > 0: 
        spread_list = []
        spread(listofagents)#calls the spread function
        for x in range (population):#goes through all element
            spread_list.append(listofagents[x].state)#append state of agents into spread_list
        a = Counter(spread_list)#Count elemnts in spread_list and stores it as a  
        daily_rate.append(a)#stores value in daily_rate list
        runs -= 1

test_data_list = []

for x in range(10):
    listofagents = []
    stateofagents = []
    population(listofagents, 99)
    total_SIR_count(listofagents)
    spread(listofagents)
    for y in range(100):
        listofagents[y].state
        total_SIR_count
    continue_spread(listofagents, 500, 99)

data_1 = pd.DataFrame(daily_rate)
data_1.to_csv('test_data_1.csv')
