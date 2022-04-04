import math
import numpy as np

'''

Defining the physics of the system. In our case, a 2D robot model
states = [x, y, theta], inputs = [v, omega]

x_next = x + v * cos(theta)
y_next = y + v * sin(theta)
theta_next = theta + omega

'''

def next_state(prev_state, ip):
    x_next = prev_state[0] + ip[0] * math.acos(prev_state[2])
    y_next = prev_state[1] + ip[0] * math.acos(prev_state[2])
    theta_next = prev_state[2] + ip[1]

    return np.transpose(np.array([x_next, y_next, theta_next]))