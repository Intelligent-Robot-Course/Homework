import numpy as np
import math
import queue
from collections import namedtuple

class grid_graph:
    def __init__(self, grid_map_matrix=None, xy_reso=0.1):
        self.grid_map = grid_map_matrix
        self.node_tuple = namedtuple('graph_node', 'x, y, cost, parent') # each node type
        self.width = grid_map_matrix.shape[0]
        self.height = grid_map_matrix.shape[1]
        self.xy_reso = xy_reso
        self.obstacle_index = np.where(self.grid_map != 0) 
        self.xy_reso = xy_reso

    def neighbors(self, node):
        # x, y, cost, parent
        # the neighbor node of each node

        dirs = [[1, 0, 1], [0, 1, 1], [-1, 0, 1], [0, -1, 1],
                [-1, -1, math.sqrt(2)], [-1, 1, math.sqrt(2)], [1, -1, math.sqrt(2)], [1, 1, math.sqrt(2)] ]    # actions of the robot, x,y,cost

        node_neighbors = []

        for dir in dirs:
            new_x = dir[0] + node.x
            new_y = dir[1] + node.y
            new_cost = dir[2] + node.cost
            
            if new_x < self.width and new_y < self.height and new_x >= 0 and new_y >= 0:
                if self.grid_map[new_x, new_y] == 0 :
                    node_neighbor = self.node_tuple(new_x, new_y, new_cost, node)
                    node_neighbors.append(node_neighbor)
    
        return  node_neighbors

    def pose_to_index(self, pos_x, pos_y):

        index_x = int(pos_x / self.xy_reso)
        index_y = int(pos_y / self.xy_reso)

        return index_x, index_y

    def index_to_pose(self, index_x, index_y):
        
        pos_x = index_x * self.xy_reso
        pos_y = index_y * self.xy_reso

        return pos_x, pos_y

    def node_equal(self, node1, node2):
        return node1.x == node2.x and node1.y == node2.y

    
        