# Homework 8 - Occupancy Grid Mapping With Known Poses

-- Course: *Intelligent Robotics – Professor: Qi Hao*

**Coding Homeworks.** Your final submission should be a compressed package with extension .zip, which includes your codes and explanations (you need to know how to write the manuscript with Markdown or LATEX). Your code should be run step-by-step without any error. Real-time animation is also recommended.

----

## Overview
Occupancy grid maps (Hans Moravec, A.E. Elfes: High resolution maps from wide angle sonar, Proc. IEEE Int. Conf. Robotics Autom. (1985)) are a popular approach to represent the environment of a mobile robot given known poses. The grid is basically discrete representation of the environment, which stores the posterior probability that the corresponding area in the environment is occupied or not, and each grid cell is considered independently from all others. Occupancy grid maps can be learned efficiently using a probabilistic approach. Reflection maps are an alternative representation. They store in each cell the probability that a beam is reflected by this cell. In this homework, we focus on the usage of probabilistic approach.


## Occupancy Mapping
A robot has to build an occupancy grid map (cells c0, . . . cn) of a simple one-dimensional environment using a sequence of measurements from a range sensor:

<div align=center> <img src=images/demo.png width=50%/> </div>


Assume a very simple sensor model: every grid cell with a distance (based on its coordinate) smaller than the measured distance is assumed to be occupied with p = 0.3. Every cell behind the measured distance is occupied with p = 0.6. Every cell located more than 20cm behind the measured distance should not be updated. 

## Task 1

Please calculate the resulting occupancy grid map using the inverse sensor model using Python.

Assign the cell coordinates, which span from 0 to 200 (both endpoints included) with increments of 10, to one array c and the belief values to another array m. Use matplotlib.pyplot.plot(c,m) to visualize the belief. 

<div align=center> <img src=images/belief_task1.png width=50%/> </div>

The measurements and the prior belief are given in the follow table:

| Grid resolution              | 10cm                                       |
|------------------------------|--------------------------------------------|
| Map length  (1D only)        | 2m                                         |
| Robot position               | c0                                         |
| Orientation (of th e sensor) | heading to cn (see figure)                 |
| Measurement  (in cm)         | 101, 82, 91, 112, 99, 151, 96, 85, 99, 105 |
| Prior                        | 0.5                                        |


In order to solve this exercise we will use log-odds, as they provide a very simple update formula, with only one addition and one subtraction.
Recall the log-odds update formula:

<img src="https://latex.codecogs.com/svg.image?l(m_i|z_{1:t},&space;x_{1:t})&space;=&space;l(m_i|z_t,x_t)&space;&plus;&space;l(m_i|z_{1:t-1},x_{1:t-1})&space;-&space;l(m_i)" title="https://latex.codecogs.com/svg.image?l(m_i|z_{1:t}, x_{1:t}) = l(m_i|z_t,x_t) + l(m_i|z_{1:t-1},x_{1:t-1}) - l(m_i)" />

From the exercise we know that the prior:

<img src="https://latex.codecogs.com/svg.image?p(m_i)=0.5&space;\Rightarrow&space;l(m_i)&space;=&space;log\frac{p(m_i)}{1-p(m_i)}&space;=&space;0" title="https://latex.codecogs.com/svg.image?p(m_i)=0.5 \Rightarrow l(m_i) = log\frac{p(m_i)}{1-p(m_i)} = 0" />

We also know that the inverse sensor model is the following:

<img src="https://latex.codecogs.com/svg.image?p(m_i/z_t,x_t)&space;=&space;\left\{\begin{matrix}0.3&space;&&space;if&space;position(m_i)&space;\leq&space;z_t&space;\\0.6&space;&&space;if&space;position(m_i)&space;>&space;z_t&space;\wedge&space;position(m_i)\leq&space;z_t&plus;20&space;cm&space;\\0.5&space;(unused)&space;&&space;if&space;position(m_i)&space;>&space;z_t&space;&plus;&space;20&space;cm&space;\\\end{matrix}\right." />


The log-odds ratio should be applied to this function in order to obtain <img src="https://latex.codecogs.com/svg.image?\inline&space;l(m_i|z_t,x_t)" title="https://latex.codecogs.com/svg.image?\inline l(m_i|z_t,x_t)" />. Note
that unused in this context means we should not update the corresponding <img src="https://latex.codecogs.com/svg.image?\inline&space;m_i" title="https://latex.codecogs.com/svg.image?\inline m_i" /> cells. Doing
an update with <img src="https://latex.codecogs.com/svg.image?\inline&space;p(m_i|z_t,x_t)&space;=&space;0.5" title="https://latex.codecogs.com/svg.image?\inline p(m_i|z_t,x_t) = 0.5" /> would be equivalent, since <img src="https://latex.codecogs.com/svg.image?\inline&space;l(0.5)&space;=&space;0" title="https://latex.codecogs.com/svg.image?\inline l(0.5) = 0" />, but computationally more expensive.

