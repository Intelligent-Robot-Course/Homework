import numpy as np
from ir_sim.env import env_base
from grid_graph import grid_graph
from dwa import dynamic_window_approach
from Astar import Astar
from pathlib import Path

# similar to question1 generate the astar path
animation = False # whether generate the animation
image_path = Path(__file__).parent / 'image'  # image and animation path
gif_path = Path(__file__).parent / 'gif'

world_name = 'question3.yaml'
env = env_base(world_name = world_name)
grid_map = grid_graph(grid_map_matrix=env.map_matrix, xy_reso=env.xy_reso)
dwa = dynamic_window_approach(vx_range=[-1.5, 1.5], vy_range=[-1.5, 1.5], accelerate=2, time_interval=0.2, predict_time=0.5, graph=grid_map)
astar = Astar()

start_point = [env.robot.state[0, 0], env.robot.state[1, 0]]
goal_point = [env.robot.goal[0, 0], env.robot.goal[1, 0]]

start_x, start_y = grid_map.pose_to_index(*start_point)
goal_x, goal_y = grid_map.pose_to_index(*goal_point)

start_node = grid_map.node_tuple(start_x, start_y, 0, None)
goal_node = grid_map.node_tuple(goal_x, goal_y, 0, None)

final_node, visit_list = astar.find_path(grid_map, start_node, goal_node)

path_index_list = astar.generate_path(final_node)
path_index_list.reverse()
# similar to question1, generate the astar path

# plot the astar path
j = 0

for index in path_index_list:
    pos_x, pos_y = grid_map.index_to_pose(*index)  
    env.world_plot.draw_point([pos_x, pos_y], color='r')
    env.render()

    if animation: env.save_fig(image_path, j) 

for i in range(300):

    # calculate the dwa velocity. you should complete the cal_vel function (add the astar cost) for question3
    vel, pre_traj = dwa.cal_vel(cur_pose=env.robot.state, goal_pose=env.robot.goal[0:2], current_vel=env.robot.vel_omni, v_gain=1, g_gain=1, o_gain=1, a_gain=1, astar_path=path_index_list)

    env.robot_step(vel)
    env.render(show_traj=True)  

    if animation: env.save_fig(image_path, j+i) 

    if env.arrive_check():
        break

if animation: env.save_ani(image_path, gif_path, ani_name='astar_dwa', keep_len=10)

env.show()