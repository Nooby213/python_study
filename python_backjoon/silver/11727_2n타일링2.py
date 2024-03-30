# 2 * N 직사각형, 1 ≤ n ≤ 1,000
# 1*2, 2*1, 2*2 타일로 채우는 방법의 수
# def tile(n):
#     if tiles[n]:
#         return tiles[n]
#     tiles[n] = tile(n - 1) + (2 * tile(n - 2))
#     return tiles[n]
N = int(input())
tiles = [0] * (N + 1)
# print(tile(N) % 10007)

for i in range(1, N):
    if i == 1:
        tiles[i] = 1
    elif i == 2:
        tiles[i] = 3
    else:
        tiles[i] = tiles[i - 1] + (2 * tiles[i - 2])
else:
    print(tiles[N] % 10007)