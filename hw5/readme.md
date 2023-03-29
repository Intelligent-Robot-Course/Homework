# Homework 5 - Reinforcement Learning
-- Course: *Intelligent Robotics – Professor: Qi Hao*

----

## Grid Map Environment

- white: the start position 
- red: the goal position
- green: the obstacle
- black: ground

- obstacle collision penalty: -1
- goal reward: 10
- each step penalty: 0
- over the bound penalty: -5

<div align=center> <img src=image/grid.png width=50%/> </div>

## Question1  

Please simulate the Monte Carlo Reinforcemenet learning with Exploring Starts under the given grid map environment. 

Pseudocode: 

<div align=center> <img src=image/mc_es.png width=70%/> </div>

Experimental Demonstration:

<div align=center> <img src=gif/monte_carlo_es.gif width=70%/> </div>


## Question2

Please simulate the Sarsa (on-policy TD control)) algorithm under the given grid map environment.

Pseudocode: 

<div align=center> <img src=image/sarsa.png width=70%/> </div>

Experimental Demonstration:

<div align=center> <img src=gif/SARSA.gif width=70%/> </div>

## Question3

Please simulate the Q_learning (Off-policy TD Control) algorithm under the given grid map environment.

Pseudocode: 

<div align=center> <img src=image/qlearning.png width=70%/> </div>

Experimental Demonstration:  

<div align=center> <img src=gif/Q_learning.gif width=70%/> </div>


**Note:** The above demonstrations are only parts of the output policy. Normally, your solution can be different but moving to the goal efficiently is necessary.

## Question4 - Extra Credit

Please add the heuristic reward on the grid map, such as the DWA reward, A star reward, or distance-to-goal based reward learned form the previous lectures, to achieve a regular policy as you expected.

## <span id="jump">Coding instruction</span>


### Code for questions

- install the package 'tqdm' for usage:

```
pip install tqdm
```

There are multiple files for these questions in the source folder. 

- *[question_run1.py](source/question_run1.py)*: is the main program you should run for question1
- *[question_run2.py](source/question_run2.py)*: is the main program you should run for question2
- *[question_run3.py](source/question_run3.py)*: is the main program you should run for question3
- *[reinforcement_learning.py](source/reinforcement_learning.py)*: is the library to implement three reinforcement learning algorithms: Monte Carlo Exploring Starts, Sarsa, and Q-learning. You should fill in this file to complete these three algorithms for the questions. 
-  *[grid_map.py](source/grid_map.py)*: is the file that defines the class about the grid map for you to use. You can add heuristic reward here for extra question4. 
- *[map_matrix.npy](source/map_matrix.npy)* and *[reward_matrix.npy](source/reward_matrix.npy)*: define the map and the reward in each grid.

You should complement the parts between '----' in the file **[reinforcement_learning.py](source/reinforcement_learning.py)** for question1-3, and the file **[grid_map.py](source/grid_map.py)** for extra question4. 

Please run the following commands (question2 as example) to see the simulated results:

```
python question2_run.py
```

If you want to save the animation, you can run this command:

```
python question2_run.py -a
```







