import sys

input = sys.stdin.readline
from collections import deque


def is_colored(y, x, n):
    for i in range(n):
        for j in range(n):
            if paper[y + i][x + j] == 0:
                return False
    return True


def is_white(y, x, n):
    for i in range(n):
        for j in range(n):
            if paper[y + i][x + j] == 1:
                return False
    return True


# 종이 크기 N * N, N = 2^k, 1 <= k <= 7
N = int(input().rstrip())
paper = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0
info = deque([(0, 0, N)])
while info:
    i, j, n = info.popleft()
    if is_colored(i, j, n):
        blue += 1
    elif is_white(i, j, n):
        white += 1
    else:
        for k in range(4):
            di = [0, 0, n // 2, n // 2]
            dj = [0, n // 2, 0, n // 2]
            ni = i + di[k]
            nj = j + dj[k]
            if n // 2:
                info.append((ni, nj, n // 2))
print(white)
print(blue)
