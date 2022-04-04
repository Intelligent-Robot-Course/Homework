#!/usr/bin/env python

import numpy as np
import csv
from matplotlib import pyplot as plt


def calculate_odometry_velocity(currentPos, velL, velR, deltaT, noise = False, control_std = [0.01, 0.01]):
    """ Calculate odometry based on velocity readings
    Args:
        currentPos (np.mat): current position
        velL (float): velocity of left wheel
        velR (float): velocity of right wheel
        deltaT (float): time difference between two preceeding positions
        noise: whether the input control data has noise
        control_std: the level of noise added to the velocity
    Returns:
        (np.mat): updated position
    """
    L = 330.0

    if noise == True:
        V_noise = np.mat([[velR], [velL]]) + np.random.normal([[0], [0]], scale = [[control_std[0]], [control_std[1]]])
    else:
        V_noise = np.mat([[velR], [velL]])

    V_noise = V_noise * deltaT
    # To do: based on the velocity motion model, please code the matrix A (dimension: 3 x 2) in the following line, then the code in libe 30 can run correctly
    
    deltaPos = A * V_noise
    currentPos = currentPos + deltaPos
    return currentPos


def calculate_odometry_encoders(currentPos, deltaL, deltaR, noise = False, control_std = [0.01, 0.01]):
    """Calculate odometry based on encoder readings
    Args:
        currentPos (np.mat): current position
        deltaL (int): shift readed on left encoder
        deltaR (int): shift readed on right encoder
        noise: whether the input control data has noise
        control_std: the level of noise added to the velocity
    Returns:
        (np.mat): updated position
    """
    L = 330.0
    ticksPerRev = 76600
    d = 195
    V = np.mat([[(deltaR / ticksPerRev) * np.pi * d],
                [(deltaL / ticksPerRev) * np.pi * d]])
    if noise == True:
        V_noise = V + np.random.normal([[0], [0]], scale=[[control_std[0]], [control_std[1]]])
    else:
        V_noise = V

     # To do: based on the encoer-based motion model, please code the matrix A (dimension: 3 x 2) in the following line
    deltaPos = A * V_noise
    currentPos = currentPos + deltaPos
    return currentPos


def calcualte_encoder_shift(row, prev_enc_L, prev_enc_R):
    """Calculate shift for both encoders
    Args:
        row (dict): dictionary with new data
        prev_enc_L (int): previous position of left encoder
        prev_enc_R (int): previous position of right encoder
    Returns:
        [int, int]: encoders shift
    """
    deltaL = 0
    deltaR = 0
    if prev_enc_L > 15000 and float(row['posL']) < -15000:
        # forward from + to -
        deltaL = float(row['posL']) - MIN_INT_16
        deltaL = deltaL + (MAX_INT_16 - prev_enc_L)
    elif prev_enc_L < -15000 and float(row['posL']) > 15000:
        # backward from - to +
        deltaL = float(row['posL']) - MAX_INT_16
        deltaL = deltaL + (MIN_INT_16 - prev_enc_L)
    else:
        deltaL = float(row['posL']) - prev_enc_L

    if prev_enc_R > 15000 and float(row['posR']) < -15000:
        # forward from + to -
        deltaR = float(row['posR']) - MIN_INT_16
        deltaR = deltaR + (MAX_INT_16 - prev_enc_R)
    elif prev_enc_R < -15000 and float(row['posR']) > 15000:
        # backward from - to +
        deltaR = float(row['posR']) - MAX_INT_16
        deltaR = deltaR + (MIN_INT_16 - prev_enc_R)
    else:
        deltaR = float(row['posR']) - prev_enc_R
    return deltaL, deltaR


def timestamp_to_sec(timeStamp):
    x = timeStamp.split(':')
    return float(x[2])


def print_possitions(vel, enc):
    print("Current position: ")
    print("VELOCITIES: x: {}, y: {}, T: {}".format(round(vel[0, 0], 3), round(vel[1, 0], 3), round(vel[2, 0], 3)))
    print("ENCODERS:   x: {}, y: {}, T: {}".format(round(enc[0, 0], 3), round(enc[1, 0], 3), round(enc[2, 0], 3)))


def plot_trajectory(title, x, y):
    plt.figure()
    plt.plot(x, y)
    plt.title(title)


def plot_both_trajectories(title, x1, y1, x2, y2):
    plt.figure()
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.title(title)
    plt.legend(["velocity odometry", 'encoders odometry'])


def showPlots():
    plt.show()


if __name__ == "__main__":

    _file = 'data/velocity/square_left.csv'

    MIN_INT_16 = -32768
    MAX_INT_16 = 32767

    current_pos_vel = np.mat('0;0;0')
    current_pos_enc = np.mat('0;0;0')

    # lists to hold data for print
    pos_vel_x = []
    pos_vel_y = []
    pos_enc_x = []
    pos_enc_y = []

    with open(_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='|')
        prev_time = 0
        prev_enc_l = 0
        prev_enc_r = 0
        prev_enc_init = False

        for row in reader:
            timestamp = timestamp_to_sec(row['#time'])
            current_pos_vel = calculate_odometry_velocity(current_pos_vel, float(row['velL']), float(row['velR']),
                                                          timestamp - prev_time, True, [0.01, 0.01])
            pos_vel_x.append(current_pos_vel[0, 0])
            pos_vel_y.append(current_pos_vel[1, 0])
            prev_time = timestamp

            if prev_enc_init == False:
                prev_enc_l = float(row['posL'])
                prev_enc_r = float(row['posR'])
                prev_enc_init = True

            delta_l, delta__r = calcualte_encoder_shift(row, prev_enc_l, prev_enc_r)
            current_pos_enc = calculate_odometry_encoders(current_pos_enc, delta_l, delta__r, True, [0.01, 0.01])
            pos_enc_x.append(current_pos_enc[0, 0])
            pos_enc_y.append(current_pos_enc[1, 0])

            prev_enc_l = float(row['posL'])
            prev_enc_r = float(row['posR'])

    print_possitions(current_pos_vel, current_pos_enc)
    plot_both_trajectories("encoders + velocity", pos_vel_x, pos_vel_y, pos_enc_x, pos_enc_y)
    showPlots()
