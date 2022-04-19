import pygame

# 시작화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5) #(그릴 위치, 색, 중심점, 반지름, 두께)

# 게임화면 보여주기
def dispaly_game_screen():
    print("Game Start")

# pos 에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

# 초기화
pygame.init()  

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("MEMORY TEST")

# 시작버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120) # 좌하에서 120, 120 떨어져있음

# 색깔
BLACK = (0, 0, 0) #RGB 값
WHITE = (255, 255, 255)

# 게임 시작 여부 판단
start = False

# 이번트 루프 (창이 꺼지지 않도록)
running = True
while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 마우스 클릭 시
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)
    

    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)


    if start:
    # start이면 게임 화면 표시
        dispaly_game_screen()
    else:
    # 시작 화면 표시
        display_start_screen()

    # 사용자가 클릭한 좌표값이 있다면 (어딘가 클릭했다면)
    if click_pos:
        check_buttons(click_pos)



    # 화면 업데이트
    pygame.display.update()

# pygame 종료

pygame.quit()