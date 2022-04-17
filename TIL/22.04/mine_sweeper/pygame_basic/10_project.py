import pygame
import time

pygame.init() 

# 화면 크기 설정
screen_width = 480
screen_height = 640

# 스크린 크기 설정
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()

#배경이미지, stage 이미지
background = pygame.image.load("C:\\Users\\USER\\Desktop\\workplace\\TIL\\22.04\\mine_sweeper\\pygame_basic\\background.png")
stage = pygame.image.load("C:\\Users\\USER\\Desktop\\workplace\\TIL\\22.04\\mine_sweeper\\pygame_basic\\stage.png")

# 캐릭터
character = pygame.image.load("C:\\Users\\USER\\Desktop\\workplace\\TIL\\22.04\\mine_sweeper\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - 50 - character_height
## 캐릭터 이동
to_x = 0
to_y = 0
character_speed = 0.6

# 무기
weapon = pygame.image.load("C:\\Users\\USER\\Desktop\\workplace\\TIL\\22.04\\mine_sweeper\\pygame_basic\\weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_x_pos = screen_width / 2 - character_width / 2
weapon_y_pos = screen_height - 50

## 무기 이동
weapon_speed = 0.6
weapon_to_y = 0

# 무기 집합
weapons = []

# 공
balloon1 = pygame.image.load("C:\\Users\\USER\\Desktop\\workplace\\TIL\\22.04\\mine_sweeper\\pygame_basic\\balloon1.png")
balloon2 = pygame.image.load("C:\\Users\\USER\\Desktop\\workplace\\TIL\\22.04\\mine_sweeper\\pygame_basic\\balloon2.png")
balloon3 = pygame.image.load("C:\\Users\\USER\\Desktop\\workplace\\TIL\\22.04\\mine_sweeper\\pygame_basic\\balloon3.png")
balloon4 = pygame.image.load("C:\\Users\\USER\\Desktop\\workplace\\TIL\\22.04\\mine_sweeper\\pygame_basic\\balloon4.png")

running = True
while running:

    # 게임화면의 초당 프레임 수 설정
    dt = clock.tick(60) 

    #종료버튼 눌렀을 때 pygame 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #키를 누를 때
    if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
        if event.key == pygame.K_LEFT:
            to_x = -character_speed
        elif event.key == pygame.K_RIGHT:
            to_x = character_speed        
        if event.key == pygame.K_UP:
            weapon_x_pos = character_x_pos
            weapon_to_y = -weapon_speed


    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0 #더 이상 움직이지 마라

    #배경 그리기
    screen.blit(background, (0, 0))

    #캐릭터 그리기
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    ## 캐릭터 위치를 스크린 안에 가두기
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    screen.blit(character, (character_x_pos, character_y_pos))

    #무기 그리기
    weapon_y_pos += weapon_to_y * dt

    if weapon_y_pos < -weapon_height:
        weapon_y_pos = screen_height - 50
        weapon_to_y = 0

    screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    #풍선 그리기

    #무대 그리기
    screen.blit(stage, (0, screen_height-50))

    #게임화면 지속 업데이트
    pygame.display.update()

pygame.quit()

