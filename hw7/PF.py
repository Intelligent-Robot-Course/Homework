import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from queue import PriorityQueue

# Environment setup
grid_size = (20, 20)
obstacles = [
    ((5, 5), (7, 7)),
    ((10, 10), (12, 15)),
    ((1, 14), (3, 17)),
    ((15, 3), (18, 5))
]


# A* for path planning
def heuristic(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))


def a_star_search(start, goal, obstacles, grid_size):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()[1]

        if current == goal:
            break

        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= next[0] < grid_size[0] and 0 <= next[1] < grid_size[1]:
                if any(ob[0][0] <= next[0] <= ob[1][0] and ob[0][1] <= next[1] <= ob[1][1] for ob in obstacles):
                    continue
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(goal, next)
                    frontier.put((priority, next))
                    came_from[next] = current

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path


# Particle filter setup
num_particles = 100
particles = np.random.rand(num_particles, 2) * grid_size  # Initial particles
weights = np.ones(num_particles) / num_particles  # Initial weights


# Motion and measurement models
def motion_update(particles, move, noise=1.0):
    """ Move particles based on the motion model and some noise. """
    particles += move + np.random.randn(*particles.shape) * noise
    return particles


def measurement_update(particles, actual_position, sensor_noise=1.0):
'''
    """ Update weights based on how close particles are to the actual position. """
    ****Complete this function for task3
'''
    return weights


def resample(particles, weights):
'''
    """ Resample particles based on weights. """
    ****Complete this function for task3
'''
    return 


# Simulation loop
path = a_star_search((2, 2), (16, 16), obstacles, grid_size)  # Planned path
fig, ax = plt.subplots()
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
line, = ax.plot([], [], 'ro', markersize=5)

# Add obstacles to plot
for ob in obstacles:
    rect = patches.Rectangle(ob[0], ob[1][0] - ob[0][0], ob[1][1] - ob[0][1], linewidth=1, edgecolor='r',
                             facecolor='gray')
    ax.add_patch(rect)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    global particles, weights
    move = np.array(path[i + 1]) - np.array(path[i])  # Movement from A*
    particles = motion_update(particles, move)
    weights = measurement_update(particles, path[i + 1])
    particles = resample(particles, weights)

    x = particles[:, 0]
    y = particles[:, 1]
    line.set_data(x, y)
    return line,


ani = FuncAnimation(fig, animate, frames=len(path) - 1, init_func=init, blit=True, interval=300)

# Save the animation
ani.save('particle_filter_simulation.gif', writer='pillow', fps=2)

plt.show()
