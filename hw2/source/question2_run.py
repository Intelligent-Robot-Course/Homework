from ir_sim.env import env_base
from matplotlib import animation
from potential_fields import potential_fields
import numpy as np
from pathlib import Path

# parameters
potential = 'uniform' # uniform, perpendicular, attractive, repulsive, tangential

animation = False # whether generate the animation
image_path = Path(__file__).parent / 'image'  # image and animation path
gif_path = Path(__file__).parent / 'gif'

if potential == 'perpendicular':
    obs_line_states= [[-1, 2, 11, 4]]
else:
    obs_line_states=[]

env = env_base(world_name = 'question2.yaml', obs_line_states=obs_line_states)
pf = potential_fields()

for i in range(30):

    if animation:
        env.save_fig(image_path, i) 

    if potential == 'uniform':
        pf_vel = pf.uniform()
        env.robot_step(pf_vel)
        env.render(show_goal=False)

    elif potential == 'perpendicular':
        pf_vel = pf.perpendicular(obs_line_states[0], env.robot.state)
        env.robot_step(pf_vel)
        env.render(show_goal=False)

    elif potential == 'attractive':
        
        pf_vel = pf.attractive(env.robot.goal[0:2], env.robot.state)
        env.robot_step(pf_vel)
        env.render(show_goal=True)

    elif potential == 'repulsive':
        
        pf_vel = pf.repulsive(env.robot.goal[0:2], env.robot.state)
        env.robot_step(pf_vel)
        env.render(show_goal=True)

    elif potential == 'tangential':
        
        pf_vel = pf.tangential(env.robot.goal[0:2], env.robot.state)
        env.robot_step(pf_vel)
        env.render(show_goal=True)

if animation:
    env.save_ani(image_path, gif_path, ani_name=potential, keep_len=10)
    
env.show()