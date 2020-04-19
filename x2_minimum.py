import numpy as np
import matplotlib.pyplot as plt
import sympy as sympy
import random

def gradient_descent(X,Y,alpha):

    equation_expression = sympy.lambdify(X, Y , "numpy")  # convert Symbolic to calculative // Model of point wise calculation
    y_prime = Y.diff(X) #calculate derivative /Symbolic
    differntial_expresion = sympy.lambdify(X, y_prime) #convert Symbolic to calculative // Model of point wise calculation
    point = random.randint(-10, 10) # starting point
    x2 = [point]
    epsilon,count = 10,1
    while epsilon > 1e-20:
        old_point = point
        delta = differntial_expresion(point)  # compute expression for the given point
        point -= alpha*delta
        epsilon = np.abs(old_point-point)
        count+=1
        if count % 20 == 0:
            x2.append(point)

    x2 = np.array(x2 , dtype = float)
    y2 = equation_expression(x2)

    return x2,y2


if __name__ == "__main__":
    x1 = np.arange(-10.0,10.1,0.1)
    y1 = np.power(x1, 2)

    '''' Plot the function and its minimum '''
    fig1, ax1 = plt.subplots()
    ax1.plot(x1, y1, label = "line 1")
    # naming the x axis
    ax1.set_xlabel('x - axis')
    # naming the y axis
    ax1.set_ylabel('y - axis')
    # giving a title to my graph
    ax1.set_title('Plot function')
    ax1.grid()
    ax1.scatter([0], [0], label= "Minimum", color= "red",marker= "o", s=60)

    ''''  define equation and calculate local minima using gradient descent '''
    alpha = 0.01 # learning rate
    X = sympy.Symbol('x')
    Y = X**2
    x2,y2 = gradient_descent(X,Y,alpha)

    '''' Plot tts minimum '''
    plt.scatter(x2, y2, label= "stars", color= "green",marker= "*", s=40)
    print('local minimum is at [{} {}]'.format(round(x2[-1],6),round(y2[-1],6)))
    #print('delta x : ')
    delta_x = np.abs((np.roll(x2, -1)- x2)[0:len(x2)-1])
    #print(delta_x)
    #print('delta y : ')
    delta_y = np.abs((np.roll(y2, -1)- y2)[0:len(y2)-1])
    #print(delta_y)

    # Print delta_x and delta_y versus iteration
    fig2, (ax2, ax3) = plt.subplots(nrows=2, ncols=1) # two axes on figure
    ax2.plot(np.arange(len(delta_x)), delta_x, label = "line 1", color='blue', linestyle='dashed', linewidth = 2,
             marker='o', markerfacecolor='red', markersize=3)
    ax3.plot(np.arange(len(delta_y)), delta_y, label = "line 2", color='blue', linestyle='dashed', linewidth = 2,
             marker='o', markerfacecolor='red', markersize=3)
    ax2.grid()
    ax3.grid()

    # naming the x axis
    ax2.set_xlabel('Iteration')
    # naming the y axis
    ax2.set_ylabel('Delta x')

    # naming the x axis
    ax3.set_xlabel('Iteration')
    # naming the y axis
    ax3.set_ylabel('Delta y')

    plt.show()

