from re import S
import numpy as np
from math import sqrt, inf


class dynamic_window_approach:
    def __init__(self, vx_range, vy_range, accelerate=0.5, time_interval=0.1, predict_time=1, graph=None):

        self.vx_range = vx_range
        self.vy_range = vy_range
        self.acce = accelerate
        self.time_int = time_interval
        self.graph = graph
        self.pre_time = predict_time
        
    def cal_vel(self, cur_pose, goal_pose, current_vel, v_gain=1, g_gain=1, o_gain=1, a_gain=1, astar_path=None):
        
        # v_gain, g_gain, o_gain, a_gain: the gain for the velocity cost, goal cost, obstacle cost, astar cost, you should modify the gain for you own task.

        cost_list = []
        vel_pair_list = []
        pre_traj_list = []

        # Calculate the admissable velocity
        min_vx, max_vx, min_vy, max_vy = self.search_space(current_vel)

        for vx in np.arange(min_vx, max_vx, 0.1):
            for vy in np.arange(min_vy, max_vy, 0.1):
                pre_traj = self.predict_traj(cur_pose, vx, vy) # predict the trajectory under current velocity
                cost = self.cost_function(goal_pose, vx, vy, pre_traj, vel_cost_gain=v_gain, goal_cost_gain=g_gain, obstacle_cost_gain=o_gain)  # the object(cost) function for you to complete. you should complete this function for the homework question2

                if astar_path is not None:
                    # complete the astar_cost function for question3
                    astar_cost = self.astar_cost(pre_traj, astar_path)
                    cost += a_gain * astar_cost

                cost_list.append(cost)
                vel_pair_list.append([vx, vy])
                pre_traj_list.append(pre_traj)

        min_cost_index = cost_list.index(min(cost_list))
        dwa_vel = vel_pair_list[min_cost_index]
        dwa_traj = pre_traj_list[min_cost_index]

        return np.array(dwa_vel), dwa_traj

    def search_space(self, current_vel):
 
        min_vx = max( self.vx_range[0], current_vel[0] - self.time_int * self.acce)
        max_vx = min( self.vx_range[1], current_vel[0] + self.time_int * self.acce)

        min_vy = max( self.vy_range[0], current_vel[1] - self.time_int * self.acce)
        max_vy = min( self.vy_range[1], current_vel[1] + self.time_int * self.acce)

        return min_vx, max_vx, min_vy, max_vy

    def predict_traj(self, cur_pose, vx, vy):
        # predict the trajectory of current velocity
        
        pre_traj = []
        cur_vel = np.array( [ [vx], [vy] ] ) 
        # print(cur_vel)
        i = 0
        while i < self.pre_time:
            next_pos = cur_pose + cur_vel * self.time_int
            i = i + self.time_int
            pre_traj.append(next_pos)
            cur_pose = next_pos
        
        return pre_traj

    def cost_function(self, goal_pose, vx, vy, pre_traj, vel_cost_gain=1, goal_cost_gain=1, obstacle_cost_gain=1):
        # Calculate the cost of current pair of vx vy
        # you should complete the function for question2. (HintL the summary cost of the following functions)
        # The cost include three parts: (1) the cost related to velocity, the maximize velocity is better, 10%
        # (2) cost realted to the goal, the closer position to the goal is better, 30%
        # (3) cost related to the obstacle, move away from the obstacle is better, 40%

        print('you should complete the cost function')
        pass
        # return cost

    def vel_cost(self, vx, vy):
        # you should complete the function for question2
        # the cost function about the velocity cost (hint: maximize the velocity is better, you can use the norm of this velocity)
        pass

    def cost_to_goal(self, pre_traj, goal):
        # you should complete the function for question2
        # the closer position to the goal is better (hint: use the position of the final point in the pre_traj to judge. )

        pass
        

    def cost_to_obstacle(self, pre_traj):
        # you should complete the function for question2
        # the cost to the avoid the obstacles, move away from the obstacle is better 
        # (hint: the minimum distance between the predicted trajectory and obstacle in grid map, 
        # you can use the below function point_to_obstalce to calculate the distance with each point)
        pass

        
    def point_to_obstalce(self, point):
        # the distance between current point and the obstacle depending on the grid map 

        index_x, index_y = self.graph.pose_to_index(point[0, 0], point[1, 0])

        temp_x = (self.graph.obstacle_index[0] - index_x)
        temp_y = (self.graph.obstacle_index[1] - index_y) 

        dis_list = [ sqrt(x**2 + y**2) for x, y in zip(temp_x, temp_y)]
        distance = min(dis_list) * self.graph.xy_reso

        return distance

    def astar_cost(self, pre_traj, astar_path):
        # you should complete the function for question3
        # related to the distance between the positions in pre_traj and points in astar_path, 20%
        print('you should complete the astar cost function')
        pass
        

        

        

        




