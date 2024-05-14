# Homework 7 - Kalman and Particle Filter 
**history homework**

-- Course: *Intelligent Robotics – Professor: Qi Hao*

**Coding Homeworks.** Your final submission should be a compressed package with extension .zip, which includes your codes and explanations (you need to know how to write the manuscript with Markdown or LATEX). Your code should be run step-by-step without any error. Real-time animation is also recommended.

----


## Overview
You will be implementing a simple 1-Dimensional vehicle tracker using Kalman Filter. Corresponding code skeltons are provided for you to implement the two filters. Also, the visulization of the filters are provided in the framework.

----

## 1D-Kalman-Filter 
Kalman Filter, which is an algorithm that uses noisy sensor measurements (and Bayes' Rule) to produce reliable estimates of unknown quantities (e.g. like where a vehicle is likely to be in 3 seconds) , represents a mathematical way to infer velocity from only a set of measured locations. Using Kalman Filter, we can estimates where future locations might be and the velocity of an object from intial parameters like positions and uncertainty.

### Objective 
In order to actually implement a Kalman Filter in a 2D or 3D world (or "state space" in the language of robotics) this 1D Kalman Filter can show the basic idea  how to keep track of robot motion and "state" (robot of a self-driving-car).

### Motion Models and State
A mathematical representation of motion: a motion model represents the position and motion of an object (an object's state). 

### Step 

**1. Gaussian Calculation**
Gaussians are exponential function characterized by a given mean, which defines the location of the peak of a Gaussian curve, ad a variance which defines the width/spread of the curve. The variance is also a measure of Gaussian spread and a measure of certainty. To find the location of a car with the most certainty, we can apply a Gaussian whose mean is the location of the car and with the smallest uncertainty/spread. 

In detail, we know that Gaussian equations contain two main parameters:

- a mean <img src="https://latex.codecogs.com/svg.image?\inline&space;\mu&space;" title="https://latex.codecogs.com/svg.image?\inline \mu " />, and
- a variance, often written as its square value, <img src="https://latex.codecogs.com/svg.image?\inline&space;\sigma&space;^{2}" title="https://latex.codecogs.com/svg.image?\inline \sigma ^{2}" />.

The general Gaussian equation looks like this:

<img src="https://latex.codecogs.com/svg.image?\inline&space;p(x)&space;=&space;\frac{1}{\sqrt{2&space;\pi}\sigma^2&space;}e^{-(x-\mu)^2/2\sigma^2}" title="https://latex.codecogs.com/svg.image?\inline p(x) = \frac{1}{\sqrt{2 \pi}\sigma^2 }e^{-(x-\mu)^2/2\sigma^2}" />


 

Where we'll call the first part of the equation the coefficient and the second part the exponential. This second part is most important in defining the shape of the Gaussian (the coefficient is a normalizing term).

For uncertain, continuous quantities, such as the estimated location of a self-driving car, we use Gaussians to represent uncertainty in that quantity. The smaller the variance, the more certain we are about a quantity.


**2. Mean and Variance**
After applying Gaussian, motion needs to be updated .This step is called the parameter or measurement update because it is the update that happens when an initial belief (represented by the Gaussian) is merged with a new piece of information, a measurement with some uncertainty (another Gaussian). By the charateristics of Gaussians, a motion update is just an addition between parameters; the new mean will be the old mean + the motion mean; same with the new variance.

Now let's take the formulas from the example below and use them to write a program that takes in two means and variances, and returns a new, updated mean and variance for a gaussian. This step is called the parameter or measurement update because it is the update that happens when an initial belief (represented by the blue Gaussian, below) is merged with a new piece of information, a measurement with some uncertainty (the orange Gaussian).

<div align=left> <img src=sources/mean_var.png width=50%/> </div>


**3. Prediction**
After performing a parameter update, which is done after some new measurement is collected, the next step is to incorporate motion into our Gaussian calculations. 
* the measurement update increases our estimation certainty
* the motion update/prediction decreases our certainty

That is because every motion has some chance of under or overshooting its goal, and since motion is not exact, we end up losing some certainty about our exact location after each motion.

Let's take the formulas from the example below and use them to write a program that takes in a mean and a motion and squared variances for both of those quantities, and returns a new, updated mean and variance for a new gaussian. This step is called the motion update or the predict step.

<div align=left> <img src=sources/motion_update.png width=50%/> </div>


**4. 1D Kalman Filter**
Last step is to implement a 1D Kalman Filter by putting all these steps together. As a robot moves through the world it locates itself by performing a cycle of:
* sensing and performing a measurement update and
* moving and performing a motion update

After implementing this filter, you should see that you can go from a very uncertain location Gaussian to a more and more certain Gaussian, as pictured below. The code in this is really just a simplified version of the Kalman filter that runs in the Google self-driving car that is used to track surrounding vehicles and other objects.

<div align=left> <img src=sources/gaussian_updates.png width=50%/> </div>


## Generic Particle Filter Algorithm
- Randomly generate a bunch of particles: particles can have position, heading, and/or whatever other state variable you need to estimate. Each has a weight (probability) indicating how likely it matches the actual state of the system. Initialize each with the same weight.

- Predict next state of the particles: Move the particles based on how you predict the real system is behaving.

- Update: Update the weighting of the particles based on the measurement. Particles that closely match the measurements are weighted higher than particles which don't match the measurements very well.

- Particle Resampling: Discard highly improbable particle and replace them with copies of the more probable particles.

- Compute Estimate: Optionally, compute weighted mean and covariance of the set of particles to get a state estimate.

You can refer to [Tutorial of particle filter ](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/12-Particle-Filters.ipynb) for better understanding and python implementation of particle filter.


----
**Task 1**

Write a Gaussian function and plot a Gaussian;

**Task 2**

Write an update function that performs the measurement update.

**Task 3**

Write a predict function that returns new values for the mean and squared variance of a Gaussian after a motion.

**Task 4** 

For the given measurements and motions, write complete 1D Kalman filter code that loops through all of these in order.

Your complete code should look at sensor measurements then motions in that sequence until all updates are done!

Initial Uncertainty
You'll see that you are given initial parameters below, and this includes and nitial location estimation, mu and squared variance, sig. Note that the initial estimate is set to the location 0, and the variance is extremely large; this is a state of high confusion much like the uniform distribution we used in the histogram filter. There are also values given for the squared variance associated with the sensor measurements and the motion, since neither of those readings are perfect, either.

You should see that even though the initial estimate for location (the initial mu) is far from the first measurement, it should catch up fairly quickly as you cycle through measurements and motions.




## Code for tasks
**Note:** Please finish the function code in **[1D_kalman.py.py](code/1D_kalman.py)**.


