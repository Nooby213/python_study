# N * M 미로
# 1 은 이동할 수 있는 칸, 0은 이동 못하는 칸
# 0, 0에서 출발
from collections import deque


def bfs(i, j):
    queue = deque([(i, j)])

    while queue:
        k, l = queue.popleft()

        if k == N and l == M:
            break

        if maze[k][l] != 0:  # 갈 수 있다면

            if k - 1 >= 0 and maze[k - 1][l] == 1:  # 위로 갈 수 있다면
                maze[k - 1][l] = maze[k][l] + 1
                queue.append((k - 1, l))

            if k + 1 < N and maze[k + 1][l] == 1:  # 아래로 갈 수 있다면
                maze[k + 1][l] = maze[k][l] + 1
                queue.append((k + 1, l))

            if l - 1 >= 0 and maze[k][l - 1] == 1:  # 왼쪽으로 갈 수 있다면
                maze[k][l - 1] = maze[k][l] + 1
                queue.append((k, l - 1))

            if l + 1 < M and maze[k][l + 1] == 1:  # 오른쪽으로 갈 수 있다면
                maze[k][l + 1] = maze[k][l] + 1
                queue.append((k, l + 1))


di = [-1, 1, 0, 0]  # 상, 하
dj = [0, 0, -1, 1]  # 좌, 우


def bfs_delta(i, j):
    queue = deque([(i, j)])
    # queue.append((i, j))
    while queue:
        k, l = queue.popleft()
        for m in range(4):
            nk = k + di[m]
            nl = l + dj[m]

            if nk < 0 or nk >= N or nl < 0 or nl >= M:  # 범위를 벗어나면
                continue

            if maze[nk][nl] != 1:  # 왔던 길이거나 못가는 길이라면
                continue

            if maze[nk][nl] == 1:  # 길이 있다면
                maze[nk][nl] = maze[k][l] + 1
                queue.append((nk, nl))


N, M = map(int, input().split())
maze = [[int(i) for i in input()] for _ in range(N)]
# print(maze)

# bfs(0, 0)
bfs_delta(0, 0)
print(maze[N - 1][M - 1])
