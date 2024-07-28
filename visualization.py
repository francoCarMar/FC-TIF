import matplotlib.pyplot as plt
import numpy as np

def draw_paths(grid, paths, start, goal, costs):
    fig, ax = plt.subplots()
    ax.imshow(np.ones_like(grid), cmap='Greys', origin='lower')  # Fondo blanco

    colors = ['r', 'g', 'b']
    labels = [f'A*: {costs[0]:.2f}', f'Theta*: {costs[1]:.2f}', f'Lazy Theta*: {costs[2]:.2f}']

    for i, path in enumerate(paths):
        if path:  # Solo dibujar si hay un camino encontrado
            px, py = zip(*path)
            ax.plot(px, py, colors[i], label=labels[i])

    ax.plot(start[0], start[1], 'go')  # Punto inicial verde
    ax.plot(goal[0], goal[1], 'ro')    # Punto final rojo

    # Dibujar obstáculos como líneas negras con grosor 2
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] == 0:
                if x < grid.shape[1] - 1 and grid[y, x + 1] == 0:
                    ax.plot([x, x + 1], [y, y], 'k-', linewidth=2)
                if y < grid.shape[0] - 1 and grid[y + 1, x] == 0:
                    ax.plot([x, x], [y, y + 1], 'k-', linewidth=2)

    ax.legend()
    plt.show()

def draw_results(results, size):
    fig, ax = plt.subplots()
    ax.plot(range(3, size), results["A*"], 'r', label='A*')
    ax.plot(range(3, size), results["Theta*"], 'g', label='Theta*')
    ax.plot(range(3, size), results["Lazy Theta*"], 'b', label='Lazy Theta*')
    ax.legend()
    ax.set_xlabel('Tamaño del grid')
    ax.set_ylabel('Tiempo (segundos)')
    plt.show()
