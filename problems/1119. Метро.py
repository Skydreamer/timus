import math
from sys import stdin, stdout

n, m = [int(x) for x in stdin.readline().split(' ')]
diag_quartals = int(stdin.readline())

map = [[0 for y in range(m + 1)] for x in range(n + 1)]
map_diag = [[0 for y in range(m + 1)] for x in range(n + 1)]

for _ in range(diag_quartals):
    dx, dy = [int(x) for x in stdin.readline().split(' ')]
    map_diag[dx][dy] = 1

for y in range(m + 1):
    for x in range(n + 1):
        if y == 0 and x == 0:
            continue

        if map_diag[x][y] == 1:
            map[x][y] = map[x - 1][y - 1] + 141.42
        else:
            map[x][y] = min(
                map[x - 1][y] + 100 if x > 0 else 10000000,
                map[x][y - 1] + 100 if y > 0 else 10000000,
            )
        # print x, y, ' -> ', map[x][y]

stdout.write(str(int(math.ceil(map[x][y]))))

