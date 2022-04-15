import enemys

lsts = []
for _ in range(4):
    lst = enemys.Enemy(
        1,
        2,
        3,
        4, 
        5, 
        6
        )
    lsts.append(lst)

lsts[0].enemy_x_pos += 1
print(lsts[0].enemy_x_pos)