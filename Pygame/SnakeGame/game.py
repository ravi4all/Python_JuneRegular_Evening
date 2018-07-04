import random
import pygame
import level_2

pygame.init()
color_1 = 189, 205, 167

red = 255,0,0
black = 0,0,0

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

frog = pygame.image.load("frog.png")

sound_1 = pygame.mixer.Sound('point.wav')
sound_2 = pygame.mixer.Sound('game_over.wav')

def gameOver():
    font = pygame.font.Font('zorque.ttf', 100)
    text = font.render("Game Over", True, black)
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(text, (200, 200))

        pygame.display.update()

def level_cleared():
    font = pygame.font.Font('zorque.ttf', 50)
    text = font.render("Level Cleared", True, black)
    text_2 = font.render("Press SPACE to open new level", True, black)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level_2.game()

        screen.blit(text, (200, 200))
        screen.blit(text_2, (100,300))

        pygame.display.update()

def score(counter):
    font = pygame.font.Font('zorque.ttf', 40)
    text = font.render("Score : "+str(counter), True, black)
    screen.blit(text, (10,10))

def snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,red,[snakeList[i][0],snakeList[i][1],50,50])

def game():
    x = 10
    y = 10
    move_x = 0
    move_y = 0
    frog_x = random.randint(0, width - frog.get_width())
    frog_y = random.randint(0, height - frog.get_height())
    snakeLength = 1
    snakeList = []
    counter = 0
    clock = pygame.time.Clock()
    FPS = 80

    while True:

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 6
                    move_y = 0
                elif event.key == pygame.K_LEFT:
                    move_x = -6
                    move_y = 0
                elif event.key == pygame.K_DOWN:
                    move_y = 6
                    move_x = 0
                elif event.key == pygame.K_UP:
                    move_y = -6
                    move_x = 0

        screen.fill(color_1)
        snake_rect = pygame.Rect(x,y,50,50)
        screen.blit(frog, (frog_x, frog_y))

        frog_rect = pygame.Rect(frog_x, frog_y, frog.get_width(), frog.get_height())

        x += move_x
        y += move_y

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)

        snakeList.append(snakeHead)
        # print(snakeList)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for each in snakeList[:-1]:
            if each == snakeList[-1]:
                sound_2.play()
                gameOver()

        if x > width:
            x = -50
        elif y > height:
            y = -50

        if x < -50:
            x = width
        elif y < -50:
            y = height

        if frog_rect.colliderect(snake_rect):
            frog_x = random.randint(0, width - frog.get_width())
            frog_y = random.randint(0, height - frog.get_height())
            snakeLength += 5
            FPS += 3
            counter += 1
            sound_1.play()

        if counter >= 10:
            level_cleared()

        snake(snakeList)
        score(counter)
        pygame.display.update()
        clock.tick(FPS)

game()