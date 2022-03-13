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

# animation
animation = True # whether generate the animation
image_path = Path(__file__).parent / 'image'  # image and animation path
gif_path = Path(__file__).parent / 'gif'

# grid_map.show_map()

## ---- Using value_iteration and policy_iteration to find the optimal path (hint: add for loop to make the interate_done be True)
policy_value = mdp.value_iteration()
interate_done = mdp.policy_iteration(policy_value)
## ----


# policy test
cur_index = grid_map.start_index
for i in range(300):
    
    action_index = np.argmax( mdp.policy_matrix[ cur_index[0], cur_index[1] ] )

    cur_index, _, _, done = grid_map.step(cur_index, action_index)

    print(cur_index)

    if done: 
        print('done')
        break

    grid_map.set_path(cur_index)
    grid_map.draw_map()

    if animation: env.save_fig(image_path, i) 

if animation: env.save_ani(image_path, gif_path, ani_name='mdp', keep_len=10)

grid_map.show_map()









