import random
import pygame
from pygame.locals import *
import time
pygame.init()

width = 1000
height = 500

white = 255,255,255

screen = pygame.display.set_mode((width,height))

gun_shot = pygame.mixer.Sound("assets/shot_sound.wav")
gameOverMusic = pygame.mixer.Sound("assets/gameOver.wav")
bg = pygame.image.load("assets/background.png")

zombie_list = []

for i in range(4):
    zombie_list.append(pygame.image.load("assets/zombie_{}.png".format(i+1)))

gun_aim = pygame.image.load("assets/aim_pointer.png")
user_gun = pygame.image.load("assets/gun_1.png")
spark = pygame.image.load("assets/fire_spark.png")

def gameOver():
    font = pygame.font.SysFont(None,80)
    text = font.render('Game Over',True,white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(text, (300,200))

        pygame.display.update()

def showTimer(timer):
    font = pygame.font.SysFont(None,50,italic=True)
    text = font.render('Time Left : '+str(timer),True,white)
    screen.blit(text, (width-300,10))

def gun_spark(pos_x):
    while True:
        screen.blit(spark, (pos_x + 20, height - 230))
        pygame.display.update()
        time.sleep(0.3)
        break

def game():
    zombie_image = random.choice(zombie_list)
    zombie_x = random.randint(0, width - zombie_image.get_width())
    zombie_y = random.randint(0, height - zombie_image.get_height())

    countShots = 0

    zombieScaleX = 130
    zombieScaleY = 180

    seconds = 15
    pygame.time.set_timer(USEREVENT, 1000)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == USEREVENT:
                seconds -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                gun_shot.play()
                gun_spark(pos_x)
                if zombie_rect.colliderect(aim_rect):
                    countShots += 1
                    zombieScaleX -= 10
                    zombieScaleY -= 10
                    zombie_image = pygame.transform.scale(zombie_image, (zombieScaleX, zombieScaleY))
                    # zombie_image = pygame.transform.rotate(zombie_image, 45)
                    if countShots == 3:
                        zombie_image = random.choice(zombie_list)
                        zombie_x = random.randint(0, width - zombie_image.get_width())
                        zombie_y = random.randint(0, height - zombie_image.get_height())
                        countShots = 0
                        zombieScaleX = 100
                        zombieScaleY = 150

        pos_x, pos_y = pygame.mouse.get_pos()

        screen.blit(bg, (0,0))
        screen.blit(zombie_image, (zombie_x, zombie_y))
        screen.blit(gun_aim, (pos_x - gun_aim.get_width()/2, pos_y - gun_aim.get_height()/2))
        screen.blit(user_gun, (pos_x, height - 200))

        aim_rect = pygame.Rect(pos_x - gun_aim.get_width()/2, pos_y - gun_aim.get_height()/2, gun_aim.get_width(), gun_aim.get_height())
        zombie_rect = pygame.Rect(zombie_x, zombie_y, zombie_image.get_width(), zombie_image.get_height())

        showTimer(seconds)

        if seconds == 0:
            gameOverMusic.play()
            gameOver()

        pygame.display.update()

game()