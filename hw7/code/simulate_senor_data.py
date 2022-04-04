import numpy as np
from state_evolution import next_state

def mock_odo_gps_data(state, ip):
    odo = []
    gps = []
    perfect_world = []

    for _ in range(50):
        state = next_state(state, ip) # state update
        perfect_world.append(state)
        odo.append(state + np.random.normal([0,0,0], [0.1, 0.1, 0.001], 3)) # odo estimate is bad
        gps.append(state + np.random.normal([0,0,0], [0.05, 0.05, 0], 3)) # gps estimate is much better

    return odo, gps, perfect_world

def generate_cirular_traj_ips():
    print("Test")