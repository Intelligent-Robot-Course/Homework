Homework 9 - EKF-Based Landmark SLAM & Fast SLAM based on Particle Filters

-- Course: Intelligent Robotics – Professor: Qi Hao

**Coding Homeworks.** Your final submission should be a compressed package with extension .zip, which includes your codes and explanations (you need to know how to write the manuscript with Markdown or LATEX). Your code should be run step-by-step without any error. Real-time animation is also recommended.
# EKF-Based Landmark SLAM
## Overview
The first project shows how to use ekfSLAM for a reliable implementation of landmark Simultaneous Localization and Mapping (SLAM) using the Extended Kalman Filter (EKF) algorithm and maximum likelihood algorithm for data association. In this project, you create a landmark map of the immediate surroundings of a vehicle and simultaneously track the path of the vehicle. Generate a trajectory by moving the vehicle using the noisy control commands, and form the map using the landmarks it encounters along the path. Correct the vehicle trajectory and landmark estimates by observing the landmarks again.
The second project shows the implementation of FastSLAM algorithm which is based on particle filters and belongs to the family of probabilistic SLAM approaches. It is used with feature-based maps (see gif above) or with occupancy grid maps.

## Simulation
This is a simulation of EKF SLAM.

-Black stars: landmarks

-Green crosses: estimates of landmark positions

-Black line: dead reckoning

-Blue line: ground truth

-Red line: EKF SLAM position estimation

<div align=left> <img src=source/animation.gif width=50%/> </div>

EKF SLAM models the SLAM problem in a single EKF where the modeled state is both the pose <img src="https://latex.codecogs.com/svg.image?\inline&space;(x,y,\theta&space;)" title="https://latex.codecogs.com/svg.image?\inline l(m_i|z_t,x_t)" /> and an array of landmarks <img src = "https://latex.codecogs.com/svg.image?\inline&space;[(x_1,y_1),&space;(x_2,y_2),...,(x_n,y_n)]"/> for n landmarks. The covariance between each of the positions and landmarks are also tracked.

<img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{X}&space;=&space;[x,y,\theta,x_1,y_1,x_2,y_2,...,x_n,y_n]^T" title="https://latex.codecogs.com/svg.image?\inline \textbf{X} = [x,y,\theta,x_1,y_1,x_2,y_2,...,x_n,y_n]^T" />

<img src="https://latex.codecogs.com/svg.image?\inline&space;P&space;=&space;\begin{bmatrix}\sigma_{xx}&space;&&space;&space;\sigma_{xy}&&space;\sigma_{x\theta}&space;&&space;\sigma_{xx1}&space;&&space;\sigma_{xy1}&space;&&space;...&&space;\sigma_{x,x_n}&space;&&space;\sigma_{x,y_n}&space;\\\sigma_{yx}&space;&&space;&space;\sigma_{yy}&&space;\sigma_{y\theta}&space;&&space;\sigma_{yx1}&space;&&space;\sigma_{yy1}&space;&&space;...&&space;\sigma_{y,x_n}&space;&&space;\sigma_{y,y_n}&space;\\\sigma_{x_n&space;x}&space;&&space;&space;\sigma_{x_ny}&&space;\sigma_{x_n\theta}&space;&&space;\sigma_{x_nx1}&space;&&space;\sigma_{x_ny1}&space;&&space;...&&space;\sigma_{x_n,x_n}&space;&&space;\sigma_{x_n,y_n}&space;&space;\\\sigma_{y_n&space;x}&space;&&space;&space;\sigma_{y_ny}&&space;\sigma_{y_n\theta}&space;&&space;\sigma_{y_nx1}&space;&&space;\sigma_{y_ny1}&space;&&space;...&&space;\sigma_{y_n,x_n}&space;&&space;\sigma_{y_n,y_n}\\\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline P = \begin{bmatrix}\sigma_{xx} & \sigma_{xy}& \sigma_{x\theta} & \sigma_{xx1} & \sigma_{xy1} & ...& \sigma_{x,x_n} & \sigma_{x,y_n} \\\sigma_{yx} & \sigma_{yy}& \sigma_{y\theta} & \sigma_{yx1} & \sigma_{yy1} & ...& \sigma_{y,x_n} & \sigma_{y,y_n} \\\sigma_{x_n x} & \sigma_{x_ny}& \sigma_{x_n\theta} & \sigma_{x_nx1} & \sigma_{x_ny1} & ...& \sigma_{x_n,x_n} & \sigma_{x_n,y_n} \\\sigma_{y_n x} & \sigma_{y_ny}& \sigma_{y_n\theta} & \sigma_{y_nx1} & \sigma_{y_ny1} & ...& \sigma_{y_n,x_n} & \sigma_{y_n,y_n}\\\end{bmatrix}" />

