import numpy as np

class potential_fields:
    
    # Please complete these functions for question2, the arguments such as coefficient can be changed by your need. The return value should be a 2*1 matrix for robot to perform

    def uniform(self, vector=np.array([ [1], [0] ]), coefficient=1):
        # Please complete this function for question2
        pass

        return

    def perpendicular(self, line_obstacle, car_position, coefficient=1):
        # line_obstacle: [px1, py1, px2, py2]
        # Please complete this function for question2
        pass

        return 
    
    def attractive(self, goal_point, car_position, coefficient=1):
        # Please complete this function for question2
        pass
                    
        return

    def repulsive(self, obstacle_point, car_position, coefficient=1):
        # Please complete this function for question2
        
        return 

    def tangential(self, point, car_position, coefficient=1):
        # Please complete this function for question2
    
        return 

    def shortest_distance_point(self, v, w, p):
        # the minimum distance between line segment vw, and point p
        # v, w, p all are 2*1 matrix

        l2 = (w - v).T @ (w - v)
        if l2 == 0:
            return np.linalg.norm( p-v )

        t = max(0, min(1, (p - v).T @ (w - v) / l2 ))
        proj_point = v + t * (w-v)
        min_distance = np.linalg.norm( p-proj_point )
        
        return min_distance, proj_point, t

