import math
import matplotlib.pyplot as plt
import numpy as np

def spread (Inf, Rec, Total_P, Beta, Gamma, Delta_T, Iterations):
    
    Data_Set_Sus = []
    Data_Set_Inf = []
    Data_Set_Rec = []
    Time_Set = []
    Sus = Total_P-Inf-Rec
    
    for i in range (Iterations):
        Delta_Sus = (- Beta*Sus*Inf/Total_P)*Delta_T
        #print(int(round(Sus)))
        Delta_Inf = ((Beta*Sus*Inf/Total_P)-(Inf*Gamma))*Delta_T
        #print(int(round(Inf)))
        Delta_Rec = (Inf*Gamma)*Delta_T
        #print(int(round(Rec)))
        
        Sus = Delta_Sus+Sus
        Inf = Delta_Inf+Inf
        Rec = Delta_Rec+Rec
        
        Data_Set_Sus.append(Sus)
        Data_Set_Inf.append(Inf)
        Data_Set_Rec.append(Rec)
        Time_Set.append(i)
        #print()

    xpoint_Sus = np.array(Data_Set_Sus)
    xpoint_Inf = np.array(Data_Set_Inf)
    xpoint_Rec = np.array(Data_Set_Rec)
    
    plt.plot(Time_Set, xpoint_Sus, label="Susceptible", color='#14bd0b')#Plots Susceptible and time/Green
    plt.plot(Time_Set, xpoint_Inf, label="Infected", color='#e8d209')#Plots Infected and time/Yellow
    plt.plot(Time_Set, xpoint_Rec, label="Recovered", color='#bd110b')#Plots Recovered and time/Red
    plt.xlabel('Time(Days)')
    plt.ylabel('Population')
    plt.legend()
    plt.show()
    
    return(Data_Set_Sus, Data_Set_Inf, Data_Set_Rec, Time_Set)

def main():
    result=spread(1, 0, 10000, 0.7, 0.3, 0.5, 100)
    print(result)
main()
