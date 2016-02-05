#The following code shows how the Python numpy and scipy libraries
#can be used to solve a differential equation using the odeint command.
#This is an effective tool for solving ordinary differential equations.
#The example in this case a differential equation for a damped harmonic oscillator.



#Numeric Python library
import numpy as np




# Plotting library Pyplot from matplot lib
import matplotlib.pyplot as plt



#Bring in the odeint module from the scipy library.
#This is an integration tool for ordinary differential equations.
from scipy.integrate import odeint




#Define the function that describes the differential equation
#of a damped harmonic oscillator.  Inputs include the initial conditions,
#horizontal axis (usually time or x) and equation parameters or constants.
def myModel(init, t, params):


    #Unpack the current values of y as initial values.
    x_init, x_dot_init = init


    #Parameters for the differential equation.
    b,k = params


    #Write out the differential equation in the function.  Need to write out the equations
    #with the initial conditions.
    x_dot = x_dot_init
    x_double_dot = -b*x_dot_init -k*x_init


    #Return the differential equation.  The ode solver will integrate both of these up one level.
    return x_dot, x_double_dot





#Parameters to be used for the differential equation.
b=0.05
k=0.05




#Bundle the parameters for the ODE solver.
#Can also bundle initial conditions into a list for the ODE solver
#if there is more than one initial condition needed.
params = [b,k]



#Time range needed for the function.
t = np.linspace(0, 500, 10000)



#Initial values.  The initial values need to match the type of quantity that is being solved
#for by the ode solver.  In this, an inital value of displacement and velocity are provided.
init = [0.5, -0.2]



#Solve the differential equation using the odeint function, with a function
#call to the myModel function.  The parameters can be passed into the solver
#as a tuple.  Note that to define a tuple, normal brackets need to be used
#and a comma is required after the parameter list.  Tuples are immutable
#and cannot be changed, unlike lists.  Lists uses square brackets.
#The ode solver basically integrates whatever is put into it with the equation model function.
#It can do more than one integration at the same time, depending on what the function returns.
state = odeint(myModel, init, t, args = (params,))



#Open up a figure for plotting the solution to the equation of displacement vs. time.
plt.figure(1)



#Plot the solution to the differential equation.  In this case, the first column of the solution is plotted,
#which is displacement.
plt.plot(t, state[:,0], '-', lw = 2)



#Change the x limit (horizontal limit) for the plot to a smaller number.
plt.xlim(0,300)



#Label the x axis.
plt.xlabel('Time(s)')



#Label the y axis
plt.ylabel('Position(cm)')



#Title of the plot
plt.title('ODE solver Solution')



#Show the plot
plt.show()








#Open up a figure for plotting displacement vs. velocity.
plt.figure(2)



#Plot the solution to the differential equation.  In this case, the second and first columns are plotted with
#respect to each other, which is displacement vs. velocity.
plt.plot(state[:,0], state[:,1], '-', lw = 2)



#Show the plot
plt.show()