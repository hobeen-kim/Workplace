import pygame

#초기화 (반드시 필요)
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

#배경이미지 불러오기
background = pygame.image.load("C:\\Users\\USER\\Desktop\\workplace\\TIL\\22.04\\mine_sweeper\\pygame_basic\\background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\Users\\USER\\Desktop\\workplace\\TIL\\22.04\\mine_sweeper\\pygame_basic\\character.png")

# 이미지 크기로 넓이, 높이를 구하고 위치 결정
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

# 이동할 좌표, 이동 속도
to_x = 0
to_y = 0
character_speed = 0.6

# 이번트 루프 (창이 꺼지지 않도록)
running = True
while running:

    # 게임화면의 초당 프레임 수 설정
    dt = clock.tick(60) #프레임 보기 .. print(f"fps : {str(clock.get_fps())}")
    
    # 프레임이 높으면 dt가 낮고, 프레임이 낮으면 dt가 높음
    #캐릭터가 1초 동안 100만큼 이동해야함
    # 10fps : 1초 동안에 10번 동작 -> 1번은 1번에 10만큼 이동해야 함
    # 20fps : 1초 동안에 20번 동작 -> 1번에 5만큼 이동해야 함

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #키를 누를 때
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            #어떤 키를 누르는 지
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 #더 이상 움직이지 마라
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt #dt를 곱하는 이유는 속도를 일정하게 하기 위해
    character_y_pos += to_y * dt

    # 캐릭터 위치를 스크린 안에 가두기
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos =screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    #배경 그리기
    screen.blit(background, (0, 0)) #screen.fill((0, 0, 255)) .. 파란색으로 채우기

    #캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    #게임 화면을 다시 그리기(반드시 계속 호출되어야 함)
    pygame.display.update()

# pygame 종료
pygame.quit()