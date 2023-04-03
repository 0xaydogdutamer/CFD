# HOMEWORK 2 TAMER AYDOGDU 030180060 Q1-A

import numpy as np #importing numpy library for matrix operations
import matplotlib.pyplot as plt #importing matplotlib library for plotting graph for our data
import math #importing math library for mathematical operations

L = 2 #thickness 2 cm
k=2.47 #thermal conductivity for aluminum W/cm.K
rho=0.0027 #density of aluminum kg/cm^3
cp=900 #specific heat capacity of aluminum J/Kg*C
alpha = k/(rho*cp) #thermal diffusivity of aluminum cm^2/s
dx = 0.125   # dx = h -- xdirection step
dt = 0.005 # y direction time step
x = np.arange(0,2+dx,dx) #creating matrix 0 to 2 by incrementing with dx
t = np.arange(0,0.2+dt,dt) #creating matrix 0 to 2 by incrementing with dt

def isthisStable(alpha,dx,dt): #for controlling stable condition
    if (alpha*dt)/dx**2 <= 0.5: #condition
        return "it is stable"
    else:
        return 'it is NOT stable'

print(isthisStable(alpha,dx,dt))#print it is stable or not

len_x = len(x) #obtain length of x matrix
len_t = len(t) #obtain length of t matrix

bc_1 = 20 #first boundary condition = 20 degree
bc_2 = 20 #second boundary condition = 20 degree
ic = np.arange(0,len_x, 1) #create initial condition matrix  9x1 size
for i in range(0,len_x, 1):# for loop to assign ic values
    if x[i] < L/2:
        ic[i] = 20 + 80 * (x[i]/L) #initial condition
    elif x[i] >= L/2:
        ic[i] = 20 + 80 * (1 - x[i]/L) #initial condition

temp = np.zeros((len_x,len_t)) #creating temperature matrix (len_x X len_t) size
temp[0, : ] = bc_1 #fill start of the temp matrix with bc1
temp[-1,: ] = bc_2 #fill end of the temp matrix with bc2
temp[:,0] =ic #fill first column of the temp matrix with ic
R = (alpha*dt)/dx**2 #factor of rearranged form of given equation

for j in range(1,len_t):
    for i in range(1, len_x-1):
        temp[i,j] = R*temp[i+1,j-1] + (1-2*R)*temp[i,j-1] + R*temp[i-1,j-1] #rearranged form for FTCS


R= np.linspace(1,0,len_t)
B= np.linspace(0,1,len_t)
G = 0
for j in range(len_t):
    plt.plot(x,temp[:,j], color = [R[j],G,B[j]])

plt.legend([f't = {time} s'for time in t])
plt.xlabel("Distance [cm]")
plt.ylabel("Temperature")
plt.show()


