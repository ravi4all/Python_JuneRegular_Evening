import pygame
pygame.init()
color_1 = 189, 205, 167
red = 255,0,0

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))
x = 10
y = 10

move_x = 0.2
move_y = 0.4

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(color_1)
    pygame.draw.rect(screen,red,[x,y,50,50])

    x += move_x
    y += move_y

    if x > width - 50:
        move_x = -0.5
    elif x < 0:
        move_x = 0.5

    if y > height - 50:
        move_y = -0.5
    elif y < 0:
        move_y = 0.5

    pygame.display.update()