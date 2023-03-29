import numpy as np
from grid_map import grid_map
from ir_sim.env import EnvBase
from reinforcement_learning import reinforcement_learning
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--animation', action='store_true')
args = parser.parse_args()

# load map and reward matrix
map_matrix = np.load(sys.path[0] + '/map_matrix.npy')
reward_matrix = np.load(sys.path[0] + '/reward_matrix.npy')

# set environment and grid_map
env = EnvBase('question.yaml', save_ani=args.animation)
grid_map = grid_map(map_matrix, reward_matrix, (2, 2))

rl = reinforcement_learning(grid_map.state_space, grid_map.action_space, grid_map)
policy = rl.monte_carlo_es()

# policy performance test
cur_index = grid_map.start_index

for i in range(300):
    action_index = np.argmax( policy[cur_index[0], cur_index[1], :])
    cur_index, _, _, done = grid_map.step(cur_index, action_index)
    grid_map.set_path(cur_index)
    grid_map.draw_map()

    env.step()
    env.render()

    if done: 
        print('done')
        break

grid_map.show_map()


