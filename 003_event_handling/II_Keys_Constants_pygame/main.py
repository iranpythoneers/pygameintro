import pygame
from random import randint

def printTxt(msg):
    global X, Y, screen, WHITE, BLACK
    msg  = str(msg)
    font = pygame.font.Font("freesansbold.ttf", 64)
    text = font.render(msg, True, WHITE, BLACK)
    rect = text.get_rect()
    rect.center = (X // 2, Y // 2)
    screen.blit(text, rect)

# setup pygame
pygame.init()
X = 800 # Width of our window
Y = 600 # Heighy of our window
SIZE  = [X, Y]
BLACK = [0] * 3
WHITE = [255] * 3
# Setup our display
screen = pygame.display.set_mode(SIZE)


msg = "Hello There!"
printTxt(msg)
isUpper = False
while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        else:
            try:
                msg = 'you pressed "%s"' % event.unicode
                if event.key == pygame.K_CAPSLOCK:
                    isUpper = not isUpper
                
                if event.key == pygame.K_UP:
                    msg = "you pressed Up arrow Key"

                if isUpper:
                    msg = msg.upper()

            except:
                pass
    printTxt(msg)
    # Update The Screen
    pygame.display.update()
    # Each 250ms
    pygame.time.delay(250)