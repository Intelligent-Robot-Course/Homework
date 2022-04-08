import numpy as np 
import matplotlib.pylab as plt

def log_inv_sensor_model(z,c):
    if c > z :
        return np.log(0.6 / (1 - 0.6))
    return np.log(0.3 / (1 - 0.3))

measurements = [101, 82, 91, 112, 99, 151, 96, 85, 99, 105]
l_m = np.zeros(21)
m = 10*np.arange(21)

for z in measurements:
    for i in range(len(m)):
        if m[i] > z+20:
            continue

        l_m[i] += log_inv_sensor_model(z, m[i])
        
p_m = 1-1/(1+np.exp(l_m))
plt.plot(m,p_m)
