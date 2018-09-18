import numpy as np
import matplotlib.pyplot as plt

dataSet=np.loadtxt("ex2data1.txt",delimiter=',')
X=dataSet[:,0]
y=dataSet[:,1]

print(X)


#Plotting data
plt.plot(X, y, "b.")
plt.axis([-3, 3, 0, 10])
plt.show()