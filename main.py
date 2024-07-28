import time
from grid import create_random_grid_with_edges
from algorithms import astar, theta_star, lazy_theta_star
from visualization import draw_paths, draw_results


def main():
    results = {"A*": [], "Theta*": [], "Lazy Theta*": []}
    length = 200

    for size in range(3, length):
        num_obstacles = int(size ** (5/4))  # Ajustar la densidad de obstáculos según el tamaño del grid
        grid = create_random_grid_with_edges(size, num_obstacles)
        start = (0, 0)
        goal = (size - 1, size - 1)

        try:
            start_time = time.time()
            path_astar, cost_astar = astar(grid, start, goal)
            time_astar = time.time() - start_time

            start_time = time.time()
            path_theta_star, cost_theta_star = theta_star(grid, start, goal)
            time_theta_star = time.time() - start_time

            start_time = time.time()
            path_lazy_theta_star, cost_lazy_theta_star = lazy_theta_star(grid, start, goal)
            time_lazy_theta_star = time.time() - start_time

            results["A*"].append(time_astar)
            results["Theta*"].append(time_theta_star)
            results["Lazy Theta*"].append(time_lazy_theta_star)

            print(f'Tamaño del grid: {size}x{size}')
            print(f'Tiempo de A*: {time_astar:.6f} segundos')
            print(f'Tiempo de Theta*: {time_theta_star:.6f} segundos')
            print(f'Tiempo de Lazy Theta*: {time_lazy_theta_star:.6f} segundos')
            print(f'Costo de A*: {cost_astar:.2f}')
            print(f'Costo de Theta*: {cost_theta_star:.2f}')
            print(f'Costo de Lazy Theta*: {cost_lazy_theta_star:.2f}')
        except Exception as e:
            print(f'Error con tamaño de grid {size}x{size}: {e}')

    draw_results(results, length)

    size = 10
    num_obstacles = 15
    grid = create_random_grid_with_edges(size, num_obstacles)
    start = (0, 0)
    goal = (9, 9)
    try:
        path_astar, cost_astar = astar(grid, start, goal)
        path_theta_star, cost_theta_star = theta_star(grid, start, goal)
        path_lazy_theta_star, cost_lazy_theta_star = lazy_theta_star(grid, start, goal)
        draw_paths(grid, [path_astar, path_theta_star, path_lazy_theta_star], start, goal,
                   [cost_astar, cost_theta_star, cost_lazy_theta_star])
    except Exception as e:
        print(f'Error al encontrar el camino: {e}')


if __name__ == "__main__":
    main()
