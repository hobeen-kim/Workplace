import pygame
import os

pygame.init() 

screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height)) 

pygame.display.set_caption("Mine Sweeper")

clock = pygame.time.Clock()
dbclock = pygame.time.Clock()
DOUBLECLICKTIME = 100
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if dbclock.tick() < DOUBLECLICKTIME:
        #         print("double click detected!")

        # mouse_pressed = pygame.mouse.get_pressed()
        # if (mouse_pressed[0] and mouse_pressed[2]) or mouse_pressed[1]:
        #     print("left and right clicked")

        if event.type == pygame.MOUSEBUTTONDOWN:
            if dbclock.tick() < DOUBLECLICKTIME:
                print(pygame.mouse.get_pressed())
    
    pygame.display.update()


# pygame 종료
pygame.quit()