import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Grid setup
cols, rows = 50, 50
cell_size = width // cols
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Function to draw the grid
def draw_grid():
    for x in range(cols):
        for y in range(rows):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            color = (255, 255, 255) if grid[y][x] == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

# Create a "glider" pattern
grid[1][2] = 1
grid[2][3] = 1
grid[3][1] = 1
grid[3][2] = 1
grid[3][3] = 1

grid[20][21] = 1
grid[21][20] = 1
grid[21][21] = 1
grid[21][22] = 1
grid[22][22] = 2
grid[22][21] = 2

grid[30][30] = 1
grid[30][31] = 1
grid[31][30] = 1

# Function to compute the next state
def next_generation():
    global grid
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for y in range(rows):
        for x in range(cols):
            # Calculate the number of live neighbors
            live_neighbors = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue  # Skip the current cell
                    live_neighbors += grid[(y + i) % rows][(x + j) % cols]

            # Apply the rules of Conway's Game of Life
            if grid[y][x] == 1 and (live_neighbors == 2 or live_neighbors == 3):
                new_grid[y][x] = 1
            elif grid[y][x] == 0 and live_neighbors == 3:
                new_grid[y][x] = 1
            else:
                new_grid[y][x] = 0
    grid = new_grid


# Main loop
running = True
while running:
    screen.fill((0, 0, 0))
    draw_grid()
    pygame.display.flip()
    next_generation()
    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()