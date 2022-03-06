from ir_sim.env import env_base
from Astar import Astar
from grid_graph import grid_graph
from pathlib import Path

## animation
animation = False # whether generate the animation
image_path = Path(__file__).parent / 'image'  # image and animation path
gif_path = Path(__file__).parent / 'gif'

# environment world
world_name = 'question1.yaml'
env = env_base(world_name = world_name)
grid_map = grid_graph(grid_map_matrix=env.map_matrix, xy_reso=env.xy_reso)
astar = Astar()

# start position
start_point = [2, 4]
goal_point = [5, 5]

env.world_plot.draw_point(start_point, markersize=5, color='r')
env.world_plot.draw_point(goal_point, markersize=5, color='g')

# start and goal index in the grid map
start_x, start_y = grid_map.pose_to_index(*start_point)
goal_x, goal_y = grid_map.pose_to_index(*goal_point)

# start and goal graph node
start_node = grid_map.node_tuple(start_x, start_y, 0, None)
goal_node = grid_map.node_tuple(goal_x, goal_y, 0, None)

# The astar algorithm, you should complete this function
final_node, visit_list = astar.find_path(grid_map, start_node, goal_node)

# plot the path
path_index_list = astar.generate_path(final_node)
path_index_list.reverse()

# animation
i = 0
for index in visit_list:
    pos_x, pos_y = grid_map.index_to_pose(*index)  
    env.world_plot.draw_point([pos_x, pos_y])

    if animation:
        env.save_fig(image_path, i) 
        i = i +1

    env.render()

j=i+1
for index in path_index_list:
    pos_x, pos_y = grid_map.index_to_pose(*index)  
    env.world_plot.draw_point([pos_x, pos_y], color='r')

    if animation:
        env.save_fig(image_path, j) 
        j = j +1
    env.render()


if animation:
    env.save_ani(image_path, gif_path, ani_name='astar', keep_len=10)

env.show()


# for i in range(300):

#     des_vel = env.robot.cal_des_vel()

#     env.robot_step(des_vel)
#     env.render()