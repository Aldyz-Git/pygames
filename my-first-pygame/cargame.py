import pygame
from pygame.locals import *

pygame.init()
running = True
screen = pygame.display.set_mode((1920, 1000))
pygame.display.set_caption("Aldyz car game")

lawn = pygame.image.load("./images/lawn.jpg")
lawn_x = 0
lawn_y = 0
lawn = pygame.transform.scale(lawn, (1920, 1000))
screen.blit(lawn, (lawn_x, lawn_y))

road = pygame.image.load("./images/road.jpg")
road_x = 350
road_y = 0
road = pygame.transform.scale(road, (1920, 1200))
road = pygame.transform.rotate(road, 90)
screen.blit(road, (road_x, road_y))

player = pygame.image.load("./images/car.png")
player_loc = player.get_rect()
playerX = 600
playerY = 700
vel = 10
player = pygame.transform.scale(player, (100, 200))
screen.blit(player, (playerX, playerY))

car2 = pygame.image.load("./images/car2.png")
car2_loc = car2.get_rect()
car2_x = 1200
car2_y = 700
vel = 0.1
car2 = pygame.transform.scale(car2, (100, 200))
screen.blit(car2, (car2_x, car2_y))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left!")
                playerX = vel
            if event.key == pygame.K_RIGHT:
                print("Right!")
                playerX = vel
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                vel = 0.1




    pygame.display.update()
            
pygame.quit()