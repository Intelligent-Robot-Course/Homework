from ir_sim.env import EnvBase
from potential_fields import potential_fields                 
import argparse

# force: uniform, perpendicular, attractive, repulsive, tangential

parser = argparse.ArgumentParser(description='The given force potential fields')

parser.add_argument('-f', default='uniform', dest='force')
parser.add_argument('-a', '--animation', action='store_true')

args = parser.parse_args()

if args.force == 'perpendicular':
    env = EnvBase(world_name = 'question2.yaml', save_ani=args.animation)
else:
    env = EnvBase(world_name = 'question2_no_obs.yaml', save_ani=args.animation)

pf = potential_fields()

for i in range(40):

    if args.force == 'uniform':
        pf_vel = pf.uniform()
    
    elif args.force == 'perpendicular':
        pf_vel = pf.perpendicular(env.obstacle_list[0].points, env.robot.state)
    
    elif args.force == 'attractive':
        pf_vel = pf.attractive(env.robot.goal, env.robot.state)

    elif args.force == 'repulsive':
        pf_vel = pf.repulsive(env.robot.goal, env.robot.state)

    elif args.force == 'tangential':
        pf_vel = pf.tangential(env.robot.goal, env.robot.state)

    env.step(pf_vel)
    env.render()

env.end(ani_name = args.force, ani_kwargs={'subrectangles': True})