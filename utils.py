import numpy as np

def heuristic(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

def line_of_sight(grid, s, s_prime):
    x0, y0 = s
    x1, y1 = s_prime
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while (x0, y0) != (x1, y1):
        if grid[y0, x0] == 0:
            return False
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return grid[y1, x1] == 1
