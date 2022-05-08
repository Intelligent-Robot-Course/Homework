Homework 9 - EKF-Based Landmark SLAM

-- Course: Intelligent Robotics – Professor: Qi Hao

**Coding Homeworks.** Your final submission should be a compressed package with extension .zip, which includes your codes and explanations (you need to know how to write the manuscript with Markdown or LATEX). Your code should be run step-by-step without any error. Real-time animation is also recommended.

## Overview
This project shows how to use ekfSLAM for a reliable implementation of landmark Simultaneous Localization and Mapping (SLAM) using the Extended Kalman Filter (EKF) algorithm and maximum likelihood algorithm for data association. In this project, you create a landmark map of the immediate surroundings of a vehicle and simultaneously track the path of the vehicle. Generate a trajectory by moving the vehicle using the noisy control commands, and form the map using the landmarks it encounters along the path. Correct the vehicle trajectory and landmark estimates by observing the landmarks again.

## Simulation
This is a simulation of EKF SLAM.

-Black stars: landmarks

-Green crosses: estimates of landmark positions

-Black line: dead reckoning

-Blue line: ground truth

-Red line: EKF SLAM position estimation

<div align=left> <img src=source/animation.gif width=50%/> </div>

EKF SLAM models the SLAM problem in a single EKF where the modeled state is both the pose <img src="https://latex.codecogs.com/svg.image?\inline&space;(x,y,\theta&space;)" title="https://latex.codecogs.com/svg.image?\inline l(m_i|z_t,x_t)" />. and an array of landmarks https://latex.codecogs.com/svg.image?\inline&space;[(x_1,y_1),&space;(x_2,y_2),...,(x_n,y_n)] for n landmarks. The covariance between each of the positions and landmarks are also tracked.

<img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{X}&space;=&space;[x,y,\theta,x_1,y_1,x_2,y_2,...,x_n,y_n]^T" title="https://latex.codecogs.com/svg.image?\inline \textbf{X} = [x,y,\theta,x_1,y_1,x_2,y_2,...,x_n,y_n]^T" />

<img src="https://latex.codecogs.com/svg.image?\inline&space;P&space;=&space;\begin{bmatrix}\sigma_{xx}&space;&&space;&space;\sigma_{xy}&&space;\sigma_{x\theta}&space;&&space;\sigma_{xx1}&space;&&space;\sigma_{xy1}&space;&&space;...&&space;\sigma_{x,x_n}&space;&&space;\sigma_{x,y_n}&space;\\\sigma_{yx}&space;&&space;&space;\sigma_{yy}&&space;\sigma_{y\theta}&space;&&space;\sigma_{yx1}&space;&&space;\sigma_{yy1}&space;&&space;...&&space;\sigma_{y,x_n}&space;&&space;\sigma_{y,y_n}&space;\\\sigma_{x_n&space;x}&space;&&space;&space;\sigma_{x_ny}&&space;\sigma_{x_n\theta}&space;&&space;\sigma_{x_nx1}&space;&&space;\sigma_{x_ny1}&space;&&space;...&&space;\sigma_{x_n,x_n}&space;&&space;\sigma_{x_n,y_n}&space;&space;\\\sigma_{y_n&space;x}&space;&&space;&space;\sigma_{y_ny}&&space;\sigma_{y_n\theta}&space;&&space;\sigma_{y_nx1}&space;&&space;\sigma_{y_ny1}&space;&&space;...&&space;\sigma_{y_n,x_n}&space;&&space;\sigma_{y_n,y_n}\\\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline P = \begin{bmatrix}\sigma_{xx} & \sigma_{xy}& \sigma_{x\theta} & \sigma_{xx1} & \sigma_{xy1} & ...& \sigma_{x,x_n} & \sigma_{x,y_n} \\\sigma_{yx} & \sigma_{yy}& \sigma_{y\theta} & \sigma_{yx1} & \sigma_{yy1} & ...& \sigma_{y,x_n} & \sigma_{y,y_n} \\\sigma_{x_n x} & \sigma_{x_ny}& \sigma_{x_n\theta} & \sigma_{x_nx1} & \sigma_{x_ny1} & ...& \sigma_{x_n,x_n} & \sigma_{x_n,y_n} \\\sigma_{y_n x} & \sigma_{y_ny}& \sigma_{y_n\theta} & \sigma_{y_nx1} & \sigma_{y_ny1} & ...& \sigma_{y_n,x_n} & \sigma_{y_n,y_n}\\\end{bmatrix}" />

A single estimate of the pose is tracked over time, while the confidence in the pose is tracked by the covariance matrix P. P is a symmetric square matrix which each element in the matrix corresponding to the covariance between two parts of the system. For example, 
 <img src="https://latex.codecogs.com/svg.image?\inline&space;\sigma_{xy}" title="https://latex.codecogs.com/svg.image?\inline \sigma_{xy}" /> represents the covariance between the belief of <img src="https://latex.codecogs.com/svg.image?\inline&space;x" title="https://latex.codecogs.com/svg.image?\inline x" /> and <img src="https://latex.codecogs.com/svg.image?\inline&space;y" title="https://latex.codecogs.com/svg.image?\inline y" /> and is equal to <img src="https://latex.codecogs.com/svg.image?\inline&space;\sigma_{yx}" title="https://latex.codecogs.com/svg.image?\inline \sigma_{yx}" />.
 
 The state can be represented more concisely as following:
 
 <img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{X}&space;=&space;\begin{bmatrix}x&space;\\&space;m\end{bmatrix}&space;P&space;=&space;\begin{bmatrix}\sum_{xx}&space;&&space;\sum_{xm}&space;\\\sum_{mx}&space;&&space;\sum_{mm}&space;\\\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline \textbf{X} = \begin{bmatrix}x \\ m\end{bmatrix} P = \begin{bmatrix}\sum_{xx} & \sum_{xm} \\\sum_{mx} & \sum_{mm} \\\end{bmatrix}" />
 
 Here the state simplifies to a combination of pose ( <img src="https://latex.codecogs.com/svg.image?\inline&space;x" title="https://latex.codecogs.com/svg.image?\inline x" />) and map (<img src="https://latex.codecogs.com/svg.image?\inline&space;m" title="https://latex.codecogs.com/svg.image?\inline m" />). The covariance matrix becomes easier to understand and simply reads as the uncertainty of the robots pose (<img src="https://latex.codecogs.com/svg.image?\inline&space;\sum_{xx}" title="https://latex.codecogs.com/svg.image?\inline \sum_{xx}" />), the uncertainty of the map (<img src="https://latex.codecogs.com/svg.image?\inline&space;\sum_{mm}" title="https://latex.codecogs.com/svg.image?\inline \sum_{mm}" />), and the uncertainty of the robots pose with respect to the map and vice versa (<img src="https://latex.codecogs.com/svg.image?\inline&space;\sum_{xm},&space;\sum_{mx}" title="https://latex.codecogs.com/svg.image?\inline \sum_{xm}, \sum_{mx}" />).

