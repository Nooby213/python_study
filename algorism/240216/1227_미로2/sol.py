import sys
sys.stdin = open('input.txt')
from collections import deque

di = [-1, 1, 0, 0]  # 상, 하
dj = [0, 0, -1, 1]  # 좌, 우

# 도착 1 못함 0
# 벽 1, 길 0, 출발 2, 도착 3
def bfs():
    result = 0
    queue = deque([(1, 1)]) # 출발 지점

    while queue:
        i, j = queue.popleft()
        maze[i][j] = 1
        for n in range(4):
            ni = i + di[n]
            nj = j + dj[n]
            if maze[ni][nj] != 1:
                queue.append((ni, nj))
            if maze[ni][nj] == 3:
                result = 1
                return result
    else:
        return result


for _ in range(1, 11):
    t = int(input())

    maze = [[int(i) for i in input()] for _ in range(100)]  # 100 * 100

    print(f'#{t} {bfs()}')   # 출발점 1, 1