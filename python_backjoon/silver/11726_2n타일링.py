# 1*2, 2*1 타일로 채우는법
tiles = [0] * 1001
tiles[1] = 1
tiles[2] = 2
# 1 <= N <= 1,000
N = int(input())
for i in range(3, N + 1):
    tiles[i] = tiles[i - 1] + tiles[i - 2]
print(tiles[N] % 10007)
