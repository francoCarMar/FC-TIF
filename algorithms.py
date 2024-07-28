import heapq
from utils import heuristic, line_of_sight


DIRECTIONS_DIAGONALS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def get_neighbors(node, grid, directions):
    neighbors = []
    for dx, dy in directions:
        x2, y2 = node[0] + dx, node[1] + dy
        if 0 <= x2 < grid.shape[0] and 0 <= y2 < grid.shape[1] and grid[y2, x2] == 1:
            neighbors.append((x2, y2))
    return neighbors


def path_cost(start, goal, came_from, cost_so_far):
    if goal not in came_from:
        return [], float('inf')  # No se encontró un camino

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path, cost_so_far[goal]


# ruta solo orthogonal
def astar(grid, start, goal):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = []
    heapq.heappush(queue, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    try:
        while queue:
            _, current = heapq.heappop(queue)

            if current == goal:
                break

            for next_node in get_neighbors(current, grid, directions):
                new_cost = cost_so_far[current] + 1
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + heuristic(goal, next_node)
                    heapq.heappush(queue, (priority, next_node))
                    came_from[next_node] = current
    except Exception as e:
        print(f'Error in A*: {e}')
    return path_cost(start, goal, came_from, cost_so_far)


# ruta orthogonal y diagonal
def theta_star(grid, start, goal):
    queue = []
    heapq.heappush(queue, (0, start))
    came_from = {start: start}
    cost_so_far = {start: 0}

    try:
        while queue:
            _, current = heapq.heappop(queue)

            if current == goal:
                break

            for next_node in get_neighbors(current, grid, DIRECTIONS_DIAGONALS):
                if line_of_sight(grid, came_from[current], next_node):
                    new_cost = cost_so_far[came_from[current]] + heuristic(came_from[current], next_node)
                    if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                        cost_so_far[next_node] = new_cost
                        priority = new_cost + heuristic(goal, next_node)
                        heapq.heappush(queue, (priority, next_node))
                        came_from[next_node] = came_from[current]
                else:
                    new_cost = cost_so_far[current] + heuristic(current, next_node)
                    if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                        cost_so_far[next_node] = new_cost
                        priority = new_cost + heuristic(goal, next_node)
                        heapq.heappush(queue, (priority, next_node))
                        came_from[next_node] = current
    except Exception as e:
        print(f'Error in Theta*: {e}')
    return path_cost(start, goal, came_from, cost_so_far)


# ruta orthogonal y diagonal lazy
def lazy_theta_star(grid, start, goal):
    queue = []
    heapq.heappush(queue, (0, start))
    came_from = {start: start}
    cost_so_far = {start: 0}
    is_expanded = {start: True}

    try:
        while queue:
            _, current = heapq.heappop(queue)

            if current == goal:
                break

            if not is_expanded[current]:
                if line_of_sight(grid, came_from[current], current):
                    new_cost = cost_so_far[came_from[current]] + heuristic(came_from[current], current)
                    if new_cost < cost_so_far[current]:
                        cost_so_far[current] = new_cost
                        came_from[current] = came_from[current]
                is_expanded[current] = True

            for next_node in get_neighbors(current, grid, DIRECTIONS_DIAGONALS):
                new_cost = cost_so_far[current] + heuristic(current, next_node)
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + heuristic(goal, next_node)
                    heapq.heappush(queue, (priority, next_node))
                    came_from[next_node] = current
                    is_expanded[next_node] = False
    except Exception as e:
        print(f'Error in Lazy Theta*: {e}')
    return path_cost(start, goal, came_from, cost_so_far)
