# Homework 4 - Markov Decision Process

-- Course: *Intelligent Robotics – Professor: Qi Hao*

----

## Grid Map Environment

- white: the start position 
- red: the goal position
- green: the obstacles
- black: ground

- obstacle collision penalty: -10
- goal reward: 10
- each step penalty: -1
- over the bound penalty: -5

<div align=center> <img src=image/mdp.png width=50%/> </div>

## Question1  

Please complete the policy evaluation algorithm to calculate the value for a given policy depending on the following pseudocode:

<div align=center> <img src=image/policy_evaluation.png width=50%/> </div>

## Question2

Please complete the MDP policy iteration algorithm to find the optimal path in the given map depending on the following pseudocode. 

<div align=center> <img src=image/policy_iteration.png width=50%/> </div>

<div align=center> <img src=gif/policy_iteration.gif width=50%/> </div>

## Question3

Please complete the MDP value iteration algorithm to find the optimal path in the given map depending on the following pseudocode.

<div align=center> <img src=image/value_iteration.png width=50%/> </div>

<div align=center> <img src=gif/value_iteration.gif width=50%/> </div>

## <span id="jump">Coding instruction</span>


### Install the intelligent robotics simulator

```
pip install ir_sim==1.1.8
```

### Code for questions



There are seven files for these questions in the source folder, *[question_run1.py](source/question_run1.py)*, *[question_run2.py](source/question_run2.py)*, *[question_run3.py](source/question_run3.py)*, *[mdp.py](source/mdp.py)*, *[grid_map.py](source/grid_map.py)*, *[map_matrix.npy](source/map_matrix.npy)*, and *[reward_matrix.npy](source/reward_matrix.npy)*

- *question_run1.py* is the main program you should run for question1
- *question_run2.py* is the main program you should run for question2
- *question_run3.py* is the main program you should run for question3
- **[mdp.py](source/mdp.py)** is the file to perform Markov Decision Process (MDP) algorithm. You should complete the functions including policy_evaluation, policy_iteration, and value_iteration and policy iteration in this file for above questions. 
- *grid_map.py* is the file that defines the class about the grid map for you to use.
- *map_matrix.npy* and *reward_matrix.npy* define the map and the reward in each grid.

Please run the following commands (question2 as example) to see the simulated results:

```
python question2_run.py
```

If you want to save the animation, you can run this command:

```
python question2_run.py -a
```







