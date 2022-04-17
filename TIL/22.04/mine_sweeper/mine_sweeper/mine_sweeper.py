import pygame
import os
import random
pygame.init() 

screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height)) 

pygame.display.set_caption("Mine Sweeper")

clock = pygame.time.Clock()
DOUBLECLICKTIME = 100
# 이미지 불러오기
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 화면
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 지뢰지대
mine_land = pygame.image.load(os.path.join(image_path, "mine_land.png"))
mine_land_width = mine_land.get_rect().size[0]
mine_land_height = mine_land.get_rect().size[1]
number = pygame.image.load(os.path.join(image_path, "number.png"))
boom = pygame.image.load(os.path.join(image_path, "boom.png"))
flag = pygame.image.load(os.path.join(image_path, "flag.png"))
question = pygame.image.load(os.path.join(image_path, "question.png"))
numbers = [
    pygame.image.load(os.path.join(image_path, "nothing.png")),
    pygame.image.load(os.path.join(image_path, "1.png")),
    pygame.image.load(os.path.join(image_path, "2.png")),
    pygame.image.load(os.path.join(image_path, "3.png")),
    pygame.image.load(os.path.join(image_path, "4.png")),
    pygame.image.load(os.path.join(image_path, "5.png")),
    pygame.image.load(os.path.join(image_path, "6.png")),
    pygame.image.load(os.path.join(image_path, "7.png")),
    pygame.image.load(os.path.join(image_path, "8.png")),

    ]
status = [mine_land, number, boom, flag]

# 지뢰 개수와 위치 지정
table_size = 5
total_number = table_size ** 2
total_mine_number = 1

number_list = [i for i in range(1,total_number)]

mine_number_list = random.sample(number_list, total_mine_number)

# 지뢰 열 생성
mines = []
for i in range(table_size):
    for j in range(table_size):
        mines.append({
            "mine_land" : mine_land,
            "reveal" : 0, 
            "nearby" : 0, 
            "x_pos" : i * mine_land_width + i, 
            "y_pos" : j * mine_land_height + j,
            "question" : 0
            })

# 지뢰 넣기
for num in mine_number_list:
    mines[num] = {
            "mine_land" : boom,
            "reveal" : 0, 
            "nearby" : 0, 
            "x_pos" : mines[num]["x_pos"], 
            "y_pos" : mines[num]["y_pos"],
            "question" : 0
            }

# 주변 지뢰에 대한 상대적 위치 값 계산 [위, 아래, 오른쪽, 왼쪽, 우하, 우상, 좌상, 좌하]
locations = [
    -1,
    1,
    table_size,
    table_size * -1,
    table_size + 1,
    table_size - 1,
    (table_size + 1) * -1,
    (table_size - 1) * -1
]

## 주변 지뢰 개수 세고 나타내기
for mine_idx, mine_val in enumerate(mines):
    for location in locations:
        try:
            if mines[mine_idx + location]["mine_land"] == boom:
                mine_val["nearby"] += 1
        except:
            continue

## 지뢰가 아니고 nearby가 0 이상인 값에 대해 mine_land 변경
for mine_idx, mine_val in enumerate(mines):
    if mine_val["mine_land"] != boom:
        mine_val["mine_land"] = numbers[mine_val["nearby"]]

# 게임 결과
game_result = "Game over"

# 폰트 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if clock.tick() < DOUBLECLICKTIME:
                for mine_idx, mine_val in enumerate(mines):
                    revealed_mine = 0
                    cnt = 0

                    if mine_val["x_pos"] < mouse_x_pos < mine_val["x_pos"] + mine_land_width and mine_val["y_pos"] < mouse_y_pos < mine_val["y_pos"] + mine_land_height:
                        
                        if mine_val["reveal"] == 1:
                            
                            for location in locations:
                                try:
                                    if mines[mine_idx + location]["mine_land"] == boom and mines[mine_idx + location]["reveal"] == 1:
                                        revealed_mine += 1

                                    if mines[mine_idx + location]["reveal"] == 0 and mines[mine_idx + location]["question"] == 1:
                                        cnt += 1
                                except:
                                    continue

                            if revealed_mine == mine_val["nearby"]:
                                for location in locations:
                                    try:
                                        mines[mine_idx + location]["reveal"] = 1 
                                    except:
                                        continue

                            elif mine_val["nearby"] == revealed_mine + cnt:
                                for location in locations:
                                    try:
                                        mines[mine_idx + location]["reveal"] = 1 

                                        if mines[mine_idx + location]["mine_land"] != boom and mines[mine_idx + location]["question"] != 0:
                                            running = False
                                    except:
                                        continue  

                
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            (mouse_x_pos, mouse_y_pos) = pygame.mouse.get_pos()
            for mine_idx, mine_val in enumerate(mines):
                # 누르면 reaveal이 1로 바뀌면서 mine_land 가 표시됨
                if mine_val["x_pos"] < mouse_x_pos < mine_val["x_pos"] + mine_land_width and mine_val["y_pos"] < mouse_y_pos < mine_val["y_pos"] + mine_land_height:
                    if mine_val["mine_land"] == boom and mine_val["reveal"] == 0:
                        mine_val["reveal"] = 1
                        running = False
                        
                    mine_val["reveal"] = 1
                    
                
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            (mouse_x_pos, mouse_y_pos) = pygame.mouse.get_pos()
            for mine_idx, mine_val in enumerate(mines):
                if mine_val["x_pos"] < mouse_x_pos < mine_val["x_pos"] + mine_land_width and mine_val["y_pos"] < mouse_y_pos < mine_val["y_pos"] + mine_land_height:
                    if mine_val["reveal"] == 0 and mine_val["question"] == 0:
                        mine_val["question"] = 1
                    elif mine_val["reveal"] == 0 and mine_val["question"] == 1:
                        mine_val["question"] = 2
                    else:
                        mine_val["question"] = 0
        


    # 주변에 지뢰가 없는 칸에 대해서 주변이 모두 열리게 설정
    cnt = 0
    for mine_idx, mine_val in enumerate(mines):

        if mine_val["reveal"] == 1 and mine_val["nearby"] == 0:
            for location in locations:
                try:
                    mines[mine_idx + location]["reveal"] = 1
                except:
                    continue

        ##승리 조건
        if mine_val["reveal"] == 1 and mine_val["mine_land"] == boom:
            cnt += 1
    
    if cnt == total_mine_number:
        game_result = "Victory"
        running = False


    #배경 그리기
    screen.blit(background, (0, 0)) 

    # 마인 그리기
    for mine_idx, mine_val in enumerate(mines):
        mine_x_pos = mine_val["x_pos"]
        mine_y_pos = mine_val["y_pos"]
        if mine_val["reveal"] == 0 and mine_val["question"] == 0:
            screen.blit(mine_land, (mine_x_pos, mine_y_pos))
        elif mine_val["reveal"] == 0 and mine_val["question"] == 1:
            screen.blit(flag, (mine_x_pos, mine_y_pos))
        elif mine_val["reveal"] == 0 and mine_val["question"] == 2:
            screen.blit(question, (mine_x_pos, mine_y_pos))
        else:
            screen.blit(mine_val["mine_land"], (mine_x_pos, mine_y_pos))

    pygame.display.update()

msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)

pygame.display.update()

pygame.time.delay(2000)

# pygame 종료
pygame.quit()

