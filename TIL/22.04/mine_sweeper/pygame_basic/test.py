import pygame
import os

pygame.init() 

screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height)) 

pygame.display.set_caption("Mine Sweeper")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 화면
background = pygame.image.load(os.path.join(image_path, "background.png"))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

# pygame 종료
pygame.quit()