A single estimate of the pose is tracked over time, while the confidence in the pose is tracked by the covariance matrix P. P is a symmetric square matrix which each element in the matrix corresponding to the covariance between two parts of the system. For example, 
 <img src="https://latex.codecogs.com/svg.image?\inline&space;\sigma_{xy}" title="https://latex.codecogs.com/svg.image?\inline \sigma_{xy}" /> represents the covariance between the belief of <img src="https://latex.codecogs.com/svg.image?\inline&space;x" title="https://latex.codecogs.com/svg.image?\inline x" /> and <img src="https://latex.codecogs.com/svg.image?\inline&space;y" title="https://latex.codecogs.com/svg.image?\inline y" /> and is equal to <img src="https://latex.codecogs.com/svg.image?\inline&space;\sigma_{yx}" title="https://latex.codecogs.com/svg.image?\inline \sigma_{yx}" />.
 
 The state can be represented more concisely as following:
 
 <img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{X}&space;=&space;\begin{bmatrix}x&space;\\&space;m\end{bmatrix}&space;P&space;=&space;\begin{bmatrix}\sum_{xx}&space;&&space;\sum_{xm}&space;\\\sum_{mx}&space;&&space;\sum_{mm}&space;\\\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline \textbf{X} = \begin{bmatrix}x \\ m\end{bmatrix} P = \begin{bmatrix}\sum_{xx} & \sum_{xm} \\\sum_{mx} & \sum_{mm} \\\end{bmatrix}" />
 
 Here the state simplifies to a combination of pose ( <img src="https://latex.codecogs.com/svg.image?\inline&space;x" title="https://latex.codecogs.com/svg.image?\inline x" />) and map (<img src="https://latex.codecogs.com/svg.image?\inline&space;m" title="https://latex.codecogs.com/svg.image?\inline m" />). The covariance matrix becomes easier to understand and simply reads as the uncertainty of the robots pose (<img src="https://latex.codecogs.com/svg.image?\inline&space;\sum_{xx}" title="https://latex.codecogs.com/svg.image?\inline \sum_{xx}" />), the uncertainty of the map (<img src="https://latex.codecogs.com/svg.image?\inline&space;\sum_{mm}" title="https://latex.codecogs.com/svg.image?\inline \sum_{mm}" />), and the uncertainty of the robots pose with respect to the map and vice versa (<img src="https://latex.codecogs.com/svg.image?\inline&space;\sum_{xm},&space;\sum_{mx}" title="https://latex.codecogs.com/svg.image?\inline \sum_{xm}, \sum_{mx}" />).

## EKF SLAM algorithm walk through
At each time step, the following is done:
- predict the new state using the control functions 

- update the belief in landmark positions based on the estimated state and measurements

### Predict
Predict State update: The following equations describe the predicted motion model of the robot in case we provide only the control <img src="https://latex.codecogs.com/svg.image?\inline&space;(v,w)" title="https://latex.codecogs.com/svg.image?\inline (v,w)" />, which are the linear and angular velocity respectively.

<img src="https://latex.codecogs.com/svg.image?\inline&space;F&space;=&space;\begin{bmatrix}1&space;&&space;0&space;&&space;0&space;\\0&space;&&space;1&space;&&space;0&space;\\0&space;&&space;0&space;&&space;1&space;\\\end{bmatrix},&space;B&space;=&space;\begin{bmatrix}\Delta&space;t&space;cos(\theta)&space;&&space;0&space;\\\Delta&space;t&space;sin(\theta)&space;&&space;0&space;\\0&space;&&space;\Delta&space;t&space;\\\end{bmatrix},&space;U&space;=&space;\begin{bmatrix}v_t&space;\\w_t\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline F = \begin{bmatrix}1 & 0 & 0 \\0 & 1 & 0 \\0 & 0 & 1 \\\end{bmatrix}, B = \begin{bmatrix}\Delta t cos(\theta) & 0 \\\Delta t sin(\theta) & 0 \\0 & \Delta t \\\end{bmatrix}, U = \begin{bmatrix}v_t \\w_t\end{bmatrix}" />

Thus, the motion model is:

<img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{X}_{t&plus;1}&space;=&space;F\textbf{X}_{t}&plus;B\begin{bmatrix}v_t&space;&plus;&space;\sigma_v&space;\\w_t&space;&plus;&space;\sigma_w\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline \textbf{X}_{t+1} = F\textbf{X}_{t}+B\begin{bmatrix}v_t + \sigma_v \\w_t + \sigma_w\end{bmatrix}" />

