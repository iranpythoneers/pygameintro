import pygame
from random import randint
# setup pygame
pygame.init()
X = 800 # Width of our window
Y = 600 # Heighy of our window
SIZE = [X, Y]
# Setup our display
screen = pygame.display.set_mode(SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Game Will be close in few seconds")
            pygame.time.delay(1000)
            pygame.quit()

    # R G B
    COLOR = [randint(0, 255), randint(0, 255), randint(0, 255)]
    # Change The Background Color
    screen.fill(COLOR)
    # Update The Screen
    pygame.display.update()
    # Each 250ms
    pygame.time.delay(250)