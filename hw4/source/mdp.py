import numpy as np

class mdp:
    def __init__(self, grid_map, state_trans_prob=1, discount_factor=0.95):

        # five parts: state, action, transition probability, reward,  
        self.state_space = grid_map.state_space # width and height
        self.action_space = grid_map.action_space # up, down, left, right

        self.state_trans_prob = state_trans_prob 
        self.gamma = discount_factor # the discount_factor to calculate the action value

        self.policy_matrix = np.ones((grid_map.state_space[0], grid_map.state_space[1], len(self.action_space))) / len(self.action_space)  # policy matrix, include the probability of each action, the init probabilities are equal 
        self.grid_map = grid_map

    def policy_iteration(self, policy_value):

        ## please complete this function for question2 by 1. calculating the action value 2. finding the action index with maximum value

        # (1) The policy iteration under current policy value
        # (2) In each state index, the action value will be calculated depend on current policy value and action reward (the formula in the lecture)
        # (3) In each state index, find the action with maximum value calculated by previous line (2)., check whether it is equal to the old action
        # (4) If all the actions are stable, the policy iteration is done.

        interate_done = True

        for i in range(self.state_space[0]):
            for j in range (self.state_space[1]):

                old_action_index = np.argmax(self.policy_matrix[i, j])
                action_value_list = []
                state_index = (i, j)

                for action_index, action in enumerate(self.action_space):
                    next_state, reward, state_prob, done = self.grid_map.step(state_index, action_index)

                    '''
                    calculate the action value
                    
                    action_value = ?
                    '''

                    action_value_list.append(action_value)

                '''
                find the action index with maximum action value
                action_index = ?
                '''

                self.policy_matrix[i, j, :] = 0
                self.policy_matrix[i, j, action_index] = 1 

                if action_index != old_action_index:
                    interate_done = False

        return interate_done


    def policy_evaluation(self, threshold=0.01):
        ## please complete this function for question1 by 1. calculating the policy value 2. completing the judgement condition indicator delta
        # (1) The value iteration under current policy matrix
        # (2) in each state index, the policy value will be calculated (cumulative reward and value)
        # (3) This iteration will be done if all the values are stable (Compare the maximum difference value with the threshold to judge)

        policy_value = np.zeros(self.state_space[0:2])

        while True:
            delta = 0
            
            for i in range (self.state_space[0]):
                for j in range (self.state_space[1]):
                    
                    old_value = policy_value[i, j]
                    
                    state_index = (i, j)
                    temp_action_value = 0

                    for action_index, action_prob in enumerate(self.policy_matrix[i, j]): 
                        next_state_index, reward, state_prob, done = self.grid_map.step( state_index, action_index)

                        '''
                        calculate the temp_action_value (policy value) 
                        temp_action_value = ?
                        '''
                        
                    policy_value[i, j] = temp_action_value

                    '''
                    complete the judgement condition indicator  (Compare the maximum difference value with the threshold to judge)
                    delta = ?
                    '''
                   
            if delta < threshold:
                break

        return policy_value


    def value_iteration(self, threshold=0.01):
        # complete the value iteration algorithm for question3
        # value iteration: refer to the value iteration pesudo code in the lecture. 
        policy_value = np.zeros((self.state_space[0], self.state_space[1]))
        iteration_num = 0

        while True:
            delta = 0
            for i in range(self.state_space[0]):
                for j in range(self.state_space[1]):
                    old_value = policy_value[i, j]
                    temp_action_value = []
                    state_index = (i, j)
                    
                    '''
                    update the policy_value
                    policy_value = ?
                    '''

                    '''
                    complete the judgement condition indicator delta:
                    delta = ?
                    '''

            iteration_num += 1
            print("iteration_num:", iteration_num)

            if delta < threshold:
                print('value iteration done')
                break
        
        return policy_value

    def get_policy_action(self, state_index):
        # get the action based on the value iteration algorithm

        return np.argmax( mdp.policy_matrix[ state_index[0], state_index[1] ] )

    def get_value_action(self, policy_value, state_index):
        # get the action based on the value iteration algorithm (the index of maximum action value)    
        # complete this function for question3

        temp_action_value = []  # list of action values

        '''
        caculate the value of each action
        temp_action_value = ?
        '''

        return np.argmax(temp_action_value)