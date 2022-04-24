def CalNearby(idx):
    for nearby in nearby_range:
        dx = nearby[0]
        dy = nearby[1]
        cells_move = dx * field_size + dy
        print(cells_move)

nearby_range = [(1, 2), (3, 4)]

field_size = 10

CalNearby(5)