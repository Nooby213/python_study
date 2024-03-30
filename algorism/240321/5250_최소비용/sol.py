import sys
sys.stdin = open('input.txt')
from collections import deque
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs():
    visited = [([0] * N) for _ in range(N)]
    q = deque([(0, 0)])
    while q:
        i, j = q.popleft()
        # 4방향 탐색
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # 처음 가는 길이라면
                if visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    # 다음 길이 높다면
                    if maps[ni][nj] > maps[i][j]:
                        visited[ni][nj] += maps[ni][nj] - maps[i][j]
                    q.append((ni, nj))
                # 간 적이 있다면
                else:
                    # 다음 길이 높다면
                    if maps[ni][nj] > maps[i][j]:
                        if visited[ni][nj] > maps[ni][nj] - maps[i][j] + visited[i][j] + 1:
                            visited[ni][nj] = maps[ni][nj] - maps[i][j] + visited[i][j] + 1
                            q.append((ni, nj))
                    # 낮거나 같으면
                    else:
                        if visited[ni][nj] > visited[i][j] + 1:
                            visited[ni][nj] = visited[i][j] + 1
                            q.append((ni, nj))


    print(f'#{t} {visited[N - 1][N - 1]}')

# 출발은 0,0 도착지는 N-1, N-1
T = int(input())

for t in range(1, T + 1):
    # 3 <= N <= 100
    N = int(input())
    # 0 <= H < 1000
    maps = [list(map(int, input().split())) for _ in range(N)]
    bfs()