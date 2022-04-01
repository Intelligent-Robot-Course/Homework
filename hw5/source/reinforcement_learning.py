import numpy as np
from math import inf
# different from MDP: Solve MDP when reward/transition models are unknown (no knowledge of MDP transitions / rewards.)

class reinforcement_learning:
    def __init__(self, state_space, action_space, grid_map, discount_factor=0.95, Epsilon=0.2):
        # state_space: (width, height)
        self.gamma = discount_factor
        self.state_space = state_space
        self.action_space = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
        self.action_index = np.arange(len(self.action_space))
        self.grid_map = grid_map
        self.Epsilon = Epsilon

    def monte_carlo_es(self, epi_num = 10000, visit = 'first'):
        # reference: textbook, Reinforcement Learning: An Introduction, Monte Carlo ES (Exploring Starts)

        # do not know the state transitions
        # agent learns from sampled experience
        # Only can be used in episodic problems
        policy_matrix = np.ones((self.state_space[0], self.state_space[1], len(self.action_space))) / len(self.action_space)  # initialize the policy with prob 0.25 for all actions
        state_action_value = np.zeros((self.state_space[0], self.state_space[1], len(self.action_space)))  # initialize the state action value
        state_action_returns_num = np.zeros((self.state_space[0], self.state_space[1], len(self.action_space)))  # initialize the state action explore number

        for i in range(epi_num):
            print('episode number percent {:.2%}'.format(i/epi_num))
            state_action_return_list, state_action_value, state_action_returns_num = self.state_action_evaluation(policy_matrix, state_action_value, state_action_returns_num, visit)
            policy_matrix = self.policy_update(policy_matrix, state_action_return_list, state_action_value)          

        return policy_matrix
    
    def state_action_evaluation(self, policy, state_action_value, state_action_returns_num, visit='first'):

        # random state action pair
        start_state = np.random.randint(low=[0, 0], high=self.state_space, size=2)
        start_action = np.random.choice([0, 1, 2, 3])

        state_action_set = set()
        
        state_action_return_list = self.episode_state_action_return(policy, start_state, start_action)
        
        # calculate the state_action_value depend current episode
        ## ----------------------------------------------------------------
        if visit == 'first':
            #you should complement this part to complete the state_action_evaluation for monte_carlo_es
            pass
            


                


        ## ----------------------------------------------------------------

        return state_action_return_list, state_action_value, state_action_returns_num

    def policy_update(self, policy_matrix, state_action_return_list, state_action_value):

        for state_action, return_G in state_action_return_list:
            state = state_action[0:2]
            action_value = state_action_value[state[0], state[1]]

            max_value_index = np.argwhere(action_value == np.max(action_value))
            action_index = np.random.choice(np.squeeze(max_value_index, axis=1))

            # deterministic policy
            policy_matrix[state[0], state[1], :] = 0.0
            policy_matrix[state[0], state[1], action_index] = 1.0

        return policy_matrix

    def episode_state_action_return(self, policy, start_state, start_action, episode_len=100):
        cur_state = (start_state[0], start_state[1])
        cur_action = start_action
        state_action_list = []
        visit_state = set()

        for i in range(episode_len):
            
            next_state, reward, _, done = self.grid_map.step(cur_state, cur_action)

            # prevent the dilemma
            if next_state in visit_state:
                reward = -0.1
            
            state_action_list.append( (cur_state, cur_action, reward) )
            visit_state.add(cur_state)

            # epsilon greedy
            p = np.random.rand()
            if p < self.Epsilon:
                cur_action = np.random.choice( [0, 1, 2, 3])
            else:
                prob = policy[cur_state[0], cur_state[1], :]
                cur_action = np.random.choice( [0, 1, 2, 3], p=prob)

            cur_state = next_state
               
            if done: 
                break

        state_action_returns = []
        G = 0    

        ## ----------------------------------------------------------------
        state_action_list.reverse()
        for state, action, reward in state_action_list:
            #you should complement this part to calculate the state_action_returns depending on the state_action_list for monte_carlo_es


            pass
        state_action_returns.reverse()
        ## ----------------------------------------------------------------

        return state_action_returns

    def SARSA(self, epi_num=10000, step_size=0.4, max_ep_len=100):

        state_action_value = np.zeros((self.state_space[0], self.state_space[1], len(self.action_space)))  # initialize the state action value

        for i in range(epi_num):
            print('episode number percent {:.2%}'.format(i/epi_num))
            cur_state = np.random.randint(low=[0, 0], high=self.state_space, size=2) # random init start state
            cur_action = self.action_choose_greedy(state_action_value[cur_state[0], cur_state[1], :])
            
            # each episode
            for j in range(max_ep_len):

                # epsilon greedy
                next_state, reward, _, done = self.grid_map.step(cur_state, cur_action)
                next_action = self.action_choose_greedy(state_action_value[next_state[0], next_state[1], :])
                
                ## ----------------------------------------------------------------
                # You should complement this part to complete the Q value update function (refer to the Pseudocode)
                pass





                ## ----------------------------------------------------------------    
                cur_state = next_state
                cur_action = next_action

                if done:
                    break

        return state_action_value

    def Q_learning(self, epi_num=10000, step_size=0.4, max_ep_len=100):

        state_action_value = np.zeros((self.state_space[0], self.state_space[1], len(self.action_space)))  # initialize the state action value

        for i in range(epi_num):
            print('episode number percent {:.2%}'.format(i/epi_num))
            cur_state = np.random.randint(low=[0, 0], high=self.state_space, size=2) # random init start state
            cur_action = self.action_choose_greedy(state_action_value[cur_state[0], cur_state[1], :])
            
            # each episode
            for j in range(max_ep_len):
                # epsilon greedy
                next_state, reward, _, done = self.grid_map.step(cur_state, cur_action)
                next_action = self.action_choose_greedy(state_action_value[next_state[0], next_state[1], :])

                ## ----------------------------------------------------------------
                # You should complement this part to complete the Q value update function (refer to the Pseudocode)
                pass





                ## ----------------------------------------------------------------    
                
                cur_state = next_state
                cur_action = next_action

                if done:
                    break

        return state_action_value

    def action_choose_greedy(self, action_value):

        p = np.random.rand()

        if  p < self.Epsilon:
            action = np.random.choice(self.action_index)
        else:
            max_value_index = np.argwhere(action_value == np.max(action_value))
            action = np.random.choice(np.squeeze(max_value_index, axis=1))

        return action


    

    
    # def 