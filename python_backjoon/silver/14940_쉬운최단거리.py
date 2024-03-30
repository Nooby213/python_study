import sys
input = sys.stdin.readline
from collections import deque


def find_goal():
    global goal
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 2:
                goal = (i, j)
                return


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs():
    q = deque([(goal[0], goal[1])])
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and maze[ni][nj] == 1:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))

def cant_go():
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = -1

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
goal = ()
find_goal()
bfs()
cant_go()
for v in visited:
    print(*v)