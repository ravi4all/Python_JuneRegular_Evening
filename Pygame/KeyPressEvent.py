import random
import pygame
pygame.init()
color_1 = 189, 205, 167

red = 255,0,0
black = 0,0,0

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))
x = 10
y = 10

move_x = 0
move_y = 0

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
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -0.4
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 0.4
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -0.4
                move_x = 0


    screen.fill(color_1)
    pygame.draw.rect(screen,red,[x,y,50,50])

    x += move_x
    y += move_y

    if x > width:
        x = -50
    elif y > height:
        y = -50

    if x < -50:
        x = width
    elif y < -50:
        y = height

    pygame.display.update()