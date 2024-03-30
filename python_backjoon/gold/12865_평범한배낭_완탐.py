import sys


def backpack(n, temp_weight, temp_value):
    global max_value

    max_value = max(max_value, temp_value)

    for i in range(n, N):
        if visited[i] == 0 and temp_weight + items[n][0] <= K:
            visited[n] = 1
            backpack(n + 1, temp_weight + items[n][0], temp_value + items[n][1])
            visited[n] = 0


input = sys.stdin.readline  # N개의 물건, 1 ≤ N ≤ 100, # 최대 무게 K, 1 ≤ K ≤ 100,000
N, K = map(int, input().split())
# (W, V),  무게 W, 1 ≤ W ≤ 100,000, 가치 V, 0 ≤ V ≤ 1,000
weight_sum = 0
value_sum = 0
items = []
for _ in range(N):
    W, V = map(int, input().split())
    if W <= K:
        items.append((W, V))
        weight_sum += W
        value_sum += V

if weight_sum <= K:
    print(value_sum)

else:
    items.sort(key=lambda x: (x[0], x[1]))
    max_value = 0
    visited = [0] * (N + 1)
    backpack(0, 0, 0)
    print(max_value)
