import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 40
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
LIGHT_GREY = (211, 211, 211)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Maze Game')

class Maze:

    def __init__(self):
        # Define the maze as a list of strings with correct dimensions
        self.maze = [
            "11111111111111111111",
            "10000000000000000001",
            "10110111101111111101",
            "10000000100000000001",
            "10111100101111110101",
            "10100000100000100001",
            "10101111001110101111",
            "10001000000010100001",
            "11111011100110111101",
            "10000010000000000001",
            "10111111101101111101",
            "10100000100000000001",
            "10101110101110010101",
            "10000010100000100001",
            "10111110111110100111",
            "10000000000010100001",
            "11111110111110111101",
            "10000000100000000001",
            "10111110101111111101",
            "10000000000000000001"
        ]

        # Define fire pits as a list of tuples (row, col)
        self.fire_pits = [(2, 4), (4, 6), (6, 8), (8, 10), (10, 12), (12, 14), (14, 16), (16, 18), (17, 15)]

        # Robot starting position
        self.robot_pos = [1, 1]

        # End position
        self.end_pos = [18, 18]

        robot = pygame.image.load("resources/robot.jpg")
        self.robot_img = pygame.transform.scale(robot, (GRID_SIZE, GRID_SIZE))

        fire = pygame.image.load("resources/fire.jpg")
        self.fire_img = pygame.transform.scale(fire, (GRID_SIZE, GRID_SIZE))

        flag = pygame.image.load("resources/flag.jpg")
        self.flag_img = pygame.transform.scale(flag, (GRID_SIZE, GRID_SIZE))


    def play(self):
        # Main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    new_pos = self.robot_pos.copy()
                    if event.key == pygame.K_LEFT:
                        new_pos[1] -= 1
                    elif event.key == pygame.K_RIGHT:
                        new_pos[1] += 1
                    elif event.key == pygame.K_UP:
                        new_pos[0] -= 1
                    elif event.key == pygame.K_DOWN:
                        new_pos[0] += 1

                    # Check if the new position is within the maze bounds and not a wall
                    if 0 <= new_pos[0] < ROWS and 0 <= new_pos[1] < COLS and self.maze[new_pos[0]][new_pos[1]] == '0':
                        self.robot_pos = new_pos


            # Draw the self.maze
            screen.fill(WHITE)
            for row in range(ROWS):
                for col in range(COLS):
                    if self.maze[row][col] == '0':
                        color = LIGHT_GREY
                    elif self.maze[row][col] == '1':
                        color = BLACK
                    pygame.draw.rect(screen, color, pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

            # Draw the fire pits
            for pit in self.fire_pits:
                screen.blit(self.fire_img, (pit[1] * GRID_SIZE, pit[0] * GRID_SIZE))
                # pygame.draw.rect(screen, RED, pygame.Rect(pit[1] * GRID_SIZE, pit[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

            # Draw the robot
            screen.blit(self.robot_img, (self.robot_pos[1] * GRID_SIZE, self.robot_pos[0] * GRID_SIZE))

            # Draw the end position
            screen.blit(self.flag_img, (self.end_pos[1] * GRID_SIZE, self.end_pos[0] * GRID_SIZE))
            # pygame.draw.rect(screen, GREEN, pygame.Rect(self.end_pos[1] * GRID_SIZE, self.end_pos[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

            # Check for win condition
            if self.robot_pos == self.end_pos:
                print("You win!")
                running = False

            # Check if robot stepped on a fire pit
            if tuple(self.robot_pos) in self.fire_pits:
                print("You stepped on a fire pit! Game over!")
                running = False

            # Update the display
            pygame.display.flip()

        # # Quit Pygame
        # pygame.quit()
        # sys.exit()


Maze().play()

