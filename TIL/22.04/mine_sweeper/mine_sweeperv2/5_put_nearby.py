from random import *
import pygame

# 게임 시작
def display_start_game():
    for cell in cells:
        rect = pygame.Rect(0, 0, cell_size, cell_size)
        rect.center = cell["center"]
        pygame.draw.rect(screen, WHITE, rect)
        if cell["status"] == 1:
            cell_text = game_font_cell.render("M", True, GRAY)
            text_rect = cell_text.get_rect(center = rect.center)
            screen.blit(cell_text, text_rect)
        else:
            cell_text = game_font_cell.render(str(cell["nearby"]), True, GRAY)
            text_rect = cell_text.get_rect(center = rect.center)
            screen.blit(cell_text, text_rect)

    

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

# 화면 타이틀 설정
pygame.display.set_caption("MINE SWEEPER_v2")

# 지뢰개수, 필드 사이즈, screen 여백
mine_number = 10
field_size = 20
cell_size = (400 - ((field_size -1) * 2)) / field_size 

screen_left_margin = 120
screen_top_margin = 200

# 셀 및 지뢰 설정
cells = []
for i in range(field_size):
    for j in range(field_size):
        cells.append({
            "status" : 0, # 0이면 지뢰x, 1이면 지뢰
            "x_pos" : i,
            "y_pos" : j,
            "reveal" : 0, 
            "nearby" : 0, 
            "center" : (screen_left_margin + i * cell_size + i, screen_top_margin + j * cell_size + j), 
            "question" : 0,
            "blank" : 0 # 0이면 표시, 1이면 주위에 지뢰없음
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
            if cells[idx + cells_move]["status"] == 0:
                cell["nearby"] += 1

# 시작버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120) # 좌하에서 120, 120 떨어져있음
start = False

# 색깔
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
BLACK = (0, 0, 0)

# 폰트 설정
game_font_cell = pygame.font.Font(None, int(cell_size))

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