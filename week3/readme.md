
# Homework Week3


*Course:Intelligent Robots (CS401) – Professor: Qi Hao*

### Question 1

The state transition for the action open the door is as shown in Fig. 1. If the door is closed, the action open the door succeeds in ${\rm{80\% }}$ of all cases. Assume the probabilities of the closed door and open door are ${\rm{50\% }}$ respectively.

<div align=center>
<img src=image/f1.bmp/>
</div>

**Calculate the probability of:** $P(open|u)$ for $u=$ open door. ![formula](https://render.githubusercontent.com/render/math?math=e^{i \pi} = -1)

### Question 2

A robot is going through a door, where the state of the door is $x = \{ open,closed\}$, the measurement of the door by the robot is $z = \{ open,closed\} $, and the action of the
robot is $u = \{ push,do\_nothing\}$. We assume that:

* (1) The robot doesnt know the state of the door initially;

* (2) The measurement noise:p(z=open|x=open)=0.8;p(z=closed|x=open)=
0.2;
```
```
(3) The measurement noise: p(z = open|x = closed)= 0.3; p(z = closed|x =
closed)=0.7;
```
```
(4) When the robot pushes the closed door, the chance to make it open is 0.9;
```
```
(5) When the robot pushes the open door, nothing will be changed;
```
```
(6) When the robot does nothing, the state of the door will not be changed;
```
```
Then, what is the state distribution of the door, after the robots measurements are
{open,open}, and its actions are{do_nothing,push}?
```

Intelligent Robots (CS401) –Homework #4 3

```
Question 3
```
```
A robot cleaner is roaming within an apartment with four rooms. The map of the
apartment is given as follows. The probability of the robot going through each door
is 0.1. Please answer the following questions:
```
```
(1) What is the Markov model for the robot roaming?
```
```
(2) What is the probability of the robot staying at each room?
```
```
(3) What is the probability of the robot going through the door between (1) and (4)
when the robot is going through a door?
```
```
Question 4
```
```
Given the observation modelp(zt|x0:t,z1:t,u1:t)=p(zt|xt)and the dynamics model
p(xt|x1:t− 1 ,z1:t,u1:t)=p(xt|xt− 1 ,ut)
```
```
Please derive how to estimate the belief over xt, that is, bel(xt)=
P(xt|u 1 ,z 1 ,... ,ut,zt), with the terms of bel(xt− 1 ) , observation and dynamics
models.
```



