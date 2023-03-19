from ir_sim.env import EnvBase
from grid_graph import grid_graph
from dwa import dynamic_window_approach
from Astar import Astar
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--animation', action='store_true')
args = parser.parse_args()

env = EnvBase('question3.yaml', save_ani=args.animation)
grid_map = grid_graph(env.world.grid_map, env.world.reso)
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

for index in path_index_list:
    pos_x, pos_y = grid_map.index_to_pose(*index)  
    env.ax.plot(pos_x, pos_y, marker='o', markersize=3, color='r')
    env.render()

for i in range(300):

    vel, pre_traj = dwa.cal_vel(cur_pose=env.robot.state, goal_pose=env.robot.goal[0:2], current_vel=env.robot.vel_omni, v_gain=10, g_gain=5, o_gain=9, a_gain=10, astar_path=path_index_list)

    env.step(vel)
    env.render(show_traj=True)  

    if env.done(): break
        
env.end(ani_name = 'astar_dwa', ani_kwargs={'subrectangles': True}, show_traj=True)