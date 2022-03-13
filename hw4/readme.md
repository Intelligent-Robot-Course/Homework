# Homework 4 - Markov Decision Process

-- Course: *Intelligent Robotics – Professor: Qi Hao*

**Coding Homeworks.** Most of coding assignments will be done by Python(>=3.5) under a simple [robotics simulator](https://github.com/hanruihua/intelligent-robot-simulator/tree/edu). You can follow the [Coding instruction](#jump) to use this simulator to complete the coding part in question1-3. Your final submission should be a compressed package with extension .zip, which includes your codes and explanations (you need to know how to write the manuscript with Markdown or LATEX). Your code should be run step-by-step without any error. Real-time animation is also recommended.

----

## Grid Map Environment

- white: the start position 
- red: the goal position
- green: the obstacle
- black: ground

- obstacle reward: -10
- goal reward: 10
- other reward: -1
- over the bound: -5

<div align=center> <img src=image/mdp.png width=50%/> </div>


## Question1  

Please simulate the value iteration algorithm to calculate the value for a given policy.  

## Question2

Please simulate the policy iteration algorithm to improve a policy under the given value function. 

## Question3

Please find the optimal path under a given grid map environment with reward using Markov Decision Process (MDP)

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

There are seven files for these questions in the source folder, *[question_run1.py](source/question_run1.py)*, *[question_run2.py](source/question_run2.py)*, *[question_run3.py](source/question_run3.py)*, *[mdp.py](source/mdp.py)*, *[grid_map.py](source/grid_map.py)*, *[map_matrix.npy](source/map_matrix.npy)*, and *[reward_matrix.npy](source/reward_matrix.npy)*

- *question_run1.py* is the main program you should run for question1
- *question_run2.py* is the main program you should run for question2
- *question_run3.py* is the main program you should run for question3
- **[mdp.py](source/mdp.py)** is the file to perform Markov Decision Process. You should complete the functions include value iteration and policy iteration in this file for question1 and question2 respectively.
- *grid_map.py* is the file that defines the class about the grid map for you to use.
- *map_matrix.npy* and *reward_matrix.npy* define the map and the reward in each grid.

You should complete the file **[mdp.py](source/mdp.py)** for question1 and question2, and *[question_run3.py](source/question_run3.py)* for the question3 to show the simulation results (as follows). You can set the parameter *animation = True* in *question_run.py* to generate the animation such as the follows.

<div align=center> <img src=image/mdp.gif width=50%/> </div>







