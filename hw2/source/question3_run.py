from ir_sim.env import env_base
from potential_fields import potential_fields
from pathlib import Path

animation = False # whether generate the animation
image_path = Path(__file__).parent / 'image'  # image and animation path
gif_path = Path(__file__).parent / 'gif'

env = env_base(world_name = 'question3.yaml')
pf = potential_fields()
env.show()
for i in range(1000):

    if animation:
        env.save_fig(image_path, i) 


    ## please complete this part to solve question3 based on the force defined in question2 
    line_list = env.obs_line_states

    #    ...
    
    ##  

    env.robot_step(pf_force)
    env.render(show_traj=True)

    if env.collision_check() or env.arrive_check():  # check whether there are 
        break

if animation:
    env.save_ani(image_path, gif_path, ani_name='potential_field', keep_len=10)

print('done')
env.show()