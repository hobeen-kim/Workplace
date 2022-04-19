from random import *
rows = 5
columns = 9
number_count = 5
## 5 X 9 채우기
grid = [[0 for col in range(columns)] for row in range(rows)]

number = 1 #시작 숫자를 1부터 number_count 까지 넣기 위해 변수 설정
while number <= number_count:
    x = randint(0, rows -1 )
    y = randint(0, columns -1)
    if grid[x][y] == 0:
        grid[x][y] = number
        number += 1

for i in range(rows):
    for j in range(columns):
        print(grid[i][j], end= " ")
    print()