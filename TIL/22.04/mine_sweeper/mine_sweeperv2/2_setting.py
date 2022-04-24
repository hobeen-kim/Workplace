from random import *
import pygame

# 게임 시작
def display_start_game():
    for table in tables:
        print(table["center"])

# 최초 화면
def display_waiting_game():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5) #(그릴 위치, 색, 중심점, 반지름, 두께)

# 버튼 체크
def check_buttons(pos):
    if start:
        display_start_game()
    
    else:
        display_waiting_game()

pygame.init() 

screen_width = 640
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height)) 

mine_number = 10
table_size = 10
table_size = 10

# 지뢰 설정
tables = []
for i in range(table_size):
    for j in range(table_size):
        tables.append({
            "status" : 0,
            "reveal" : 0, 
            "nearby" : 0, 
            "center" : (i * 15 + i, j * 15 + j), 
            "question" : 0
            })

mine_location = randint(0, table_size ** 2)

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