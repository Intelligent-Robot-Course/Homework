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