Notice that while <img src="https://latex.codecogs.com/svg.image?\inline&space;U" title="https://latex.codecogs.com/svg.image?\inline U" />  is only defined by <img src="https://latex.codecogs.com/svg.image?\inline&space;v_t" title="https://latex.codecogs.com/svg.image?\inline v_t" />
 and <img src="https://latex.codecogs.com/svg.image?\inline&space;w_t" title="https://latex.codecogs.com/svg.image?\inline w_t" />, in the actual calculations, a <img src="https://latex.codecogs.com/svg.image?\inline&space;&plus;\sigma_v" title="https://latex.codecogs.com/svg.image?\inline +\sigma_v" />
 and <img src="https://latex.codecogs.com/svg.image?\inline&space;&plus;\sigma_w" title="https://latex.codecogs.com/svg.image?\inline +\sigma_w" />
 appear. These values represent the error between the given control inputs and the actual control inputs.

As a result, the simulation is set up as the following. R represents the process noise which is added to the control inputs to simulate noise experienced in the real world. A set of truth values are computed from the raw control values while the values dead reckoning values incorporate the error into the estimation:

<img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{X}_{true}&space;=&space;FX&plus;B(U)\\\textbf{X}_{DR}&space;=&space;FX&plus;B(U&plus;R),R&space;=&space;\begin{bmatrix}\sigma_v&space;\\&space;\sigma_w\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline \textbf{X}_{true} = FX+B(U)\\\textbf{X}_{DR} = FX+B(U+R),R = \begin{bmatrix}\sigma_v \\ \sigma_w\end{bmatrix}" />

The implementation of the motion model prediciton code is shown in "motion_model" function of the provided code [ekf_slam.py](source/ekf_slam.py). The "observation" function in  [ekf_slam.py](source/ekf_slam.py) shows how the simulation uses (or doesn’t use) the process noise Rsim to the find the ground truth and dead reckoning estimates of the pose.

### Update
In the update phase, the observations of nearby landmarks are used to correct the location estimate. For every landmark observed, it is associated to a particular landmark in the known map. If no landmark exists in the position surrounding the landmark, it is taken as a NEW landmark. The distance threshold for how far a landmark must be from the next known landmark before its considered to be a new landmark is set by M_DIST_TH.

With an observation associated to the appropriate landmark, the innovation can be calculated. Innovation (<img src="https://latex.codecogs.com/svg.image?\inline&space;y" title="https://latex.codecogs.com/svg.image?\inline y" />) is the difference between the observation and the observation that should have been made if the observation were made from the pose predicted in the predict stage:

<img src="https://latex.codecogs.com/svg.image?\inline&space;y&space;=&space;z_t&space;-&space;h(\textbf{X})" title="https://latex.codecogs.com/svg.image?\inline y = z_t - h(\textbf{X})" />

With the innovation calculated, the question becomes which to trust more - the observations or the predictions? To determine this, we calculate the Kalman Gain K - a percent of how much of the innovation to add to the prediction based on the uncertainty in the predict step and the update step:

<img src="https://latex.codecogs.com/svg.image?\inline&space;K&space;=&space;\overline{P}_t&space;H_t^T(H_t&space;\overline{P}_t&space;H_t^T&space;&plus;&space;Q_t)^{-1}" title="https://latex.codecogs.com/svg.image?\inline K = \overline{P}_t H_t^T(H_t \overline{P}_t H_t^T + Q_t)^{-1}" />

where H is the jacobian of the measurement function. 

The update is captured in the following:

<img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{X}_{Update}&space;=&space;X_{predict}&space;&plus;&space;K*y" title="https://latex.codecogs.com/svg.image?\inline \textbf{X}_{Update} = X_{predict} + K*y" />

<img src="https://latex.codecogs.com/svg.image?\inline&space;P_t&space;=&space;(I-K_tH_t)\overline{P}_t" title="https://latex.codecogs.com/svg.image?\inline P_t = (I-K_tH_t)\overline{P}_t" />


### Observation Step
The observation step described here is outside the main EKF SLAM process and is primarily used as a method of driving the simulation. The observations function is in charge of calculating how the poses of the robots change and accumulate error over time, and the theoretical measurements that are expected as a result of each measurement.

Observations are based on the TRUE position of the robot. Error in dead reckoning and control functions are passed along here as well.
Please refer to the function "observation" in the code file [ekf_slam.py](source/ekf_slam.py)

