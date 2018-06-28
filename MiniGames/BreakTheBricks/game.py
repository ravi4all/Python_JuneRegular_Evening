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

width = 1100
height = 500

screen = pygame.display.set_mode((width,height))
x = (width / 2) - 75
y = height - 50

bar_width = 150
move_x = 0

circle_move_x = 0
circle_move_y = 0

on_bar = True
in_air = False

circle_x = int(x) + bar_width // 2
circle_y = int(y) - 10

clock = pygame.time.Clock()
FPS = 100

while True:
    bricks = []
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if not in_air:
                if event.key == pygame.K_SPACE:
                    circle_move_x = -random.randint(0,6)
                    circle_move_y = -4
                    on_bar = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 6
            elif event.key == pygame.K_LEFT:
                move_x = -6
        elif event.type == pygame.KEYUP:
            move_x = 0

    screen.fill(color_1)
    bar = pygame.draw.rect(screen,blue,[x,y,bar_width,20])

    for row in range(5):
        for col in range(15):
            bricks.append(pygame.draw.rect(screen, red, [80*col,40*row,70,35]))

    x += move_x

    ball_rect = pygame.draw.circle(screen, black, [circle_x, circle_y], 10)

    for i in range(len(bricks)):
        if ball_rect.colliderect(bricks[i]):
            bricks.pop(i)
            circle_move_y = 4

    if on_bar:
        circle_x = int(x) + bar_width // 2
        circle_y = int(y) - 10
    else:
        circle_x += circle_move_x
        circle_y += circle_move_y
        in_air = True

    if bar.colliderect(ball_rect):
        # circle_move_x = -random.randint(0,6)
        circle_move_y = -4

    if x > width - 150 or x < 0:
        move_x = 0

    if circle_x > width - 50:
        circle_move_x = -4
    elif circle_x < 0 :
        circle_move_x = 4

    if circle_y > height:
        on_bar = True
        in_air = False

    pygame.display.update()
    clock.tick(FPS)