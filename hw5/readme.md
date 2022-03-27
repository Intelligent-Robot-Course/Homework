# Homework 5 - Reinforcement Learning
-- Course: *Intelligent Robotics – Professor: Qi Hao*

**Coding Homeworks.** Most of coding assignments will be done by Python(>=3.5) under a simple [robotics simulator](https://github.com/hanruihua/intelligent-robot-simulator/tree/edu). You can follow the [Coding instruction](#jump) to use this simulator to complete the coding part in question1-3. Your final submission should be a compressed package with extension .zip, which includes your codes and explanations (you need to know how to write the manuscript with Markdown or LATEX). Your code should be run step-by-step without any error. Real-time animation is also recommended.

----

## Grid Map Environment

- white: the start position 
- red: the goal position
- green: the obstacle
- black: ground

- obstacle reward: -1
- goal reward: 10
- other reward: 0
- over the bound: -5

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


**Note:** The above demonstrations are only parts of the output policy. Normally, your solution should be different but moving to the goal is necessary.

## Question4 - Extra Credit

Please add the heuristic reward on the grid map, such as the DWA reward, A star reward, or distance-to-goal based reward learned form the previous lectures, to achieve a regular policy as you expected.

## <span id="jump">Coding instruction</span>

### Install the intelligent robotics simulator

```
git clone -b edu https://github.com/hanruihua/intelligent-robot-simulator.git
cd intelligent-robot-simulator
pip install -e .
```

**Note1**: Please confirm that this repository is under the *edu* branch. You can use **git branch** to check current branch. If it is not under the *edu* branch, you can use **git checkout edu** to change current branch to *edu* branch.

**Note2**: The pycharm reduces the functionality of Matplotlib, which may lead to the failure of saving the gif animation. You can follow this [link](https://blog.csdn.net/Weiai_520/article/details/106437605) to solve this problem

**Note3:** If you have installed this simulator, you can use *git pull* to fetch the code update.

### Code for questions

There are multiple files for these questions in the source folder. 

- *[question1_run.py](source/question1_run.py)*: is the main program you should run for question1
- *[question2_run.py](source/question2_run.py)*: is the main program you should run for question2
- *[question3_run.py](source/question3_run.py)*: is the main program you should run for question3
- *[reinforcement_learning.py](source/reinforcement_learning.py)*: is the library to implement three reinforcement learning algorithms: Monte Carlo Exploring Starts, Sarsa, and Q-learning. You should fill in this file to complete these three algorithms for the questions. 
-  *[grid_map.py](source/grid_map.py)*: is the file that defines the class about the grid map for you to use. You can add heuristic reward here for extra question4. 
- *[map_matrix.npy](source/map_matrix.npy)* and *[reward_matrix.npy](source/reward_matrix.npy)*: define the map and the reward in each grid.

You should complement the parts between ---- in the file **[reinforcement_learning.py](source/reinforcement_learning.py)** for question1-3, and the file **[grid_map.py](source/grid_map.py)** for extra question4. You can set the parameter *animation = True* in *question_run.py* to generate the animation.







