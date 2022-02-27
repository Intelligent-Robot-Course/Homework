
# Homework Ⅰ

*Course:Intelligent Robotics (CS401) – Professor: Qi Hao*

### Question 1

The state transition for the action open the door is as shown in the following figure. If the door is closed, the action open the door succeeds in *80%* of all cases. Assume the probabilities of the closed door and open door are *50%* respectively.

<div align=center> <img src=image/f1.bmp/> </div>

**Calculate the probability of:** 

*P( open | u )* for *u =* "open door".

### Question 2

A robot is going through a door, where the state of the door is x = {open,closed}, the measurement of the door by the robot is *z = {open,closed}*, and the action of the robot is *u = {push,do_nothing}*. We assume that:

* (1) The robot doesn't know the state of the door initially;

* (2) The measurement noise: *p(z=open|x=open)=0.8*; *p(z=closed|x=open)=0.2*;

* (3) The measurement noise: *p(z=open|x=closed)= 0.3*; *p(z= closed|x=closed)=0.7*;

* (4) When the robot pushes the closed door, the chance to make it open is 0.9;

* (5) When the robot pushes the open door, nothing will be changed;

* (6) When the robot does nothing, the state of the door will not be changed;

Then, what is the state distribution of the door, after the robots measurements are *{open,open}*, and its actions are *{do_nothing,push}?*

<div align=center> <img src=image/f2.bmp/> </div>

## Question 3

A robot cleaner is roaming within an apartment with four rooms. The map of the apartment is given as follows. The probability of the robot going through each door is 0.1. Please answer the following questions:

* (1) What is the Markov model for the robot roaming?

* (2) What is the probability of the robot staying at each room?

* (3) What is the probability of the robot going through the door between (1) and (4) when the robot is going through a door?

<div align=center> <img src=image/f3.bmp/> </div>

## Question 4

Given the observation model <img src="https://latex.codecogs.com/svg.image?p\left(z_{t}&space;\mid&space;x_{0:&space;t},&space;z_{1:&space;t-1},&space;u_{1:&space;t}\right)=p\left(z_{t}&space;\mid&space;x_{t}\right)" title="p\left(z_{t} \mid x_{0: t}, z_{1: t-1}, u_{1: t}\right)=p\left(z_{t} \mid x_{t}\right)" /> and the dynamics model <img src="https://latex.codecogs.com/svg.image?p\left(x_{t}&space;\mid&space;x_{0:&space;t-1},&space;z_{1:&space;t-1},&space;u_{1:&space;t}\right)=p\left(x_{t}&space;\mid&space;x_{t-1},&space;u_{t}\right)" title="p\left(x_{t} \mid x_{0: t-1}, z_{1: t-1}, u_{1: t}\right)=p\left(x_{t} \mid x_{t-1}, u_{t}\right)" />

Please derive how to estimate the belief over <img src="https://latex.codecogs.com/svg.image?{x_t}" title="{x_t}" />, that is, <img src="https://latex.codecogs.com/svg.image?bel\left(&space;{{x_t}}&space;\right)&space;=&space;p\left(&space;{{x_t}\mid&space;{u_1},{z_1},&space;\ldots&space;,{u_t},{z_t}}&space;\right)" title="bel\left( {{x_t}} \right) = p\left( {{x_t}\mid {u_1},{z_1}, \ldots ,{u_t},{z_t}} \right)" />, with the terms of <img src="https://latex.codecogs.com/svg.image?bel\left(&space;{{x_{t&space;-&space;1}}}&space;\right)" title="bel\left( {{x_{t - 1}}} \right)" />, observation and dynamics models.

## Question 5

Given the observation model <img src="https://latex.codecogs.com/svg.image?p\left(z_{t}&space;\mid&space;x_{0:&space;t},&space;z_{1:&space;t-1},&space;u_{1:&space;t}\right)=p\left(z_{t}&space;\mid&space;x_{t}\right)" title="p\left(z_{t} \mid x_{0: t}, z_{1: t-1}, u_{1: t}\right)=p\left(z_{t} \mid x_{t}\right)" /> and the dynamics model <img src="https://latex.codecogs.com/svg.image?p\left(x_{t}&space;\mid&space;x_{0:&space;t-1},&space;z_{1:&space;t-1},&space;u_{1:&space;t}\right)=p\left(x_{t}&space;\mid&space;x_{t-1},&space;u_{t}\right)" title="p\left(x_{t} \mid x_{0: t-1}, z_{1: t-1}, u_{1: t}\right)=p\left(x_{t} \mid x_{t-1}, u_{t}\right)" />

Please derive how to estimate the belief over <img src="https://latex.codecogs.com/svg.image?x_{0:&space;t}" title="x_{0: t}" />, that is, <img src="https://latex.codecogs.com/svg.image?bel\left(&space;{{x_{0:t}}}&space;\right)&space;=&space;p\left(&space;{{x_{0:t}}\mid&space;{u_1},{z_1},&space;\ldots&space;,{u_t},{z_t}}&space;\right)" title="bel\left( {{x_{0:t}}} \right) = p\left( {{x_{0:t}}\mid {u_1},{z_1}, \ldots ,{u_t},{z_t}} \right)" />, with the terms of <img src="https://latex.codecogs.com/svg.image?bel\left(&space;{{x_{0:t&space;-&space;1}}}&space;\right)" title="bel\left( {{x_{0:t - 1}}} \right)" />, observation and dynamics models.

