import numpy as np
import random

def create_random_grid_with_edges(size, num_obstacles):
    grid = np.ones((size, size))
    for _ in range(num_obstacles):
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            y = random.randint(0, size - 1)
            x = random.randint(0, size - 2)
            if (x, y) != (0, 0) and (x + 1, y) != (0, 0) and (x, y) != (size - 1, size - 1) and (x + 1, y) != (size - 1, size - 1):
                grid[y, x] = 0
                grid[y, x + 1] = 0
        else:
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 2)
            if (x, y) != (0, 0) and (x, y + 1) != (0, 0) and (x, y) != (size - 1, size - 1) and (x, y + 1) != (size - 1, size - 1):
                grid[y, x] = 0
                grid[y + 1, x] = 0
    return grid
