import numpy as np 
import matplotlib.pylab as plt

measurements = [101, 82, 91, 112, 99, 151, 96, 85, 99, 105]
l_m = np.zeros(21)
m = 10*np.arange(21)

for z in measurements:
    i = z//10 
    if i+3<=len(l_m):
        l_m[0:i+1] = l_m[0:i+1] + np.log(0.3/0.7) 
        l_m[i+1:i+3] = l_m[i+1:i+3] + np.log(0.6/0.4)
    elif i+1<=len(l_m):
        l_m[0:i+1] = l_m[0:i+1] + np.log(0.3/0.7) 
        l_m[i+1:] = l_m[i+1:] + np.log(0.6/0.4)
    else:
        l_m = l_m + np.log(0.3/0.7) 

p_m = 1-1/(1+np.exp(l_m))
plt.plot(m,p_m)
