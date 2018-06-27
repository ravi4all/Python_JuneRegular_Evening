import random
import pygame

pygame.init()
color_1 = 189, 205, 167

red = 255, 0, 0
black = 0, 0, 0
blue = 0, 0, 255
yellow = 255, 255, 0
green = 0, 255, 0
pink = 0, 255, 255

colors = [red, black, blue, yellow, green, pink]

width = 1100
height = 500

screen = pygame.display.set_mode((width, height))

x = 0
y = 0

gap = 10

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(color_1)

    for col in range(5):
        for i in range(15):
            pygame.draw.rect(screen, red, [x+80*i,y+40*col,70,35])

    # pygame.draw.rect(screen, red, [x, y, 70, 35])
    # pygame.draw.rect(screen, red, [x+80, y, 70, 35])
    # pygame.draw.rect(screen, red, [x+160, y, 70, 35])
    # pygame.draw.rect(screen, red, [x+240, y, 70, 35])
    # pygame.draw.rect(screen, red, [x+320, y, 70, 35])

    pygame.display.update()