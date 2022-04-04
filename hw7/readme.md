# Homework 7 - Kalman Filter

-- Course: *Intelligent Robotics – Professor: Qi Hao*

**Coding Homeworks.** Your final submission should be a compressed package with extension .zip, which includes your codes and explanations (you need to know how to write the manuscript with Markdown or LATEX). Your code should be run step-by-step without any error. Real-time animation is also recommended.

----


## Overview
You will be implementing a 2-Dimensional Kalman Filter for constant velocity model and also a 2D particle filter.
Corresponding code skeltons are provided for you to implement the two filters. Also, the visulization of the filters are provided in the framework.


## 2D Kalman Filter with Constant Velocity Model
A simple kalman filter implementation in python. A simulated scenario where we consider a robot in 2D and use odometry for prediction and mocked GPS measurement for evaluation.

## motion model and obervation motion model.

### Velocity-based 2D robot motion model 

 
Suppose the robot has a state vector includes 3 states at time <img src="https://latex.codecogs.com/svg.image?\inline&space;t" title="https://latex.codecogs.com/svg.image?\inline t" />:

<img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf&space;X_t&space;=&space;\begin{bmatrix}x_t&space;\\y_t&space;\\\theta_t\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline \textbf X_t = \begin{bmatrix}x_t \\y_t \\\theta_t\end{bmatrix}" />

Meanwhile, the robot can obtain the velocity and orientation information, and their can be used as input vector at each time step:

<img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{u}_t&space;=&space;\begin{bmatrix}&space;v_t\\w_t\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline \textbf{u}_t = \begin{bmatrix} v_t\\w_t\end{bmatrix}" />

Thus, the robot motion model is:

<img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf&space;X_{t&plus;1}&space;=&space;A&space;\textbf{X}_t&space;&plus;&space;B&space;\textbf{u}_t&space;&plus;&space;\textbf{w}_t" title="https://latex.codecogs.com/svg.image?\inline \textbf X_{t+1} = A \textbf{X}_t + B \textbf{u}_t + \textbf{w}_t" />

where

<img src="https://latex.codecogs.com/svg.image?\inline&space;A&space;=&space;\begin{bmatrix}1&space;&&space;0&space;&&space;0&space;\\0&space;&&space;1&space;&&space;0&space;\\0&space;&&space;0&space;&&space;1&space;\\\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline A = \begin{bmatrix}1 & 0 & 0 \\0 & 1 & 0 \\0 & 0 & 1 \\\end{bmatrix}" />, <img src="https://latex.codecogs.com/svg.image?\inline&space;B&space;=&space;\begin{bmatrix}cos(\theta_t)&space;&&space;0&space;\\sin(\theta_t)&space;&&space;0&space;\\0&space;&&space;&space;1\\\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline B = \begin{bmatrix}cos(\theta_t) & 0 \\sin(\theta_t) & 0 \\0 & 1\\\end{bmatrix}" />, and  <img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{w}_t&space;" title="https://latex.codecogs.com/svg.image?\inline \textbf{w}_t " /> is the zero-mean Gaussian process noise vector with covariance matrix Q.
 
 
### Observation Model:

Also, the robot has a GPS sensor, it means that the robot can observe x, y position at each time:

<img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{Z}_{t&plus;1}&space;=&space;H\textbf{X}_{t&plus;1}&space;&plus;&space;\textbf{v}_{t&plus;1}" title="https://latex.codecogs.com/svg.image?\inline \textbf{Z}_{t+1} = H\textbf{X}_{t+1} + \textbf{v}_{t+1}" />


where, <img src="https://latex.codecogs.com/svg.image?\inline&space;H&space;=&space;\begin{bmatrix}1&space;&&space;0&space;&&space;0&space;\\0&space;&&space;1&space;&&space;0&space;\\0&space;&&space;0&space;&&space;0&space;\\\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline H = \begin{bmatrix}1 & 0 & 0 \\0 & 1 & 0 \\0 & 0 & 0 \\\end{bmatrix}" /> and <img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{v}_{t&plus;1}" title="https://latex.codecogs.com/svg.image?\inline \textbf{v}_{t+1}" /> is the zero-mean Gaussian observation noise with variance R.

### Implement the kalman filter
If the kalman filter design is complete, we just have to write the code to run the filter and output the data in the format of our choice.
The initial uncertanty for the motion noise and observation noise are defined in the code.
The comparisons between the odometry, GPS, filter and ground truth are shown in the following figure:

<div align=left> <img src=sources/kalman_compare.png width=40%/> </div>


### Task 1
Please derivate the predcition and update process of kalman filter.

### Task 2
Please implement the "predict" and "estimate" function in the code [kalman-filter.py](code/kalman-filter.py)

