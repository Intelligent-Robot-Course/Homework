from mdp import mdp
import numpy as np
from grid_map import grid_map
from mdp import mdp
from ir_sim.env import env_base
from pathlib import Path

map_matrix = np.load('map_matrix.npy')
reward_matrix = np.load('reward_matrix.npy')

env = env_base(world_width = 20, world_height = 20)
grid_map = grid_map(map_matrix=map_matrix, reward_matrix=reward_matrix)
mdp = mdp(grid_map)


# grid_map.show_map()

## please complete the function policy_iteration()
policy_value = mdp.value_iteration()
iterate_done = mdp.policy_iteration(policy_value) 

print(mdp.policy_matrix)










