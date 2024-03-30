import sys

input = sys.stdin.readline
from collections import deque

dy = [-1, 1, 0, 0]  # 상 하
dx = [0, 0, -1, 1]  # 좌 우


def ripe(alist):
    max_day = 0
    q = deque()
    for k in alist:
        q.append(k)

    while q:
        y, x, day = q.popleft()
        for w in range(4):
            ny = y + dy[w]
            nx = x + dx[w]
            if 0 <= ny < N and 0 <= nx < M and tomatoes[ny][nx] == 0:
                tomatoes[ny][nx] = 1
                max_day = day + 1
                q.append((ny, nx, day + 1))
    return max_day


def can():
    for t in tomatoes:
        if t.count(0):
            return False
    else:
        return True


# 익은 토마토 상하좌우 익는다.
# 상자 크기 M, N, 2 ≤ M, N ≤ 1,000
M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

cnt0 = 0
ripen_tomatoes = []
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            ripen_tomatoes.append((i, j, 0))
        elif tomatoes[i][j] == 0:
            cnt0 += 1

# 안 익은 토마토 없으면
if cnt0 == 0:
    print(0)

else:
    result = ripe(ripen_tomatoes)
    if can():
        print(result)
    else:
        print(-1)
