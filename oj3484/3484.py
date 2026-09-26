"""Tile clanking"""
def main():
    """I don't know what I'm doing!"""
    data = input().split()
    n, p = int(data[0]), float(data[1])
    tiles = []
    for _ in range(n):
        tiles.append(list(map(int, input().split())))
    for i in range(n):
        def_tiles = sum(1 for t in tiles[i] if t > 0)
        print(*(tiles[i] + [def_tiles, sum(tiles[i])]))
    col_def_tiles, col_total = [], []
    total_def_tiles = 0
    total_sound = 0
    for j in range(n):
        def_tiles = 0
        total = 0
        for i in range(n):
            v = tiles[i][j]
            total += v
            total_sound += v
            if v > 0:
                total_def_tiles += 1
                def_tiles += 1
        col_def_tiles.append(def_tiles)
        col_total.append(total)
    print(*col_def_tiles)
    print(*col_total)
    print(total_def_tiles, total_sound, f"{total_sound * p:.2f}")
main()
