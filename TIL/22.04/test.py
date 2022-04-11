plate = []
sticks = [] #길이, 방향, x좌표, y좌표
h, w = map(int, input().split())
number = int(input())
for i in range(number):
    k = list(map(int, input().split()))
    sticks.append(k)

for i in range(h):
    plate.append([])
    for j in range(w):
        plate[i].append(0)




for i in range(number):
    try:
        length = sticks[i][0]
        direction = sticks[i][1]
        x = sticks[i][2]-1
        y = sticks[i][3]-1
        if plate[x][y] == 1:
            pass
        else:
            plate[x][y] = 1
            if direction == 0:
                for i in range(1, length):
                    if plate[x][y+i] == 0:
                        plate[x][y+i] = 1
                    else:
                        pass


            if direction == 1:
                for i in range(1, length):
                    if plate[x+i][y] == 0:
                        plate[x+i][y] = 1
                    else:
                        pass
    except IndexError as e:
        print(f"{i-1}번째 스틱 오류")
                    
            
for i in range(h):
    k = list(map(str, plate[i]))
    print(" ".join(k))