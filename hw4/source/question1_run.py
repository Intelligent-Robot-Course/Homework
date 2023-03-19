from mdp import mdp
import numpy as np
from grid_map import grid_map
from mdp import mdp
from ir_sim.env import EnvBase
from pathlib import Path
import sys

cur_path = sys.path[0]

map_matrix = np.load(cur_path + '/map_matrix.npy')
reward_matrix = np.load(cur_path + '/reward_matrix.npy')

grid_map = grid_map(map_matrix=map_matrix, reward_matrix=reward_matrix)
mdp_policy = mdp(grid_map)

policy_value = mdp_policy.policy_evaluation()

print(policy_value)