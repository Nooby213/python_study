import sys
input = sys.stdin.readline

n, m = map(int, sys.stdin.readline().split())
cnt = 0
combinations = [[False] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    combinations[a - 1][b - 1] = True
    combinations[b - 1][a - 1] = True

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not combinations[i][j] and not combinations[j][k] and not combinations[k][i]:
                cnt += 1

print(cnt)