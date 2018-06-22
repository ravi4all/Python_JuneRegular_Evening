import pygame

pygame.init()

width = 1000
height = 500
red = 255,0,0
screen = pygame.display.set_mode((width,height))

bg_img = pygame.image.load("img_2.jpg")
# bg_img = pygame.transform.scale(bg_img,(4000,3000))

m1 = pygame.image.load("m1.png")
m2 = pygame.image.load("m2.png")

mario = [m1,m2]
m = 0
x = 200
y = height - 100

move_x = 0
move_y = 0

bg_x = 0
move_bg_x = 0

FPS = 5
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_bg_x = -2

        elif event.type == pygame.KEYUP:
            move_bg_x = 0

    # blit - render
    screen.blit(bg_img, (bg_x,0))
    # pygame.draw.rect(screen,red,[x,y,50,50])

    if m == 0:
        screen.blit(mario[0],[x,y])
        m = 1
    elif m == 1:
        screen.blit(mario[1], [x, y])
        m = 0

    bg_x += move_bg_x

    pygame.display.update()
    clock.tick(FPS)