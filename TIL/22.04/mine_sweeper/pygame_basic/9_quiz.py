# 하늘에서 똥 피하기
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우만 이동가능
# 2. 똥은 화면 가장 위에서 떨어짐. x좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30 으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480
# 2. 캐릭터 : 70 * 70
# 3. 똥 70 * 70

# [개인 추가사항]
# 똥 여러개 생성

from random import randint, random
import pygame
import enemys

#초기화 
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
enemy_speed = 0.6

#적 enemy 캐릭터
num_enemies = randint(3, 7)
enemies = []
enemy = pygame.image.load("C:\\Users\\USER\\Desktop\\workplace\\TIL\\22.04\\mine_sweeper\\pygame_basic\\enemy.png")
for _ in range(num_enemies):
    lst = enemys.Enemy(
        enemy,
        enemy.get_rect().size,
        enemy.get_rect().size[0],
        enemy.get_rect().size[1], 
        randint(0, screen_width - enemy.get_rect().size[0]), 
        randint(-screen_height, 0)
        )
    enemies.append(lst)


# 폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트, 크기)

# 총 시간 / 시작 시간
total_time = 30
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴


# 이번트 루프 (창이 꺼지지 않도록)
running = True
while running:

    # 게임화면의 초당 프레임 수 설정
    dt = clock.tick(30) #프레임 보기 .. print(f"fps : {str(clock.get_fps())}")
    
    # 프레임이 높으면 dt가 낮고, 프레임이 낮으면 dt가 높음
    #캐릭터가 1초 동안 100만큼 이동해야함
    # 10fps : 1초 동안에 10번 동작 -> 1번은 1번에 10만큼 이동해야 함
    # 20fps : 1초 동안에 20번 동작 -> 1번에 5만큼 이동해야 함

####################이벤트 처리 (키보드, 마우스 등) ####################

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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 #더 이상 움직이지 마라

#################### 게임 캐릭터 위치 정의 ####################
    #캐릭터 위치
    character_x_pos += to_x * dt 
    
    # 캐릭터 위치를 스크린 안에 가두기
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos =screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    #충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos #실제 캐릭터 x위치 업데이트
    character_rect.top = character_y_pos #실제 캐릭터 y위치 업데이트

    # enemy 4개 생성
    for i in range(num_enemies):
         # enemy 하강
        enemies[i].enemy_y_pos += enemy_speed * dt 

        # enemy 위치 계속 생성
        if enemies[i].enemy_y_pos >= screen_height:
            enemies[i].enemy_y_pos = -enemies[0].enemy_height
            enemies[i].enemy_x_pos = randint(0, screen_width - enemies[0].enemy_width)
        
        enemy_rect = enemies[i].enemy.get_rect()
        enemy_rect.left = enemies[i].enemy_x_pos #실제 캐릭터 x위치 업데이트
        enemy_rect.top = enemies[i].enemy_y_pos #실제 캐릭터 y위치 업데이트

        if character_rect.colliderect(enemy_rect): #충돌하였는가?
            print("충돌했어요")
            running = False


    


#################### 화면에 그리기 ####################

    #배경 그리기
    screen.blit(background, (0, 0)) #screen.fill((0, 0, 255)) .. 파란색으로 채우기

    #캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    #적 그리기
    for i in range(num_enemies):
        screen.blit(enemy, (enemies[i].enemy_x_pos, enemies[i].enemy_y_pos))

    # 타이머 집어넣기
    ## 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #단위가 ms라서 1000으로 나눠 초(s)로 표시
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) #render(출력할 글자, True, 색상) /소수점을 버리기 위해 int, 이후 str 
    ## 타이머 집어 넣기
    screen.blit(timer, (10, 10))
    ## 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("성공하였습니다.")
        running = False


    #게임 화면을 다시 그리기(반드시 계속 호출되어야 함)
    pygame.display.update()

# 종료 전 2초 대기
pygame.time.delay(2000)

# pygame 종료
pygame.quit()

