import matplotlib.pyplot as plt
import numpy as np

def plot_results(odometry, gps, perfect_world, kal_out):
    plt.figure(1)
    plt.plot(np.array(odometry)[:,0], np.array(odometry)[:,1], label='odometry')
    plt.plot(np.array(gps)[:,0], np.array(gps)[:,1], label='GPS')
    plt.plot(np.array(kal_out)[:,0], np.array(kal_out)[:,1], label='Filtered signal')
    plt.plot(np.array(perfect_world)[:,0], np.array(perfect_world)[:,1], label='Perfect World')
    plt.legend()
    plt.show()