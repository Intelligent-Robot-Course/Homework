from scipy.optimize import minimize
import numpy as np

def trilateration(distances_to_APs, STA_coordinates, target_position=None):
    # you should complete the function for question1
    # related to the distances between STA and three APs
    return target_position

if __name__ == "__main__":
	stations = list(np.array([[1,1], [0,1], [1,0]]))
	distances_to_station = [0.1, 0.5, 0.5]
	print(trilateration(distances_to_station, stations))
