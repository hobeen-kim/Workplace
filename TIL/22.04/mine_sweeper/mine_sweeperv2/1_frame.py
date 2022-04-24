from random import *
import pygame

pygame.init() 

screen_width = 640
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height)) 


running = True
while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

#pygame.time.delay(5000)

pygame.quit()