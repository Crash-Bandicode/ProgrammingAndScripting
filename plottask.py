# Program to plot square, cubed and quartic functions in given range (0, 4).

# Import numpy for arrays and matplotlib for plotting
# Give them abbreviated names for convenience.
import numpy as np
import matplotlib.pyplot as plt

# Create an array for given range
xpoints = np.array(range(0, 4))
# represent squared, cubed and quartic functions mathematically:
x2 = xpoints * xpoints
x3 = xpoints * xpoints * xpoints
x4 = xpoints * xpoints * xpoints * xpoints

#PLot each line using different styles & colors:
plt.plot(x2, linestyle = '--', color = 'blue', marker = 'o', label = "x**2")
plt.plot(x3, linestyle = '--', color = '#444444', marker = '.', label = "x**3")
plt.plot(x4, linestyle = '--', color = '#5a7d9a', marker = 'x', label = "x**4")
# Add legend
plt.legend()
# Add title:
plt.title("Power functions:")
# Add axis labels:
plt.xlabel("xaxis")
plt.ylabel("yaxis")
# Use a specific style:
plt.style.use('fivethirtyeight')
# show is unnecessary in Jupyter, but needed in python program to see plot.
plt.show