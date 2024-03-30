import sys
sys.stdin = open('input.txt')
from collections import deque

pm = [1, 0, -1, -10]
def change(n, target):
    global mini
    q = deque([(n, 0)])
    visited.add(N)

    while q:
        n, cnt = q.popleft()
        if n == target:
            return cnt

        for k in range(4):
            if pm[k]:
                nn = n + pm[k]
            else:
                nn = 2 * n
            if 0 < nn < 1000001 and nn not in visited:
                visited.add(nn)
                q.append((nn, cnt + 1))


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    visited = set()
    mini = change(N, M)

    print(f'#{t} {mini}')
