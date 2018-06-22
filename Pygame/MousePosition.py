import pygame

pygame.init()

width = 1000
height = 500

red = 255,0,0
black = 0,0,0

screen = pygame.display.set_mode((width, height))

x = 100
y = 100

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)

    pos_x,pos_y = pygame.mouse.get_pos()

    pygame.draw.circle(screen,black,[pos_x,pos_y],80)

    pygame.display.update()