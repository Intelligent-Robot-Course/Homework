import numpy as np
from grid_map import grid_map
from ir_sim.env import env_base
from pathlib import Path
from reinforcement_learning import reinforcement_learning
import sys
from pathlib import Path

animation = False

# path set
cur_path = sys.path[0]
map_path = cur_path + '/map_matrix.npy'
reward_path = cur_path + '/reward_matrix.npy'
image_path = Path(__file__).parent / 'image' 
gif_path = Path(__file__).parent / 'gif'

# load map and reward matrix
map_matrix = np.load(map_path)
reward_matrix = np.load(reward_path)

# set environment and grid_map
env = env_base(world_width = 20, world_height = 20)
grid_map = grid_map(map_matrix=map_matrix, reward_matrix=reward_matrix, start_index=(2, 2))

# run Q learning algorithm
rl = reinforcement_learning(grid_map.state_space, grid_map.action_space, grid_map)
state_action_value = rl.Q_learning()

# policy performance test
cur_index = grid_map.start_index

for i in range(300):
    action_index = np.argmax( state_action_value[cur_index[0], cur_index[1], :])
    cur_index, _, _, done = grid_map.step(cur_index, action_index)
    grid_map.set_path(cur_index)
    grid_map.draw_map()

    if animation: env.save_fig(image_path, i)

    if done: 
        print('done')
        break

if animation: env.save_ani(image_path, gif_path, ani_name='Q_learning', keep_len=10)

grid_map.show_map()

# print(policy_value)





