import random
import numpy as np

def random_policy(grid_world):
    return random.randint(0, 3)

def greedy_policy(grid_world):
    pos = grid_world.get_position()
    return np.argmax(grid_world.q[pos[0], pos[1]])

def eps_greedy_policy(grid_world):
    if random.random() > grid_world.epsilon:
        return greedy_policy(grid_world)
    else:
        return random_policy(grid_world)