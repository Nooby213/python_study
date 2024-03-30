import sys

input = sys.stdin.readline
from collections import deque

dy = [-1, 1, 0, 0]  # 상 하
dx = [0, 0, -1, 1]  # 좌 우


def group(y, x):
    apart_cnt = 1
    q = deque([(y, x)])
    apartments[y][x] = 0
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N and apartments[ny][nx] == 1:
                apartments[ny][nx] = 0
                q.append((ny, nx))
                apart_cnt += 1
    return apart_cnt


# N * N, 5 ≤ N ≤ 25
N = int(input().rstrip())
# 단지 리스트
apartments = [[int(i) for i in input().rstrip()] for _ in range(N)]
cnt = 0
group_cnt = []
for i in range(N):
    for j in range(N):
        if apartments[i][j]:
            cnt += 1
            group_cnt.append(group(i, j))

group_cnt.sort()
print(cnt)
for i in group_cnt:
    print(i)
