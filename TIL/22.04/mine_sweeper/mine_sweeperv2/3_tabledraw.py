from random import *
import pygame

# 게임 시작
def display_start_game():
    for table in tables:

        rect = pygame.Rect(0, 0, table_size, table_size)
        rect.center = table["center"]
        pygame.draw.rect(screen, WHITE, rect)

# 최초 화면
def display_waiting_game():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5) #(그릴 위치, 색, 중심점, 반지름, 두께)

# 버튼 체크
def check_buttons(pos):
    global start
    if start:
        pass
    
    elif start_button.collidepoint(pos):
        start = True

pygame.init() 

screen_width = 640
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height)) 

# 지뢰개수, 필드 사이즈, screen 여백
mine_number = 10
field_size = 20
table_size = (400 - ((field_size -1) * 2)) / field_size 

screen_left_margin = 120
screen_top_margin = 200

# 지뢰 설정
tables = []
for i in range(field_size):
    for j in range(field_size):
        tables.append({
            "status" : 0,
            "reveal" : 0, 
            "nearby" : 0, 
            "center" : (screen_left_margin + i * table_size + i, screen_top_margin + j * table_size + j), 
            "question" : 0
            })

mine_location = randint(0, field_size ** 2)

# 시작버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120) # 좌하에서 120, 120 떨어져있음
start = False

# 색깔
WHITE = (255, 255, 255)

running = True
while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()


    if start:
        display_start_game()
    else:
        display_waiting_game()

    if click_pos:
        check_buttons(click_pos)

    pygame.display.update()

#pygame.time.delay(5000)

pygame.quit()