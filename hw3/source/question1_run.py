from ir_sim.env import EnvBase
from Astar import Astar
from grid_graph import grid_graph
import argparse

parser = argparse.ArgumentParser(description='The given force potential fields')

parser.add_argument('-a', '--animation', action='store_true')
args = parser.parse_args()

env = EnvBase('question1.yaml', save_ani=args.animation)
grid_map = grid_graph(grid_map_matrix=env.world.grid_map, xy_reso=env.world.reso)
astar = Astar()

start_point = [2, 4]
goal_point = [5, 5]

env.ax.plot(start_point[0], start_point[1], marker='o', markersize=5, color='r')
env.ax.plot(goal_point[0], goal_point[1], marker='o', markersize=5, color='g')

start_x, start_y = grid_map.pose_to_index(*start_point)
goal_x, goal_y = grid_map.pose_to_index(*goal_point)

start_node = grid_map.node_tuple(start_x, start_y, 0, None)
goal_node = grid_map.node_tuple(goal_x, goal_y, 0, None)

final_node, visit_list = astar.find_path(grid_map, start_node, goal_node)

path_index_list = astar.generate_path(final_node)
path_index_list.reverse()

# animation
for index in visit_list:
    pos_x, pos_y = grid_map.index_to_pose(*index)  
    env.ax.plot(pos_x, pos_y, marker='o', markersize=2, color='k')
    env.step()
    env.render()

for index in path_index_list:
    pos_x, pos_y = grid_map.index_to_pose(*index)  
    env.ax.plot(pos_x, pos_y, marker='o', markersize=2, color='r')
    env.step()
    env.render()

env.end(ani_name = 'astar', ani_kwargs={'subrectangles': True}, show_traj=True)