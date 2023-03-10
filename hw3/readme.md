# Homework 3- Planning

-- Course: *Intelligent Robotics – Professor: Qi Hao*

**Note:** The graphs as shown below are only simple demonstrations to help your understanding. You can develop your own algorithms to achieve higher performance.

## Question1 

Simulate the Astar algorithm depending on the given grid map. You can follow the [Coding instruction](#jump) to use the robotics simulator [ir_sim 1.1.8](https://github.com/hanruihua/ir_sim) to complete this task. 

<div align=center> <img src=animation/astar.gif width=50%/> </div>

## Question2 

Simulate a robot to achieve the collision avoidance motion with dynamic window approach (DWA). Please follow the [Coding instruction](#jump) to complete this task under [ir_sim 1.1.8](https://github.com/hanruihua/ir_sim). 

<div align=center> <img src=animation/dwa.gif width=50%/> </div>

## Question3 - Extra Credit

Combine the Astar and dwa to achieve the 5D planning under the given grid map. Please complete this task by following the [Coding instruction](#jump). 

<div align=center> <img src=animation/astar_dwa.gif width=50%/> </div>

## <span id="jump">Coding instruction</span>

### Install the intelligent robotics simulator

```
pip install ir_sim==1.1.8
```

### Code for question1

There are four files for question1 in the source folder, *[question1.yaml](source/question1.yaml)*, *[question1_run.py](source/question1_run.py)*, *[Astar.py](source/Astar.py)*, and *[grid_graph.py](source/grid_graph.py)*.

- *question1.yaml* is the configuration file for the simulator.
- *question1_run.py* is the main program
- *[Astar.py](source/Astar.py)* is the file to perform A star algorithm. **You should complete this file for the coding task.**
- *grid_graph.py* is the file that defines the class about the grid map for you to use. 

You should complete the file *[Astar.py](source/Astar.py)* and run *question1_run.py* to show the simulation results by the following command:

```
python question1_run.py
```

If you want to save the animation, you can run this command:

```
python question1_run.py -a
```

### Code for question2

There are four files for question1 in the source folder, *[question2.yaml](source/question2.yaml)*, *[question2_run.py](source/question2_run.py)*, *[dwa.py](source/dwa.py)*, and *[grid_graph.py](source/grid_graph.py)*.

- *question2.yaml* is the configuration file for the simulator.
- *question2_run.py* is the main program
- *[dwa.py](source/dwa.py)* is the file to perform dwa algorithm. **You should complete the cost function in this file for the coding task.**
- *grid_graph.py* is the file that defines the class about the grid map for you to use. 

You should complete the functions in *[dwa.py](source/dwa.py)* and run *question2_run.py* to show the simulation results by the command:

```
python question2_run.py
```

If you want to save the animation, you can run this command:

```
python question2_run.py -a
```

### Code for question3

There are two main files for question3 in the source folder, *[question3.yaml](source/question3.yaml)*, *[question3_run.py](source/question3_run.py)*. In question3, you should utilize the file and function defined and completed the in question1 and question2 to complete the 5D planning. You should complete the function **astar_cost** in the file *[dwa.py](source/dwa.py)* to complete this task.

Please run the following commands to see the simulated results:

```
python question3_run.py
```

If you want to save the animation, you can run this command:

```
python question3_run.py -a
```

**Note:** All the gain arguments should be tuned for your own task.






