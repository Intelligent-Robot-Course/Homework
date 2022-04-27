import numpy as np 
import matplotlib.pylab as plt

def log_inv_sensor_model(z,c):
    if c > z :
        return #Todo
    return #Todo

measurements = [101, 82, 91, 112, 99, 151, 96, 85, 99, 105]
l_m = np.zeros(21)
m = 10*np.arange(21)

for z in measurements:
    for i in range(len(m)):
        if m[i] > z+20:
            continue

        l_m[i] += log_inv_sensor_model(z, m[i])
        
p_m = # Todo
plt.plot(m,p_m)
plt.show()
