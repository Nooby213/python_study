import sys

input = sys.stdin.readline
from collections import deque

# 상하좌우 안전
# 배추 1, 빈 땅 0
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bug(Y, X):
    q = deque([(Y, X)])
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and field[ni][nj]:
                field[ni][nj] = 0
                q.append((ni, nj))


T = int(input())
for t in range(T):
    # 배추밭 N * M, 1 ≤ N ≤ 50, 1 ≤ M ≤ 50, 배추 K 개, 1 ≤ K ≤ 2500
    # 배추 위치 Y(0 ≤ Y ≤ N-1), X(0 ≤ X ≤ M-1)
    M, N, K = map(int, input().split())
    mini_bug = 0
    field = [[0] * M for _ in range(N)]
    # 배추 심기
    for i in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    # 인접 배추 확인
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                bug(i, j)
                mini_bug += 1
    print(mini_bug)
