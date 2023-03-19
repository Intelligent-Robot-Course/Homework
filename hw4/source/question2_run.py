from mdp import mdp
import numpy as np
from grid_map import grid_map
from mdp import mdp
from pathlib import Path
import sys
from ir_sim.env import EnvBase
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--animation', action='store_true')
args = parser.parse_args()

# initialize the map
cur_path = sys.path[0]

map_matrix = np.load(cur_path + '/map_matrix.npy')
reward_matrix = np.load(cur_path + '/reward_matrix.npy')

grid_map = grid_map(map_matrix=map_matrix, reward_matrix=reward_matrix)
mdp = mdp(grid_map)

env = EnvBase('question.yaml', save_ani=args.animation)

# update the policy
for i in range(300):
    policy_value = mdp.policy_evaluation()
    interate_done = mdp.policy_iteration(policy_value)

    print('iterator', i)

    if interate_done:
        print('mdp iteration done')
        break

# policy test
cur_index = grid_map.start_index

for i in range(300):
    
    action_index = np.argmax( mdp.policy_matrix[ cur_index[0], cur_index[1] ] )

    cur_index, _, _, done = grid_map.step(cur_index, action_index)

    print('current index:', cur_index)

    if done: 
        print('Done with total steps: ', i)
        break
    
    env.step()
    
    grid_map.set_path(cur_index)
    grid_map.draw_map()

    env.render()

env.end(ani_name = 'policy_iteration', ani_kwargs={'subrectangles': True})










