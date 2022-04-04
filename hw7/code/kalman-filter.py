import math
import numpy as np
import matplotlib.pyplot as plt

from state_evolution import next_state
from simulate_senor_data import mock_odo_gps_data
from plot_util import plot_results

class KalmanFilter:
    def __init__(self, _state, _ip):
        '''
        The matrices of Kalman filter:
        System:
        next_state = A*prev_state + B*input + SigmaState
        output = H*next+state + SigmaOutput
        '''
        self.state = _state
        self.ip = _ip
        self.output = None
        self.A = None
        self.B = None
        self.H = None
        self.SigmaState=None
        self.SigmaOutput = None
        self.P = None
    
    def set_kalman_matrices(self, A, B, H, P, SigmaState, SigmaOutput):
        self.A = A
        self.B = B
        self.H = H
        self.SigmaState= SigmaState
        self.SigmaOutput = SigmaOutput
        self.P = P
    
    def predict(self, state):
        self.state = next_state(self.state, self.ip) + np.random.normal([1,1,0], [0.4, 0.4, 0.001], 3)
        self.P = 
        self.output =
        return self.state

    def update(self, measurement):
        Kalman_gain = 
        gain_factor = 
        self.state = 
        self.P = 
        self.output = 

        return self.state, self.output 

if __name__ == "__main__":

    state = np.transpose(np.array([0,0,0.002]))
    ip = np.array([1,0.01])
    output = None
    
    # Covariance matrices
    sigmax = 1
    sigmay = 1
    sigmatheta = 0.1

    # Tuning parameters
    P = np.diag([sigmax**2, sigmay**2, sigmatheta**2])
    SigmaState = np.diag([0.01, 0.01, 0.007]) #uncertainity in state
    SigmaOutput = np.diag([0.1,0.1,0]) #uncertainity in measurement - How much you believe in ur measurement

    odometry, gps, perfect_world = mock_odo_gps_data(state, ip)
    kal_out = []
    odo_out = []

    kal_filter = KalmanFilter(state, ip)

    for idx, gps_data in enumerate(gps):
        # from the physics of the system we derive A, B, H
        A = np.array(np.identity(3))
        B = np.array([[math.acos(state[2]), 0], [math.asin(state[2]), 0], [0,1]])
        H = np.array(np.identity(3))
        H[2][2] = 0

        kal_filter.set_kalman_matrices(A,B,H,P,SigmaState,SigmaOutput)
        odo_out.append(kal_filter.predict(state))
        state, output = kal_filter.update(gps_data)
        kal_out.append(output)

    plot_results(odo_out, gps, perfect_world, kal_out)
