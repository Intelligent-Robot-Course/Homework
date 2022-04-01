import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

class grid_map:
    def __init__(self, map_matrix=None, reward_matrix=None, start_index=(2, 2), goal_index=(16, 16), reward_bound=-5, reward_collision=-0.1):
        self.map_matrix = map_matrix

        self.state_space = map_matrix.shape[0:2]
        self.action_space = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
        self.reward_matrix = reward_matrix
        self.reward_bound = reward_bound
        self.reward_collision = reward_collision

        self.start_index = start_index
        self.goal_index = goal_index

    def step(self, cur_state_index, action_index, state_trans_prob=1):
        
        others = (1 - state_trans_prob) / 3
        action_prob_list = [others, others, others, others]
        action_prob_list[action_index] = state_trans_prob

        real_action_index = np.random.choice([0, 1, 2, 3], p=action_prob_list)
        action_prob = action_prob_list[real_action_index]

        action = self.action_space[action_index]
        done = False

        next_x = cur_state_index[0] + action[0]
        next_y = cur_state_index[1] + action[1]

        if next_x > self.state_space[0] - 1:
            next_x = self.state_space[0] - 1
            reward = self.reward_bound
            done = True
        
        elif next_x < 0:
            next_x = 0
            reward = self.reward_bound
            done = True
        
        elif next_y > self.state_space[1] - 1:
            next_y = self.state_space[1] - 1
            reward = self.reward_bound 
            done = True

        elif next_y < 0:
            next_y = 0
            reward = self.reward_bound 
            done = True
        else:        
            reward = self.reward_matrix[next_x, next_y]

            ## Extra Credit 
            # ----------------------------------------------------------------
            # You can add the heuristic reward here, such as the dwa reward, astar reward, or distance-to-goal reward learned from previous lectures to achieve a regular policy as you expected (such as keeping moving away from the obstacle.). In addition, if the self.reward_matrix[next_x, next_y] == reward_collision, there should the obstacle grid index.
            pass
            # example: reward = self.reward_matrix[next_x, next_y] + heuristic_reward
            # ----------------------------------------------------------------
            done = False

        if next_x == self.goal_index[0] and next_y == self.goal_index[1]:
            done = True
    
        next_state = (next_x, next_y)

        return next_state, reward, action_prob, done

    def set_path(self, index):
        self.map_matrix[index[0], index[1], :] = 255

    def show_map(self):
        plt.imshow(self.map_matrix)
        plt.show()

    def draw_map(self, time=0.01):
        plt.imshow(self.map_matrix)
        plt.pause(time) 