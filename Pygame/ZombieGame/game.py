import random
import pygame
import time
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

gun_shot = pygame.mixer.Sound("assets/shot_sound.wav")

bg = pygame.image.load("assets/background.png")

zombie_list = []

for i in range(4):
    zombie_list.append(pygame.image.load("assets/zombie_{}.png".format(i+1)))

zombie_image = random.choice(zombie_list)
zombie_x = random.randint(0,width - zombie_image.get_width())
zombie_y = random.randint(0,height - zombie_image.get_height())

gun_aim = pygame.image.load("assets/aim_pointer.png")
user_gun = pygame.image.load("assets/gun_1.png")
spark = pygame.image.load("assets/fire_spark.png")

def gun_spark(pos_x):
    while True:
        screen.blit(spark, (pos_x + 20, height - 230))
        pygame.display.update()
        time.sleep(0.3)
        break

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            gun_shot.play()
            gun_spark(pos_x)
            if zombie_rect.colliderect(aim_rect):
                zombie_image = random.choice(zombie_list)
                zombie_x = random.randint(0, width - zombie_image.get_width())
                zombie_y = random.randint(0, height - zombie_image.get_height())

    pos_x, pos_y = pygame.mouse.get_pos()

    screen.blit(bg, (0,0))
    screen.blit(zombie_image, (zombie_x, zombie_y))
    screen.blit(gun_aim, (pos_x - gun_aim.get_width()/2, pos_y - gun_aim.get_height()/2))
    screen.blit(user_gun, (pos_x, height - 200))

    aim_rect = pygame.Rect(pos_x - gun_aim.get_width()/2, pos_y - gun_aim.get_height()/2, gun_aim.get_width(), gun_aim.get_height())
    zombie_rect = pygame.Rect(zombie_x, zombie_y, zombie_image.get_width(), zombie_image.get_height())

    pygame.display.update()