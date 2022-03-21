"""

This script implements a multilateration algorithm that, given the coordinates of a finite number of radio stations,
and given their distances to the station (derived from the intensities of the signal they received in a previous step)
computes the most probable coordinates of the station. Even if the distances computed for each station do not match
(in terms of pointing to a single optimal solution) the algorithm finds the coordinates that minimize the error function
and returns the most optimal solution possible.


https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
https://docs.scipy.org/doc/scipy/reference/optimize.minimize-neldermead.html#optimize-minimize-neldermead

"""

from scipy.optimize import minimize
from cmaes import CMA
import numpy as np


def quadratic(x, c, r):
    return **complete the error section**


if __name__ == "__main__":
    stations = list(np.array([[1, 1], [0, 1], [1, 0], [0, 0]]))
    distance_to_station = [0.1, 0.5, 0.5, 1.3]
    optimizer = CMA(mean=np.zeros(2), sigma=1.3)

**finish the main function of cmaes optimization**
