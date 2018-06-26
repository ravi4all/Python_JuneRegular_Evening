import random
import pygame
pygame.init()
color_1 = 189, 205, 167

red = 255,0,0
black = 0,0,0
blue = 0,0,255
yellow = 255,255,0
green = 0,255,0
pink = 0,255,255

colors = [red,black,blue,yellow,green,pink]

width = 1100
height = 500

screen = pygame.display.set_mode((width,height))
x = (width / 2) - 75
y = height - 50

move_x = 0

# events = [keydown,keyup,mousemotion]
while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 0.4
            elif event.key == pygame.K_LEFT:
                move_x = -0.4

        elif event.type == pygame.KEYUP:
            move_x = 0

    screen.fill(color_1)
    pygame.draw.rect(screen,red,[x,y,150,20])

    for i in range(5):
        for j in range(20):
            # col = random.choice(colors)
            pygame.draw.rect(screen,red,[j*50+12, i*35, 50, 35])

    x += move_x

    if x > width - 150 or x < 0:
        move_x = 0

    pygame.display.update()