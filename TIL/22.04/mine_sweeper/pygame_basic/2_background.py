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

#배경이미지 불러오기
background = pygame.image.load("C:\\Users\\USER\\Desktop\\workplace\\TIL\\22.04\\mine_sweeper\\pygame_basic\\background.png")

# 이번트 루프 (창이 꺼지지 않도록)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #배경 그리기
    screen.blit(background, (0, 0)) #screen.fill((0, 0, 255)) .. 파란색으로 채우기

    #게임 화면을 다시 그리기(반드시 계속 호출되어야 함)
    pygame.display.update()

# pygame 종료
pygame.quit()