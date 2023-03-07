import numpy as np
from ir_sim.env import EnvBase
from grid_graph import grid_graph
from dwa import dynamic_window_approach
import argparse

parser = argparse.ArgumentParser(description='The given force potential fields')

parser.add_argument('-a', '--animation', action='store_true')
args = parser.parse_args()

env = EnvBase('question2.yaml', save_ani=args.animation)
grid_map = grid_graph(grid_map_matrix=env.world.grid_map, xy_reso=env.world.reso)
dwa = dynamic_window_approach(vx_range=[-1.5, 1.5], vy_range=[-1.5, 1.5], accelerate=2, time_interval=0.5, predict_time=1, graph=grid_map)

for i in range(300):

    vel, pre_traj = dwa.cal_vel(cur_pose=env.robot.state, goal_pose=env.robot.goal, current_vel=env.robot.vel_omni, v_gain=1, g_gain=1, o_gain=1.5)

    env.step(vel)
    env.render(show_traj=True)

    if env.done(): break
        
env.end(ani_name = 'dwa', ani_kwargs={'subrectangles': True}, show_traj=True)