# Fast SLAM

## simulation 

<div align=left> <img src=source/animation.gif width=50%/> </div>

This demo shows the example of landmark feature based FastSLAM using particle filters.

- The blue line is the true trajectory

- The red line is the estimated trajectory

- The red dots represent the distribution of particles

- The black line represent dead reckoning tracjectory

- The blue x is the observed and estimated landmarks

- The black x is the true landmark

As it is shown, the particle filter differs from EKF by representing the robot’s estimation through a set of particles. Each single particle has an independent belief, as it holds the pose <img src="https://latex.codecogs.com/svg.image?\inline&space;(x,y,\theta&space;)" title="https://latex.codecogs.com/svg.image?\inline l(m_i|z_t,x_t)" /> and an array of landmarks <img src = "https://latex.codecogs.com/svg.image?\inline&space;[(x_1,y_1),&space;(x_2,y_2),...,(x_n,y_n)]"/> for n landmarks.

I.e. Each particle maintains a deterministic pose and n-EKFs for each landmark and update it with each measurement.

The particles are initially drawn from a uniform distribution the represent the initial uncertainty. At each time step we do:

- Predict the pose for each particle by using control input u and the motion model (the landmarks are not updated).

- Update the particles with observations z, where the weights are adjusted based on how likely the particle to have the correct pose given the sensor measurement

- Resampling such that the particles with the largest weights survive and the unlikely ones with the lowest weights die out.

### Predict
The predict step is the same as that of landmarks based EKF-SLAM.
From the equations, we can see how the particles distribution evolves.
To get the insight of the motion model change the value of  and re-run the cells again. As R is the parameters that indicates how much we trust that the robot executed the motion commands.
It is interesting to notice also that only motion will increase the uncertainty in the system as the particles start to spread out more. If observations are included the uncertainty will decrease and particles will converge to the correct estimate.
Please refer to the functions "motion_model" and "predict_particles" implementations in [pf_slam.py](source/pf_slam.py).

### Update
For the update step it is useful to observe a single particle and the effect of getting a new measurements on the weight of the particle.
The weight of the particle is updated according to the following equation:

<img src="https://latex.codecogs.com/svg.image?\inline&space;w_i&space;=&space;|2\pi&space;Q|^{-\frac{1}{2}}exp(\frac{-1}{2}(z_t-\hat{z}_i)^TQ^{-1}(z_t-\hat{z}_i))" title="https://latex.codecogs.com/svg.image?\inline w_i = |2\pi Q|^{-\frac{1}{2}}exp(\frac{-1}{2}(z_t-\hat{z}_i)^TQ^{-1}(z_t-\hat{z}_i))" />

Where, <img src="https://latex.codecogs.com/svg.image?\inline&space;w_i" title="https://latex.codecogs.com/svg.image?\inline w_i" /> is the computed weight, <img src="https://latex.codecogs.com/svg.image?\inline&space;Q" title="https://latex.codecogs.com/svg.image?\inline Q" /> is the measurement covariance, <img src="https://latex.codecogs.com/svg.image?\inline&space;z_t" title="https://latex.codecogs.com/svg.image?\inline z_t" /> is the actual measurment and <img src="https://latex.codecogs.com/svg.image?\inline&space;\hat{z}_i" title="https://latex.codecogs.com/svg.image?\inline \hat{z}_i" />
 is the predicted measurement of particle i.
 
To experiment this, a single particle is initialized then passed an initial measurement, which results in a relatively average weight. However, setting the particle coordinate to a wrong value to simulate wrong estimation will result in a very low weight. The lower the weight the less likely that this particle will be drawn during resampling and probably will die out.


### Resampling
In the reseampling steps a new set of particles are chosen from the old set. This is done according to the weight of each particle.

The following figure shows 100 particles distributed uniformly between [-0.5, 0.5] with the weights of each particle distributed according to a Gaussian funciton.

<div align=left> <img src=source/sampling.png width=50%/> </div>

----
## Task 1
The prediction, update and Jacobian functions are given, please implement the "**fast_slam1**" processing of EKF-SLAM and print the final experimental result using the provided visualization function.

## Task 2
The basic functions such as prediction, update, Jacobian, weight calculation and resampling functions given, please implement the "**fast_slam1**" function of particle slam and print the final experimental result using the provided visualization function.

## Code instructions for tasks
**Note1** [ekf_slam.py](source/ekf_slam.py) give the implememtation framework of the task1, please complete the ekf_slam function.

**Note2** [pf_slam.py](source/pf_slam.py) give the implememtation framework of the task2.
