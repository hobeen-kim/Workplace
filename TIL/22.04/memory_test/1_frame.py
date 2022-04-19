import pygame

# 초기화
pygame.init()  

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("MEMORY TEST")

# 이번트 루프 (창이 꺼지지 않도록)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# pygame 종료

pygame.quit()