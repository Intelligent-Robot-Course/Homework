import numpy as np
import queue
from math import sqrt

class Astar:
    def __init__(self):
        # graph node: x, y, cost, parent
        self.cur_vis = []   # current visited node list
        self.next_vis = []  # next visit node list

    def find_path(self, graph, start_pos, goal_pos):
        
        print('start to Astar search') 

        frontier = queue.PriorityQueue()  # priority queue for algorithm to explore current points.
        frontier.put((0, start_pos))  # put the priority and position

        self.cur_vis.append([start_pos.x, start_pos.y])
        self.next_vis.append([start_pos.x, start_pos.y])
        
        cost_so_far = np.zeros((graph.width, graph.height)) # cost matrix from start point to this point
        final_node = None

        while not frontier.empty():
            print('you should complete this part to find the path')
            # please complete this part for the homework question1 
            pass

        print('search done')

        return final_node, self.cur_vis

    def heuristic(self, node1, node2, coefficient=1):
        # please complete the heuristic function for the homework question1 
        print('You should complete the heuristic function')
        pass
        

    def generate_path(self, final_node):

        path = [ [final_node.x, final_node.y] ]
        
        while final_node.parent is not None:
            path.append( [final_node.parent.x, final_node.parent.y] )
            final_node = final_node.parent
        
        return path





    

