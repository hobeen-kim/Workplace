# n, m = map(int, input().split())
# pos = list(map(int, input().split()))
# area = []
# for _ in range(n):
#     k = list(map(int, input().split()))
#     area.append(k)

n = 8
m = 4
pos = [1, 1, 0]
area = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]
direction = pos[2]
x = pos[1]
y = pos[0]
running = True
cnt = 0
cnt_loc = 1
area[x][y] = 2
x_move = [0, -1, 0, 1]
y_move = [-1, 0, 1, 0]
while running:

    for i in range(4):
        if direction == i and cnt != 4:
            if direction > 0:
                direction -= 1
            else:
                direction += 3

            if area[x+x_move[i]][y+y_move[i]] == 0:
                area[x+x_move[i]][y+y_move[i]] = 2
                x += x_move[i]
                y += y_move[i]
                cnt = 0
                cnt_loc += 1

    cnt += 1

    if cnt == 4:
        if area[x-x_move[i]][y-y_move[i]] == 1:
            running = False
        else:
            x -= x_move[i]
            y -= y_move[i]
            cnt = 0
            continue
        
print(cnt_loc)
for i in range(n):
    for j in range(m):
        print(area[i][j], end=" ")
    print()
    
        
            
