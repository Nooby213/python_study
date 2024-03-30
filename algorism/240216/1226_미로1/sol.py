import sys
from collections import deque

sys.stdin = open('input.txt')

di = [-1, 1, 0, 0]  # 상, 하
dj = [0, 0, -1, 1]  # 좌, 우

def bfs(i, j):
    global result2
    stack = deque()
    stack.append((i, j))
    while stack:
        k, l = stack.popleft()
        maze[k][l] ='1'
        for n in range(4):
            nk = k + di[n]
            nl = l + dj[n]
            if maze[nk][nl] != '1':
                stack.append((nk, nl))
            if maze[nk][nl] == '3':
                result2 = 1
                break

for t in range(1, 11):
    # 미로는 16 * 16
    T = int(input())
    maze = [list(map(str, input())) for _ in range(16)]

    # (1, 1) 출발

    result2 = 0
    bfs(1, 1)
    print(f'#{T} {result2}')
