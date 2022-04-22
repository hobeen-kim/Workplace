from random import *
import pygame

# 레벨에 맞게 설정
def setup(level):
    ## 얼마동안 숫자를 보여줄지? (시간)
    global display_time

    display_time = 5 - (level // 3)
    display_time = max(display_time, 1) # 1초 미만이면 1초로 설정

    ## 얼마나 많은 숫자를 보여줄 것인가?
    number_count = (level // 3) + 5 # 3의 배수마다 1씩 추가
    number_count = min(number_count, 20) # 만약 20을 초과하면 그냥 20으로 처리

    # 실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)

# 숫자 섞기 (가장 중요한 부분)
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    ## 셀, 버튼, 마진 등 크기
    cell_size = 130 # 각 셀 별 가로, 세로 크기
    button_size = 110 
    screen_left_margin = 55
    screen_top_margin = 20

    ## 5 X 9 채우기
    grid = [[0 for col in range(columns)] for row in range(rows)]

    ## (1, number_count) 만큼 grid 에 넣어주기
    number = 1 #시작 숫자를 1부터 number_count 까지 넣기 위해 변수 설정
    while number <= number_count:
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            ### 현재 grid cell 위치 기준으로 x, y 위치를 구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            ### 버튼 그리기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)


# 시작화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5) #(그릴 위치, 색, 중심점, 반지름, 두께)
    ## 현재 레벨 보여주기
    msg = game_font.render(f"{curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=start_button.center)
    screen.blit(msg, msg_rect)
    
# 게임화면 보여주기
def display_game_screen():
    global hidden

    if not hidden:
        elapsed_time = ( pygame.time.get_ticks() - start_ticks ) / 1000 # ms -> sec
        if elapsed_time > display_time:
            hidden = True

    ## 실제텍스트 그리기
    for idx, rect in enumerate(number_buttons, start=1): #start 1은 idx를 1부터 시작하겠다는 말

        ### 버튼 사각형 그리기 (숨김 처리)
        if hidden:
            pygame.draw.rect(screen, WHITE, rect)
        ### 실제 숫자 텍스트
        else:
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center = rect.center) #text의 rect.center를 정의
            screen.blit(cell_text, text_rect) #text 그리기

# pos 에 해당하는 버튼 확인
def check_buttons(pos):
    global start, start_ticks

    if start:
        check_number_buttons(pos)

    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks() # 타이머 시작 (현재 시간을 저장)

def check_number_buttons(pos):
    global hidden, start, curr_level

    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                print("Correct")
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                game_over()
                break
        
        # 모든 숫자를 맞췄다면 level을 높임
        if len(number_buttons) == 0:
            start = False
            hidden = False
            curr_level += 1
            setup(curr_level)

# 게임 종료 처리
def game_over():
    global running

    running = False
    msg = game_font.render(f"Your level is {curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width / 2, screen_height / 2))

    ## 종료 메세지 출력
    screen.fill(BLACK)
    screen.blit(msg, msg_rect)

# 초기화
pygame.init()  

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("MEMORY TEST")

# 폰트 설정
game_font = pygame.font.Font(None, 120)

# 시작버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120) # 좌하에서 120, 120 떨어져있음

# 색깔
BLACK = (0, 0, 0) #RGB 값
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

# 플레이어가 눌러야 하는 버튼들
number_buttons = []

# 현재 레벨
curr_level =1 

# 시간 정의
display_time = None # 보여지는 시간
start_ticks = None # 시간 계산 (현재 시간 정보를 저장)

# 게임 시작 여부 
start = False

# 숫자 숨김 여부 (사용자가 1을 클릭했거나, 보여주는 시간 초과했을 때)
hidden = False

# 게임 시작하기 전에 게임 설정 함수 수행
setup(curr_level)

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


    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)


    if start:
    # start이면 게임 화면 표시
        display_game_screen()
    else:
    # 시작 화면 표시
        display_start_screen()

    # 사용자가 클릭한 좌표값이 있다면 (어딘가 클릭했다면)
    if click_pos:
        check_buttons(click_pos)



    # 화면 업데이트
    pygame.display.update()

# 5초 정도 보여줌
pygame.time.delay(5000)

# pygame 종료

pygame.quit()