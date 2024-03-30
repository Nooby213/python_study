import sys

sys.stdin = open('input.txt')


# N * N 도착시 1 아니면 X
# 맨 밑의 2 > 맨 윗줄 3, 0을 타고 이동

def dfs(i, j):
    global result
    # i나 j가 미로는 벗어나면 x
    if i < 0 or i >= N or j < 0 or j >= N:
        return

    if maze[i][j] == 2:  # 2면 탈출!
        result = 1

    if maze[i][j] != 1:  # 1은 못 지나간다.
        maze[i][j] = 1
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    maze = [list(int(i) for i in input()) for _ in range(N)]

    # print(maze)

    result = 0
    a = 0
    b = 0

    for i in range(N):  # 출발지 지정
        for j in range(N):
            if maze[i][j] == 3:
                a = i
                b = j
                break

    dfs(a, b)
    # print(maze)
    print(f'#{t} {result}')
