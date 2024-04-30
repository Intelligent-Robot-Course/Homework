import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from queue import PriorityQueue

# Define the environment
grid_size = (20, 20)
obstacles = [
    ((5, 5), (7, 7)),
    ((10, 10), (12, 15)),
    ((1, 14), (3, 17)),
    ((15, 3), (18, 5))
]


# A* path planning function
def heuristic(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))


def a_star_search(start, goal, obstacles, grid_size):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 4-way connectivity
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
            if 0 <= next[0] < grid_size[0] and 0 <= next[1] < grid_size[1]:  # Stay within the grid
                if any(ob[0][0] <= next[0] <= ob[1][0] and ob[0][1] <= next[1] <= ob[1][1] for ob in obstacles):
                    continue  # This grid cell is blocked by an obstacle
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


# Kalman Filter predict and update functions
def kalman_filter_predict(state, cov, F, Q):
'''
****Complete this function for task2
'''
    return 


def kalman_filter_update(state_pred, cov_pred, observation, H, R):
'''
****Complete this function for task2
'''
    return 


# Set up matrices for the Kalman Filter
F = np.array([[1, 0], [0, 1]])  # Identity matrix for simplicity
H = np.array([[1, 0], [0, 1]])
Q = np.eye(2) * 0.1  # Process noise
R = np.eye(2) * 0.1  # Measurement noise

# Initial state and covariance
initial_state = np.array([[2], [2]])
initial_covariance = np.eye(2) * 0.1

# Path planning
start = (2, 2)
goal = (16, 16)
path = a_star_search(start, goal, obstacles, grid_size)

# Simulate robot movement along the path with Kalman Filter
states = [initial_state.flatten().tolist()]
current_state = initial_state
current_covariance = initial_covariance

for step in path[1:]:  # Start from the second element
    move = np.array([[step[0]], [step[1]]])  # Direct move to the next step
    current_state, current_covariance = kalman_filter_predict(current_state, current_covariance, F, Q)

    observation = move + np.random.randn(2, 1) * 0.1  # Add some noise
    current_state, current_covariance = kalman_filter_update(current_state, current_covariance, observation, H, R)

    states.append(current_state.flatten().tolist())

# Visualization using matplotlib's animation
fig, ax = plt.subplots()
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)

for ob in obstacles:
    rect = patches.Rectangle(ob[0], ob[1][0] - ob[0][0], ob[1][1] - ob[0][1], linewidth=1, edgecolor='r',
                             facecolor='gray')
    ax.add_patch(rect)

line, = ax.plot([], [], 'go-', lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = [state[0] for state in states[:i + 1]]
    y = [state[1] for state in states[:i + 1]]
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, animate, frames=len(states), init_func=init, blit=True, interval=300)

# Save as GIF using Pillow
ani.save('robot_path.gif', writer='pillow', fps=2)

plt.show()
