import pygame
import time
import os

pygame.init() 

# 화면 크기 설정
screen_width = 640
screen_height = 480

# 스크린 크기 설정
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()

# 이미지 불러오기
## 현재 파일의 위치 반환
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 만들기 
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height - stage_height


running = True
while running:

    # 게임화면의 초당 프레임 수 설정
    dt = clock.tick(60) 

    #종료버튼 눌렀을 때 pygame 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 배경 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()

