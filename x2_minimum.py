import numpy as np
import matplotlib.pyplot as plt


x1 = np.arange(-10.0,10.1,0.1)
y1 = np.power(x1, 2)
plt.plot(x1, y1, label = "line 1")

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('graph!')

# show a legend on the plot
#plt.legend()
plt.grid()
plt.show()