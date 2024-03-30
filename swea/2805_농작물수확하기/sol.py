import sys

sys.stdin = open('input.txt')
from collections import deque


# N * N 홀수, 1 ≤ N ≤ 49
def harvest(n):
    global cnt
    start = deque([(n, n)])
    # N // 2 회만큼 4 방향으로 전진
    time = (N // 2) * 4 + 1
    while start:
        y, x = start.popleft()
        # 나아간 방향에서 N // 2 만큼 더 전진
        for k in range(n + 1):
            dy = [-k, k, 0, 0]  # 상, 하
            dx = [0, 0, -k, k]  # 좌, 우
            for l in range(4):
                ny = y + dy[l]
                nx = x + dx[l]
                if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
                    start.append((ny, nx))
                    visited[ny][nx] = 1
                    cnt += int(farm[ny][nx])
        time -= 1
        if time % 4 == 0:
            n -= 1


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    farm = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    harvest(N // 2)
    print(f'#{t} {cnt}')
