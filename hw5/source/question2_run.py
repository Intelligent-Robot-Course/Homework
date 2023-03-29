import numpy as np
from grid_map import grid_map
from reinforcement_learning import reinforcement_learning
import sys
import argparse
from ir_sim.env import EnvBase

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--animation', action='store_true')
args = parser.parse_args()

# path set
map_path = sys.path[0] + '/map_matrix.npy'
reward_path = sys.path[0] + '/reward_matrix.npy'

# load map and reward matrix
map_matrix = np.load(map_path)
reward_matrix = np.load(reward_path)

# set environment and grid_map
env = EnvBase('question.yaml', save_ani=args.animation)
grid_map = grid_map(map_matrix=map_matrix, reward_matrix=reward_matrix, start_index=(2, 2))

rl = reinforcement_learning(grid_map.state_space, grid_map.action_space, grid_map)
state_action_value = rl.SARSA()

# policy performance test
cur_index = grid_map.start_index

for i in range(300):
    action_index = np.argmax( state_action_value[cur_index[0], cur_index[1], :])
    cur_index, _, _, done = grid_map.step(cur_index, action_index)
    grid_map.set_path(cur_index)
    grid_map.draw_map()

    env.step()
    env.render()

    if done: 
        print('done')
        break

grid_map.show_map()