The solution of this exercise will thus involve applying for each measurement and for each cell the log-odds update formula. Once we are done with that we convert from log-odds to probability and display the output. Note that the inverse transformation is the unique solution w.r.t. p of the log-odds definition:

<img src="https://latex.codecogs.com/svg.image?l&space;=&space;log&space;\frac{p}{1-p}&space;\Rightarrow&space;exp&space;\,&space;l&space;=&space;\frac{p}{1-p}" title="https://latex.codecogs.com/svg.image?l = log \frac{p}{1-p} \Rightarrow exp \, l = \frac{p}{1-p}" />


<img src="https://latex.codecogs.com/svg.image?(1-p)&space;exp&space;\,&space;l&space;=&space;p\Rightarrow&space;exp&space;\,&space;l&space;=&space;p(1&plus;exp&space;\,&space;l)&space;" title="https://latex.codecogs.com/svg.image?(1-p) exp \, l = p\Rightarrow exp \, l = p(1+exp \, l) " />

<img src="https://latex.codecogs.com/svg.image?p&space;=&space;\frac{exp&space;\,&space;l}{1&plus;exp&space;\,&space;l}&space;=&space;\frac{exp&space;\,&space;l&space;&plus;&space;1&space;-1}{1&plus;exp&space;\,l}&space;=&space;1&space;-&space;\frac{1}{1&plus;exp&space;\,&space;l}&space;" title="https://latex.codecogs.com/svg.image?p = \frac{exp \, l}{1+exp \, l} = \frac{exp \, l + 1 -1}{1+exp \,l} = 1 - \frac{1}{1+exp \, l} " />


## Task 2

Prove that in the occupancy grid mapping framework the occupancy value of a grid cell <img src="https://latex.codecogs.com/svg.image?\inline&space;P(m_j|x_{1:t};z_{1:t})" title="https://latex.codecogs.com/svg.image?\inline P(m_j|x_{1:t};z_{1:t})" /> is independent of the order in which the measurements are integrated.

Let us consider the log-odds update formula and let us recursively unwrap it:

<img src="https://latex.codecogs.com/svg.image?\inline&space;l(m_i|z_{1:t},&space;x_{1:t})&space;=&space;l(m_i|z_t,&space;x_t)&space;&plus;&space;l(m_i|z_{1:t-1},&space;x_{1:t-1})&space;-&space;l(m_i)&space;\\=&space;&space;l(m_i|z_t,&space;x_t)&space;&plus;&space;l(m_i|z_{1:t-1},&space;x_{1:t-1})&space;&plus;&space;l(m_i|z_{1:t-2},&space;x_{1:t-2})&space;-&space;2.l(m_i)&space;\\=&space;...&space;=&space;&space;\sum_{k=1}^{t}l(m_i|z_k,x_k)&space;-&space;t.l(m_i)" title="https://latex.codecogs.com/svg.image?\inline l(m_i|z_{1:t}, x_{1:t}) = l(m_i|z_t, x_t) + l(m_i|z_{1:t-1}, x_{1:t-1}) - l(m_i) \\= l(m_i|z_t, x_t) + l(m_i|z_{1:t-1}, x_{1:t-1}) + l(m_i|z_{1:t-2}, x_{1:t-2}) - 2.l(m_i) \\= ... = \sum_{k=1}^{t}l(m_i|z_k,x_k) - t.l(m_i)" />

It is clear that  <img src="https://latex.codecogs.com/svg.image?\inline&space;l(m_i|z_{1:t},&space;x_{1:t})" title="https://latex.codecogs.com/svg.image?\inline l(m_i|z_{1:t}, x_{1:t})" /> is simply a sum of the log-odds form of the inverse measurements. Suppose that we exchange a measurement at time i with the measurement at a different time j. Since the sum is a commutative operator we will still obtain the same value of <img src="https://latex.codecogs.com/svg.image?\inline&space;l(m_i|z_{1:t},&space;x_{1:t})" title="https://latex.codecogs.com/svg.image?\inline l(m_i|z_{1:t}, x_{1:t})" />. Hence, we can repeat exchanging measurements to obtain any order permutation of the measurements without changing the result. Finally, since the log-odds value does not change, neither will the corresponding probability.


## Code instructions for tasks
**Note1** [task1.py](code/task1.py) give the implememtation framework of the task1.

**Note2** [task2.py](code/task2.py) give the implememtation framework of the task2.
