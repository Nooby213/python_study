import sys

input = sys.stdin.readline

from collections import deque


def up():
    maxi = 0
    q = deque([(0, 0, 0)])
    while q:
        stair, score, cnt = q.popleft()
        if stair == N:
            maxi = max(maxi, score)

        if stair + 1 <= N and cnt + 1 <= 2:
            q.append((stair + 1, score + stairs[stair + 1], cnt + 1))

        if stair + 2 <= N:
            q.append((stair + 2, score + stairs[stair + 2], 1))
    return maxi

# +1 / +2, 연속된 계단 3개 못밟음, 마지막 계단 무조건 밟아야됨
# 계단 수 N, 1 <= N <= 300
N = int(input().rstrip())
# 점수 <= 10,000
stairs = deque([int(input().rstrip()) for _ in range(N)])
stairs.appendleft(0)
print(up())
