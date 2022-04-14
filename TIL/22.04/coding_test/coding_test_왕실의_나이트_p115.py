# 나이트 이동 (8x8)
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한칸 이동
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한칸 이동
# 어느 한 좌표에서 나이트가 이동가능한 경우의 수는?

lst = input()
dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
place = [lst[:1], int(lst[1])]
cnt = 0
moves = [(2, 1), (2, -1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for move in moves:
    x = dic[place[0]]
    y = place[1]
    x += move[0]
    y += move[1]
    if x > 0 and x < 9 and y > 0 and y < 9:
        cnt += 1
    
print(cnt)


