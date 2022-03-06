import numpy as np
from ir_sim.env import env_base
from grid_graph import grid_graph
from dwa import dynamic_window_approach
from pathlib import Path

# for the animation
animation = False # whether generate the animation
image_path = Path(__file__).parent / 'image'  # image and animation path
gif_path = Path(__file__).parent / 'gif'

# the environment
world_name = 'question2.yaml'
env = env_base(world_name = world_name)
grid_map = grid_graph(grid_map_matrix=env.map_matrix, xy_reso=env.xy_reso)

# the main program of dynamic_window_approach
# vx_range: the range of the velocity x, vx_range: the range of the velocity y
# time_interval: the step time
dwa = dynamic_window_approach(vx_range=[-1.5, 1.5], vy_range=[-1.5, 1.5], accelerate=2, time_interval=0.5, predict_time=1, graph=grid_map)

for i in range(300):

    # the main function to calculate the velocity
    vel, pre_traj = dwa.cal_vel(cur_pose=env.robot.state, goal_pose=env.robot.goal[0:2], current_vel=env.robot.vel_omni, v_gain=1, g_gain=1, o_gain=1.5)

    if animation: env.save_fig(image_path, i) 

    env.robot_step(vel)
    env.render(show_traj=True)

    if env.arrive_check():
        break

if animation: env.save_ani(image_path, gif_path, ani_name='dwa', keep_len=10)

env.show()