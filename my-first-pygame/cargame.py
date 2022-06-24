import pygame
import sys
import os
from pygame.locals import *

pygame.init()
running = True
screen = pygame.display.set_mode((1920, 1000))
pygame.display.set_caption("Aldyz car game")


lawn = pygame.image.load(os.path.join("my-first-pygame", "images", "lawn.jpg")).convert()
lawn_x = 0
lawn_y = 0
lawn = pygame.transform.scale(lawn, (1920, 1000))
screen.blit(lawn, (lawn_x, lawn_y))

road = pygame.image.load(os.path.join("my-first-pygame", "images", "road.jpg")).convert()
road_x = 350
road_y = 0
road = pygame.transform.scale(road, (1920, 1200))
road = pygame.transform.rotate(road, 90)
screen.blit(road, (road_x, road_y))

car = pygame.image.load(os.path.join("my-first-pygame", "images", "car.png"))
carX = 600
carY = 700
x_movement = 10
y_movement = 10
car = pygame.transform.scale(car, (100, 200))
screen.blit(car, (carX, carY))

car2 = pygame.image.load(os.path.join("my-first-pygame", "images", "car2.png"))
car2_loc = car2.get_rect()
car2_x = 1200
car2_y = 700
car2 = pygame.transform.scale(car2, (100, 200))
screen.blit(car2, (car2_x, car2_y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP!")
                y_movement = 0.1
            if event.key == pygame.K_RIGHT:
                print("Right!")
                
    pygame.display.update()
            
pygame.quit()