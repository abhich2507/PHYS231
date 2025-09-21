import numpy as np

V = np.array([0,1,2,3,4,5,6,7,8,9,10],dtype=float) #voltage
I = np.array([0,0.8,1.5,1.6,2.5,2.7,3.2,3.9,4.5,5.0,5.5],dtype=float) #current

n = len(V)
sum_V = np.sum(V)
sum_I = np.sum(I)
sum_VI = np.sum(V*I)
sum_V2 = np.sum(V**2)

m = (n*sum_VI - sum_V*sum_I)/(n*sum_V2 - sum_V**2)
c = (sum_I - m*sum_V)/n

print(f"Slope {np.round(m,3)} ohm" )

import matplotlib.pyplot as plt

plt.scatter(V,I,color='blue')
plt.plot(V,m*V+c,color='red')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.savefig("plot_linear_regression.pdf")
