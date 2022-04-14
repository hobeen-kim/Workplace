n = int(input())
cnt = 0
all = (n+1) * 3600
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if not "3" in str(i) and not "3" in str(j) and not "3" in str(k):
                cnt += 1

print(all - cnt)

