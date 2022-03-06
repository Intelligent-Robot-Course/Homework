# Homework 3- Planning

-- Course: *Intelligent Robotics – Professor: Qi Hao*

**Coding Homeworks.** Most of coding assignments will be done by Python(>=3.5) under a simple [robotics simulator](https://github.com/hanruihua/intelligent-robot-simulator/tree/edu). You can follow the [Coding instruction](#jump) to use this simulator to complete the coding question1,2,3. Your final submission should be a compressed package with extension .zip, which includes your codes and explanations (you need to know how to write the manuscript with Markdown or LATEX, the scan version is also accepted). Your code should be run step-by-step without any error. Real-time animation is also encouraged.

**Note:** The graphs as shown below are only simple demonstrations to help you understand. You can develop your own algorithms to achieve higher performance by your understanding.

## Question1 

Simulate the Astar algorithm depending on the given grid map. You can follow the [Coding instruction](#jump) to use the robotics simulator to complete this task. 

<div align=center> <img src=image/astar.gif width=50%/> </div>

## Question2 

Simulate a robot to achieve the collision avoidance motion with dynamic window approach(DWA). You can follow the [Coding instruction](#jump) to use the robotics simulator to complete this task.

<div align=center> <img src=image/dwa.gif width=50%/> </div>

## Question3 - Extra Credit

Combine the astar and dwa to achieve the 5D planning under the given grid map. You can follow the [Coding instruction](#jump) to use the robotics simulator to complete this task.

<div align=center> <img src=image/astar_dwa.gif width=50%/> </div>

## <span id="jump">Coding instruction</span>

### Install the intelligent robotics simulator

```
git clone -b edu https://github.com/hanruihua/intelligent-robot-simulator.git
cd intelligent-robot-simulator
pip install -e .
```

**Note1**: Please confirm that this repository is under the *edu* branch. You can use **git branch** to check current branch. If it is not under the *edu* branch, you can use **git checkout edu** to change current branch to *edu* branch.

**Note2**: The pycharm reduces the functionality of Matplotlib, which may lead to the failure of saving the gif animation. You can follow this [link](https://blog.csdn.net/Weiai_520/article/details/106437605) to solve this problem

### Code for question1

There are four files for question1 in the source folder, *[question1.yaml](source/question1.yaml)*, *[question1_run.py](source/question1_run.py)*, *[Astar.py](source/Astar.py)*, and *[grid_graph.py](source/grid_graph.py)*.

- *question1.yaml* is the configuration file for the simulator.
- *question1_run.py* is the main program
- *[Astar.py](source/Astar.py)* is the file to perform A star algorithm. You should complete this file for the coding task.
- *grid_graph.py* is the file that defines the class about the grid map for you to use. 

You should complete the file *[Astar.py](source/Astar.py)* and run *question1_run.py* to show the simulation results. You can set the parameter *animation = True* in *question1_run.py* to generate the gif file.

### Code for question2

There are four files for question1 in the source folder, *[question2.yaml](source/question2.yaml)*, *[question2_run.py](source/question2_run.py)*, *[dwa.py](source/dwa.py)*, and *[grid_graph.py](source/grid_graph.py)*.

- *question2.yaml* is the configuration file for the simulator.
- *question2_run.py* is the main program
- *[dwa.py](source/dwa.py)* is the file to perform dwa algorithm. You should complete this file for the coding task.(the cost function)
- *grid_graph.py* is the file that defines the class about the grid map for you to use. 

You should complete the functions in *[dwa.py](source/dwa.py)* and run *question2_run.py* to show the simulation results. You can set the parameter *animation = True* in *question2_run.py* to generate the gif file.

### Code for question3

There are two main files for question3 in the source folder, *[question3.yaml](source/question3.yaml)*, *[question3_run.py](source/question3_run.py)*. In question3, you should utilize the file and function defined and completed the in question1 and question2 to complete the 5D planning. You should complete the function **astar_cost** in the file *[dwa.py](source/dwa.py)* to complete this task.

**Note:** All the gain arguments should be tuned for your own task.






