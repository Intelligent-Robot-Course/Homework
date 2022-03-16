
# Homework 6 - Multilateration-based location estimation

-- Course: *Intelligent Robotics – Professor: Qi Hao*

**Coding Homeworks.** Your final submission should be a compressed package with extension .zip, which includes your codes and explanations (you need to know how to write the manuscript with Markdown or LATEX). Your code should be run step-by-step without any error. Real-time animation is also recommended.

----

## Overview
Multilateration is the technique of using only distance measurements from stations to determine the location of a target, with no information about the direction from which this distance was measured. Given a coordinate and a measured distance, the set of all points for which the target could be located forms a circle; the coordinate is the circle center and the distance is the circle radius. Multilateration is a classic problem in navigation and target tracking, and also applicable to problems such as using time-domain reflectometry to determine locations of faults in modem connections.
For example, a GPS receiver uses multilateration to determine its exact location from its measured distances from at least three satellites, each satellite is at the center of a sphere and where they all intersect is the position of the GPS receiver.
For detail of GPS localization, please refer to [How GPS Receivers Work - Trilateration vs Triangulation](https://gisgeography.com/trilateration-triangulation-gps/).

## Multilateration of a single target
To simplify the problem, here we only consider the Multilateration-based location in the two-dimensional plane.
We simulates an 802.11az network consisting of a station (STA) and multiple access points (APs). With only one station (STA), there are infinitely many points on the circle where the targets could be located. With two stations whose distance circles intersect, the possible target location is reduced down to two possible points. With three or more stations that intersect at a single point, the target location can be isolated to that point.
Thus, to estimate the position of a STA, the network requires a minimum of three APs. 

The following demo simulates a ranging measurement exchange for each STA-AP pair, then trilaterates the position of the STA by using these distance measurements.
<div align=center> <img src=gif/demo.gif width=50%/> </div>

Suppose the known coordinates of AP1, AP2 and AP3 are <img src="https://latex.codecogs.com/svg.image?(x_1,y_1),&space;(x_2,y_2)" title="https://latex.codecogs.com/svg.image?(x_1,y_1), (x_2,y_2)" /> and <img src="https://latex.codecogs.com/svg.image?(x_3,y_3)" title="https://latex.codecogs.com/svg.image?(x_3,y_3)" />, respectively.
Also, the calculated distances from AP1, AP2, and AP3 to the STA are <img src="https://latex.codecogs.com/svg.image?d_1,&space;d_2" title="https://latex.codecogs.com/svg.image?d_1, d_2" /> and <img src="https://latex.codecogs.com/svg.image?d_3" title="https://latex.codecogs.com/svg.image?d_3" />, respectively.

**Then, the question is how to calculate the exact position <img src="https://latex.codecogs.com/svg.image?(x,y)" title="https://latex.codecogs.com/svg.image?(x,y)" /> of the STA in the current coordinte space.**

## Mathematical Derivation
The distance equations between known APs and unknown STA are as following:


<img src="https://latex.codecogs.com/svg.image?\left\{\begin{matrix}(x_1-x)^2&plus;(y_1-y)^2=d_1^2\\(x_2-x)^2&plus;(y_2-y)^2=d_2^2\\(x_3-x)^2&plus;(y_3-y)^2=d_3^2\\\end{matrix}\right." title="https://latex.codecogs.com/svg.image?\left\{\begin{matrix}(x_1-x)^2+(y_1-y)^2=d_1^2\\(x_2-x)^2+(y_2-y)^2=d_2^2\\(x_3-x)^2+(y_3-y)^2=d_3^2\\\end{matrix}\right." />

As we can see these equations are nonlinear, and we substract the third equation from the first and second equations, after that we can can obtain a linear equation:


<img src="https://latex.codecogs.com/svg.image?A\textbf{X}=\textbf{b}" title="https://latex.codecogs.com/svg.image?A\textbf{X}=\textbf{b}" />

where 
<img src="https://latex.codecogs.com/svg.image?\inline&space;A=\begin{bmatrix}2(x_1-x_3)&space;&&space;2(y_1-y_3)&space;\\2(x_2-x_3)&space;&&space;2(y_2-y_3)&space;\\\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline A=\begin{bmatrix}2(x_1-x_3) & 2(y_1-y_3) \\2(x_2-x_3) & 2(y_2-y_3) \\\end{bmatrix}" />, <img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{b}=\begin{bmatrix}x_1^2-x_3^2&plus;y_1^2-y_3^2&plus;d_3^2-d_1^2&space;\\x_2^2-x_3^2&plus;y_2^2-y_3^2&plus;d_3^2-d_2^2\end{bmatrix}" title="https://latex.codecogs.com/svg.image?\inline \textbf{b}=\begin{bmatrix}x_1^2-x_3^2+y_1^2-y_3^2+d_3^2-d_1^2 \\x_2^2-x_3^2+y_2^2-y_3^2+d_3^2-d_2^2\end{bmatrix}" /> and <img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{X}=\begin{bmatrix}x,y\end{bmatrix}^T" title="https://latex.codecogs.com/svg.image?\inline \textbf{X}=\begin{bmatrix}x,y\end{bmatrix}^T" />

Least square method can be used to solve this linear equation and the solver is:
<img src="https://latex.codecogs.com/svg.image?\inline&space;\textbf{X}&space;=&space;(A^TA)^{-1}(A^T\textbf{b})" title="https://latex.codecogs.com/svg.image?\inline \textbf{X} = (A^TA)^{-1}(A^T\textbf{b})" />



 


