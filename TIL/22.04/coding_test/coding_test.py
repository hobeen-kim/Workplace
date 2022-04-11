place = []
for i in range(10):
    k = list(map(int, input().split()))
    place.append(k)
    
'''place = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]'''

x = 1
y = 1
cur_point = place[x][y]
right_point = place[x][y+1]
below_point = place[x+1][y]

moving = True
while moving:
    if place[x][y] == 2:
        place[x][y] = 9
        moving = False

    if place[x][y] == 0:
        place[x][y] = 9

    if place[x][y+1] == 0 or place[x][y+1] == 2:
        y += 1

    elif place[x+1][y] == 0 or place[x+1][y] == 2:
        x += 1
        
    else:
        moving = False

for i in range(10):
    k = list(map(str, place[i]))
    print(" ".join(k))





