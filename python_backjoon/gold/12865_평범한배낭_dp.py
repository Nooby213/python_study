import sys

input = sys.stdin.readline
# N개의 물건, 1 ≤ N ≤ 100, # 최대 무게 K, 1 ≤ K ≤ 100,000
N, K = map(int, input().split())
# (W, V),  무게 W, 1 ≤ W ≤ 100,000, 가치 V, 0 ≤ V ≤ 1,000
backpack = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = map(int, input().split())
    for j in range(1, K + 1):
        if j < w:  # 물건을 가방에 넣을 수 없는 경우
            backpack[i][j] = backpack[i - 1][j]
        else:  # 물건을 가방에 넣을 수 있는 경우
            backpack[i][j] = max(backpack[i - 1][j], backpack[i - 1][j - w] + v)


print(backpack[N][K])
