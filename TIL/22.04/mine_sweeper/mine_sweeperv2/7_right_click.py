from random import *
import pygame
##남은 과제
# nearby class 만들기
# 마우스 누르고 대기할 때 상태 출력
# 종료 조건 설정
# 시간 출력
# level 선택

# 게임 시작
def display_start_game():
    for cell in cells:
        rect = cell["rect"]
        rect.center = cell["center"]

        ## hide 된 상태
        if cell["reveal"] == 0:
            pygame.draw.rect(screen, WHITE, rect)
            ### 느낌표 그리기
            if cell["right_button"] == 1:
                cell_text = game_font_cell.render("!", True, GRAY)
                text_rect = cell_text.get_rect(center = rect.center)
                screen.blit(cell_text, text_rect)
            ### 물음표 그리기
            if cell["right_button"] == 2:
                cell_text = game_font_cell.render("?", True, GRAY)
                text_rect = cell_text.get_rect(center = rect.center)
                screen.blit(cell_text, text_rect)

        ## reveal 되면
        else:
            ### 지뢰일 때
            if cell["status"] == 1:
                cell_text = game_font_cell.render("M", True, GRAY)
                text_rect = cell_text.get_rect(center = rect.center)
                screen.blit(cell_text, text_rect)

            ### 지뢰가 아닐 때
            else:
                cell_text = game_font_cell.render(str(8-cell["nearby"]), True, GRAY)
                text_rect = cell_text.get_rect(center = rect.center)
                screen.blit(cell_text, text_rect)

    
# 최초 화면
def display_waiting_game():
    pygame.draw.circle(screen, WHITE, start_button.center, 30, 5) #(그릴 위치, 색, 중심점, 반지름, 두께)

# 왼쪽 버튼 체크
def check_left_buttons(pos):
    global start
    if start:
        for cell in cells:
            if cell["rect"].collidepoint(pos):
                cell["reveal"] = 1
    
    elif start_button.collidepoint(pos):
        start = True

# 오른쪽 버튼 체크
def check_right_buttons(pos):
    ## right_button이 0부터 1씩 증가(최대 2)
    for cell in cells:
        if cell["rect"].collidepoint(pos):
            if cell["right_button"] == 2:
                cell["right_button"] = 0
            else:
                cell["right_button"] += 1

# 더블클릭 체크
def check_double_bottons(pos):
    for idx, cell in enumerate(cells):
        cnt = 0
        if cell["rect"].collidepoint(pos):
            for nearby in nearby_range:
                dx = nearby[0]
                dy = nearby[1]
                if -1 < cell["x_pos"] + dx < field_size and -1 < cell["y_pos"] + dy < field_size:
                    cells_move = dx * field_size + dy
                    nearby_cell = cells[idx + cells_move]
                    if nearby_cell["status"] == 1:
                        if nearby_cell["reveal"] == 0 and nearby_cell["right_button"] == 1:
                            cnt += 1
                        elif nearby_cell["reveal"] == 1:
                            cnt += 1
            if cnt > 0 and cnt == cell["nearby"]:
                print(f"{idx} + 성공")
                for nearby in nearby_range:
                    dx = nearby[0]
                    dy = nearby[1]
                    if -1 < cell["x_pos"] + dx < field_size and -1 < cell["y_pos"] + dy < field_size:
                        cells_move = dx * field_size + dy
                        nearby_cell = cells[idx + cells_move]
                        nearby_cell["reveal"] = 1
                cnt = 0

        #     for nearby in nearby_range:
        #         dx = nearby[0]
        #         dy = nearby[1]
        #         if -1 < cell["x_pos"] + dx < field_size and -1 < cell["y_pos"] + dy < field_size:
        #             cells_move = dx * field_size + dy
        #             nearby_cell = cells[idx + cells_move]
        #             if nearby_cell["reveal"] == 0 and nearby_cell["status"] == 0 and nearby_cell["right_button"] == 1:
        #                 print("lose")
        #             else:
        #                 nearby_cell["reveal"] = 1
                        
pygame.init() 

screen_width = 640
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption("MINE SWEEPER_v2")

# 지뢰개수, 필드 사이즈, screen 여백
mine_number = 30
field_size = 20
cell_size = (500 - ((field_size -1) * 2)) / field_size 

screen_left_margin = 70
screen_top_margin = 150

# 셀 및 지뢰 설정
cells = []
cell_rects = []
for i in range(field_size):
    for j in range(field_size):
        cells.append({
            "status" : 0, # 0이면 지뢰x, 1이면 지뢰
            "x_pos" : i,
            "y_pos" : j,
            "reveal" : 0, 
            "nearby" : 0, 
            "checked" : 0,
            "rect" : pygame.Rect(0, 0, cell_size, cell_size),
            "center" : (screen_left_margin + i * cell_size + i * 2 + cell_size/2, screen_top_margin + j * cell_size + j * 2 + cell_size/2), 
            "right_button" : 0
            })

mine_locations = [randrange(0, field_size ** 2) for i in range(mine_number)]

## 지뢰 설정
for location in mine_locations :
    cells[location]["status"] = 1
    
# nearby 설정
nearby_range = [(-1, -1), (-1, 0), (-1, 1), (0, 1), 
                (0, -1), (1, -1), (1, 0), (1, 1)]

for idx, cell in enumerate(cells):
    for nearby in nearby_range:
        dx = nearby[0]
        dy = nearby[1]
        cells_move = dx * field_size + dy
        if -1 < cell["x_pos"] + dx < field_size and -1 < cell["y_pos"] + dy < field_size:
            if cells[idx + cells_move]["status"] == 1:
                cell["nearby"] += 1

# 시작버튼
start_button = pygame.Rect(0, 0, 30, 30)
start_button.center = (60, 60) # 좌하에서 120, 120 떨어져있음
start = False

# 색깔
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
BLACK = (0, 0, 0)

# 더블클릭을 위한 시간 설정
clock = pygame.time.Clock()
DOUBLECLICKTIME = 100

# 폰트 설정
game_font_cell = pygame.font.Font(None, int(cell_size))

running = True
while running:
    left_click_pos = None
    right_click_pos = None
    double_click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            if clock.tick() < DOUBLECLICKTIME:
                double_click_pos = pygame.mouse.get_pos()
            
            else:
                if event.button == 1:
                    left_click_pos = pygame.mouse.get_pos()

                elif event.button == 3:
                    right_click_pos = pygame.mouse.get_pos()

    # 스크린 까맣게 칠하기 및 지뢰 뒤 배경
    screen.fill(BLACK)
    pygame.draw.rect(screen, (60, 60, 60),(screen_left_margin, screen_top_margin, 500, 500))

    if start:
        display_start_game()
    else:
        display_waiting_game()

    if left_click_pos:
        check_left_buttons(left_click_pos)

    if right_click_pos:
        check_right_buttons(right_click_pos)

    if double_click_pos:
        check_double_bottons(double_click_pos)

    ## 아무것도 없는 셀 주변 열기
    for idx, cell in enumerate(cells):
        if cell["reveal"] == 1 and cell["nearby"] == 0:
           for nearby in nearby_range:
                dx = nearby[0]
                dy = nearby[1]
                if -1 < cell["x_pos"] + dx < field_size and -1 < cell["y_pos"] + dy < field_size:
                    cells_move = dx * field_size + dy
                    nearby_cell = cells[idx + cells_move]
                    nearby_cell["reveal"] = 1   

    pygame.display.update()

#pygame.time.delay(5000)

pygame.quit()