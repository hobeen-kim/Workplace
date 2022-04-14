n = int(input())
moves = list(map(str,input().split()))
x = 1
y = 1
for move in moves:
    if move == "L" and y != 1:
        y -= 1
    elif move == "R" and y != n:
        y += 1
    elif move == "U" and x != 1:
        x -= 1
    elif move == "D" and x != n:
        x += 1
    else:
        continue

print(x, y)
