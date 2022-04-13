n, k = map(int, input().split())
cnt = 0
while True:
    if n <= 1:
        break
    div = n%k #k로 나눴을 때 나머지는 전부 바로 cnt에 더해줌
    cnt += div
    n -= div # n은 k의 배수
    n /= k
    cnt += 1

print(cnt)

