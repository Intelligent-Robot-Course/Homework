
# Homework 6 - Robot Perception

-- Course: *Intelligent Robotics – Professor: Qi Hao*

**Coding Homeworks.** Your final submission should be a compressed package with extension .zip, which includes your codes and explanations (you need to know how to write the manuscript with Markdown or LATEX). Your code should be run step-by-step without any error. Real-time animation is also recommended.

----

## Overview
The homework contains range-only based localization and robot motion model.

## Range only based localization
Range only based localization is the technique of using only distance measurements from stations to determine the location of a target, with no information about the direction from which this distance was measured. Given a coordinate and a measured distance, the set of all points for which the target could be located forms a circle; the coordinate is the circle center and the distance is the circle radius. It is a classic problem in navigation and target tracking, and also applicable to problems such as using time-domain reflectometry to determine locations of faults in modem connections.
For example, a GPS receiver uses trilateration (a type of range only based localization algorithms) to determine its exact location from its measured distances from at least three satellites, each satellite is at the center of a sphere and where they all intersect is the position of the GPS receiver.
For detail of GPS localization, please refer to [How GPS Receivers Work - Trilateration vs Triangulation](https://gisgeography.com/trilateration-triangulation-gps/).

### Localization of a single target
To simplify the problem, here we only consider the location in the two-dimensional plane.
We simulates an 802.11az network consisting of a station (STA) and multiple access points (APs). With only one station (STA), there are infinitely many points on the circle where the targets could be located. With two stations whose distance circles intersect, the possible target location is reduced down to two possible points. With three or more stations that intersect at a single point, the target location can be isolated to that point.
Thus, to estimate the position of a STA, the network requires a minimum of three APs. 

The following demo simulates a ranging measurement exchange for each STA-AP pair, then trilaterates the position of the STA by using these distance measurements.
<div align=center> <img src=gif/demo.gif width=50%/> </div>

Suppose the known coordinates of AP1, AP2 and AP3 are <img src="https://latex.codecogs.com/svg.image?(x_1,y_1),&space;(x_2,y_2)" title="https://latex.codecogs.com/svg.image?(x_1,y_1), (x_2,y_2)" /> and <img src="https://latex.codecogs.com/svg.image?(x_3,y_3)" title="https://latex.codecogs.com/svg.image?(x_3,y_3)" />, respectively.
Also, the calculated distances from AP1, AP2, and AP3 to the STA are <img src="https://latex.codecogs.com/svg.image?d_1,&space;d_2" title="https://latex.codecogs.com/svg.image?d_1, d_2" /> and <img src="https://latex.codecogs.com/svg.image?d_3" title="https://latex.codecogs.com/svg.image?d_3" />, respectively.

### Task 1
How to calculate the exact position <img src="https://latex.codecogs.com/svg.image?(x,y)" title="https://latex.codecogs.com/svg.image?(x,y)" /> of the STA in the current coordinte space? 
*Note1:* Linear least square method can be used to solve the problem analytically.

**Mathematical Derivation**
The distance equations between known APs and unknown STA are as following:


<img src="https://latex.codecogs.com/svg.image?\left\{\begin{matrix}(x_1-x)^2&plus;(y_1-y)^2=d_1^2\\(x_2-x)^2&plus;(y_2-y)^2=d_2^2\\(x_3-x)^2&plus;(y_3-y)^2=d_3^2\\\end{matrix}\right." title="https://latex.codecogs.com/svg.image?\left\{\begin{matrix}(x_1-x)^2+(y_1-y)^2=d_1^2\\(x_2-x)^2+(y_2-y)^2=d_2^2\\(x_3-x)^2+(y_3-y)^2=d_3^2\\\end{matrix}\right." />

As we can see these equations are nonlinear, and we substract the third equation from the first and second equations, after that we can can obtain a linear equation:


<img src="https://latex.codecogs.com/svg.image?A\textbf{X}=\textbf{b}" title="https://latex.codecogs.com/svg.image?A\textbf{X}=\textbf{b}" />

where 
<img src="https://latex.codecogs.com/svg.image?\inline&space;A=\begin{bmatrix}2(x_1-x_3)&space;&&space;2(y_1-y_3)&space;\\2(x_2-x_3)&space;&&space;2(y_2-y_3)&space;\\\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline A=\begin{bmatrix}2(x_1-x_3) & 2(y_1-y_3) \\2(x_2-x_3) & 2(y_2-y_3) \\\end{bmatrix}" />, <img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{b}=\begin{bmatrix}x_1^2-x_3^2&plus;y_1^2-y_3^2&plus;d_3^2-d_1^2&space;\\x_2^2-x_3^2&plus;y_2^2-y_3^2&plus;d_3^2-d_2^2\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline \textbf{b}=\begin{bmatrix}x_1^2-x_3^2+y_1^2-y_3^2+d_3^2-d_1^2 \\x_2^2-x_3^2+y_2^2-y_3^2+d_3^2-d_2^2\end{bmatrix}" /> and <img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{X}=\begin{bmatrix}x,y\end{bmatrix}^T" title="https://latex.codecogs.com/svg.image?\inline \textbf{X}=\begin{bmatrix}x,y\end{bmatrix}^T" />

Least square method can be used to solve this linear equation and the solver is:
<img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{X}&space;=&space;(A^TA)^{-1}(A^T\textbf{b})" title="https://latex.codecogs.com/svg.image?\inline \textbf{X} = (A^TA)^{-1}(A^T\textbf{b})" />



 ### Task 2
However, even with accurate sensors, it is unlikely that three circles would intersect at exactly the same point at which the STA is located. This means that attempts to tackle this problem analytically will almost always fail. Instead, an optimization-based approach can be used; it infers the STA's location by finding the point which minimizes the squared euclidean distances between the STA and all the APs.
Please **formulate an error function** which calculates the euclidean distance between the STA and all APs:

<img src="https://latex.codecogs.com/svg.image?\sum_{i=1}^{k}\left&space;(\left\|AP_i-X&space;\right\|_2-d_i\right&space;)^2" title="https://latex.codecogs.com/svg.image?\sum_{i=1}^{k}\left (\left\|AP_i-X \right\|_2-d_i\right )^2" />

where <img src="https://latex.codecogs.com/svg.image?\inline&space;k" title="https://latex.codecogs.com/svg.image?\inline k" /> is the total number of APs.


### Task 3
This problem is not convex. It is also worth noting that gradeint-based optimization methods such as [Gauss-Newton(GN)](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm) and [Levenberg–Marquardt (LM)](https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm#:~:text=In%20mathematics%20and%20computing%2C%20the,in%20least%20squares%20curve%20fitting.) algorithm used require a Jacobian (gradient) function. Thus, in this homework, we solve the problem using numerical optimization methods which are derivative-free methods. For example, [Covariance matrix adaptation evolution strategy (CMA-ES)](https://en.wikipedia.org/wiki/CMA-ES) which uses the principle of biological evolution, namely the repeated interplay of variation (via recombination and mutation) and selection: in each generation (iteration) new individuals (candidate solutions) are generated by variation, usually in a stochastic way, of the current parental individuals. Then, some individuals are selected to become the parents in the next generation based on their fitness or objective function value. Like this, over the generation sequence, individuals with better and better function values are generated. 
Please use CMA-ES algorithm to solve the localization problem, you can refer to the usage of CMA-ES in python from the [link](https://github.com/CyberAgentAILab/cmaes).


### Code for tasks
**Note1:** The question one is simple, please finish the function code in **[trilateration.py](source/trilateration.py)**  by refering to the above mathematical derivation.

**Note2:** Given the coordinates of a finite number of radio stations, and given their distances to the source (derived from the intensities of the signal they received in a previous step) computes the most probable coordinates of the source, please complete the **quadratic** function (the error function formulation) in **[distance_only_localization.py](source/distance_only_localization.py)**.

**Note3:** Please complete the optimization section of main function in the file **[distance_only_localization.py](source/distance_only_localization.py)**


## Robot Motion Models

You will implement the velocity-based odometry, encoder-based differential odometry and accelerometer-gyroscope-based dead reckoning models in Python.
Corresponding code skeltons are provided for you to implement the motion models.

----
### Robot motion models

A working robot motion model is a requirement for all Bayes Filter implementations. 
In practice, the following three types of robot motion models are often used:

-- **velocity-based models**, cacluclating odometry for mobile robot using data from velocity readings:

<img src="https://latex.codecogs.com/svg.image?\inline&space;\left\{\begin{matrix}\dot{x}&space;=&space;vcos(\theta)&space;\\\dot{y}&space;=&space;vsin(\theta)&space;\\\dot{\theta}&space;=&space;w\end{matrix}\right." title="https://latex.codecogs.com/svg.image?\inline \left\{\begin{matrix}\dot{x} = vcos(\theta) \\\dot{y} = vsin(\theta) \\\dot{\theta} = w\end{matrix}\right." />


<img src="https://latex.codecogs.com/svg.image?\inline&space;\left\{\begin{matrix}v&space;=&space;\frac{v_R&space;&plus;&space;v_L}{2}&space;\\w&space;=&space;\frac{v_R-v_L}{L}\end{matrix}\right." title="https://latex.codecogs.com/svg.image?\inline \left\{\begin{matrix}v = \frac{v_R + v_L}{2} \\w = \frac{v_R-v_L}{L}\end{matrix}\right." />

<img src="https://latex.codecogs.com/svg.image?\inline&space;\left\{\begin{matrix}\Delta&space;x&space;=&space;v\Delta_t&space;cos(\theta)&space;\\\Delta&space;y&space;=&space;v\Delta_t&space;sin(\theta)&space;\\\Delta&space;\theta&space;=&space;w\Delta_t\end{matrix}\right." title="https://latex.codecogs.com/svg.image?\inline \left\{\begin{matrix}\Delta x = v\Delta_t cos(\theta) \\\Delta y = v\Delta_t sin(\theta) \\\Delta \theta = w\Delta_t\end{matrix}\right." />

<img src="https://latex.codecogs.com/svg.image?\inline&space;\left\{\begin{matrix}x=&space;\int&space;\dot{x}dt&space;\\y=&space;\int&space;\dot{y}dt&space;\\\theta&space;=&space;\int&space;\dot{\theta}dt\end{matrix}\right." title="https://latex.codecogs.com/svg.image?\inline \left\{\begin{matrix}x= \int \dot{x}dt \\y= \int \dot{y}dt \\\theta = \int \dot{\theta}dt\end{matrix}\right." />

where

- <img src="https://latex.codecogs.com/svg.image?\inline&space;x,y" title="https://latex.codecogs.com/svg.image?\inline x,y" /> - the 2D position

- <img src="https://latex.codecogs.com/svg.image?\inline&space;\theta" title="https://latex.codecogs.com/svg.image?\inline \theta" /> - the robot's orientation

- <img src="https://latex.codecogs.com/svg.image?\inline&space;\upsilon&space;" title="https://latex.codecogs.com/svg.image?\inline \upsilon " /> - the robot's velocity

- <img src="https://latex.codecogs.com/svg.image?\inline&space;v_L" title="https://latex.codecogs.com/svg.image?\inline v_L" /> - the left wheel's velocity reading

- <img src="https://latex.codecogs.com/svg.image?\inline&space;v_R" title="https://latex.codecogs.com/svg.image?\inline v_R" /> -  the right wheel's velocity reading

- <img src="https://latex.codecogs.com/svg.image?\inline&space;\omega" title="https://latex.codecogs.com/svg.image?\inline \omega" /> - the robot's angular velocity

- <img src="https://latex.codecogs.com/svg.image?\inline&space;L" title="https://latex.codecogs.com/svg.image?\inline L" /> - the distance between wheels

- <img src="https://latex.codecogs.com/svg.image?\inline&space;\Delta_t" title="https://latex.codecogs.com/svg.image?\inline \Delta_t" /> - the time interval.


-- **Encoder-based differential odometry**, which are used when systems are equipped with wheel encoders and encoder readings are used to calculate odometry:

<img src="https://latex.codecogs.com/svg.image?\inline&space;\left\{\begin{matrix}\Delta&space;x&space;=&space;(\Delta&space;E_{encL}&space;&plus;&space;\Delta&space;E_{encR})\frac{cos(\theta)}{2T_{pr}}\pi&space;d&space;\\\Delta&space;y&space;=&space;(\Delta&space;E_{encL}&space;&plus;&space;\Delta&space;E_{encR})\frac{sin(\theta)}{2T_{pr}}\pi&space;d&space;\\\Delta&space;\theta&space;=&space;(\Delta&space;E_{encL}&space;-&space;\Delta&space;E_{encR})\frac{\pi&space;d}{L.T_{pr}}\end{matrix}\right." title="https://latex.codecogs.com/svg.image?\inline \left\{\begin{matrix}\Delta x = (\Delta E_{encL} + \Delta E_{encR})\frac{cos(\theta)}{2T_{pr}}\pi d \\\Delta y = (\Delta E_{encL} + \Delta E_{encR})\frac{sin(\theta)}{2T_{pr}}\pi d \\\Delta \theta = (\Delta E_{encL} - \Delta E_{encR})\frac{\pi d}{L.T_{pr}}\end{matrix}\right." />

where

- <img src="https://latex.codecogs.com/svg.image?\inline&space;d" title="https://latex.codecogs.com/svg.image?\inline d" /> - diameter of the wheels

- <img src="https://latex.codecogs.com/svg.image?\inline&space;v_R&space;=&space;\frac{d}{2}w_R" title="https://latex.codecogs.com/svg.image?\inline v_R = \frac{d}{2}w_R" /> - velocity of the right wheel

- <img src="https://latex.codecogs.com/svg.image?\inline&space;v_L&space;=&space;\frac{d}{2}w_L" title="https://latex.codecogs.com/svg.image?\inline v_L = \frac{d}{2}w_L" /> - velocity of the left wheel

- <img src="https://latex.codecogs.com/svg.image?\inline&space;T_{pr}" title="https://latex.codecogs.com/svg.image?\inline T_{pr}" /> - pules per revolution

- <img src="https://latex.codecogs.com/svg.image?\inline&space;E_{enc}" title="https://latex.codecogs.com/svg.image?\inline E_{enc}" /> - encoder increment

-- **accelerometer-gyroscope-based dead reckoning models**, they use the motion sensors to estimate the change in position and orientation over time:

<img src="https://latex.codecogs.com/svg.image?\inline&space;\left\{\begin{matrix}\Delta&space;x&space;=&space;v\Delta_t&space;cos(\theta)&space;\\\Delta&space;y&space;=&space;v\Delta_t&space;sin(\theta)&space;\\\Delta&space;\theta&space;=&space;w\Delta_t\end{matrix}\right." title="https://latex.codecogs.com/svg.image?\inline \left\{\begin{matrix}\Delta x = v\Delta_t cos(\theta) \\\Delta y = v\Delta_t sin(\theta) \\\Delta \theta = w\Delta_t\end{matrix}\right." />

where 
- <img src="https://latex.codecogs.com/svg.image?\inline&space;\theta" title="https://latex.codecogs.com/svg.image?\inline \theta" /> - the robot's heading obtained from the motion sensor

- <img src="https://latex.codecogs.com/svg.image?\inline&space;\upsilon&space;" title="https://latex.codecogs.com/svg.image?\inline \upsilon " /> - the robot's velocity obtained from the motion sensor.

Notice that the input and observation vector includes sensor noise, thus the estimated trajectory will have drift compared to its ground truth trajectory, the following image shows the comparison between estimated trajectory and ground truth:
<div align=center> <img src=data/fig_traj.png width=50%/> </div>

----
### Task 1
Please implement the velocity-based odometry in Python.

### Task 2
Please implement the encoder-based differential odometry in Python.

### Task 3
Running the velocity-based odometry with noise (by setting the bool switch in the function) and compare the ground truth trajectory and the estimated trajectory.

### Task 4
Running the encoder-based differential odometry with noise (by setting the bool switch in the function) and compare the ground truth trajectory and the estimated trajectory.

### Extra credit
Please implement the ICC-based differential drive model (see the below equations)：

<div align=center> <img src=gif/1648955007452.jpg width=50%/> </div>

----
### Code for tasks
**Note1**
- **[calculate_odometry.py](code/caclculate_odometry.py)** - main script
- data - direcotry with example data:
-forward.csv, backward.csv - motion length 1.15m
-left_full_turn.csv, right_full_turn.csv - full angle rotation
-square_right.csv, square_left.csv - square side length = 1.15m and return to initial pose
- Implement the function of **calculate_odometry_velocity** in **[calculate_odometry.py](code/caclculate_odometry.py)**.

**Note2**
- Implement the function of **calculate_odometry_encoders** in **[calculate_odometry.py](code/caclculate_odometry.py)**.

- data - direcotry with example data:
- forward.csv, backward.csv - motion length 1.15m
- left_full_turn.csv, right_full_turn.csv - full angle rotation
- square_right.csv, square_left.csv - square side length = 1.15m and return to initial pose

