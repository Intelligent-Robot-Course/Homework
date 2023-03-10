from ir_sim.env import EnvBase
from ir_sim.util.collision_dectection_geo import collision_seg_seg 
from potential_fields import potential_fields
from collections import namedtuple
import argparse

parser = argparse.ArgumentParser(description='The given force potential fields')
parser.add_argument('-a', '--animation', action='store_true')
args = parser.parse_args()

point = namedtuple('point', 'x y')

env = EnvBase(world_name='question3.yaml', save_ani=args.animation)

pf = potential_fields()

line_obs = env.get_obstacle_list() 

for i in range(1000):


    ## please complete this part to solve question3 based on the force defined in question2 


    


    ## please complete this part to solve question3 based on the force defined in question2 

    env.step(pf_force)
    env.render(show_traj=True)

    if env.done():
        break

env.end(ani_name = 'potential_field', ani_kwargs={'subrectangles': True})