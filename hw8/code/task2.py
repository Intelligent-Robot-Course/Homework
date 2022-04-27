import numpy as np 
import matplotlib.pylab as plt

measurements = [101, 82, 91, 112, 99, 151, 96, 85, 99, 105]
l_m = np.zeros(21)
m = 10*np.arange(21)

for z in measurements:
    i = z//10 
    if i+3<=len(l_m):
        l_m[0:i+1] = # todo 
        l_m[i+1:i+3] = # todo
    elif i+1<=len(l_m):
        l_m[0:i+1] = #todo
        l_m[i+1:] = #todo
    else:
        l_m = # todo

p_m = # todo
plt.plot(m,p_m)
