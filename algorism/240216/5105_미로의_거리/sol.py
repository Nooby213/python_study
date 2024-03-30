import sys
from collections import deque

sys.stdin = open('input.txt')

di = [-1, 1, 0, 0]  # 상, 하
dj = [0, 0, -1, 1]  # 좌, 우


def bfs(i, j):
    global result
    global N

    stack = deque()
    stack.append((i, j))
    while stack:
        k, l = stack.popleft()
        if maze[k][l] == 2:
            result = True
            break
        for n in range(4):  # 4방향 탐색
            nk = k + di[n]
            nl = l + dj[n]
            # 미로를 안 벗어나고 방문한 적 없을 때
            if nk >= 0 and nk < N and nl >= 0 and nl < N and maze[nk][nl] != 1 and visited[nk][nl] == 0:
                stack.append((nk, nl))
                visited[nk][nl] = visited[k][l] + 1





# 최소경로, 없으면 0
# 1은 벽, 0은 통로

T = int(input())
for t in range(1, T + 1):
    N = int(input())  # N * N
    maze = [[int(i) for i in input()] for _ in range(N)]  # 미로 만들기
    visited = [[0] * N for _ in range(N)]   # 몇 칸 이동했었는지
    si, sj = 0, 0
    ei, ej = 0, 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:  # 출발 위치
                si, sj = i, j

            if maze[i][j] == 2:
                ei, ej = i, j

        if maze[si][sj] == 3 and maze[ei][ej] == 2:  # 탈출 위치
            break

    result = False

    bfs(si, sj)

    if result == True:
        print(f'#{t} {visited[ei][ej] - 1}')    # 2까지 포함해서 -1
    else:
        print(f'#{t} 0')
