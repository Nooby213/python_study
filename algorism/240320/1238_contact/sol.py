# import sys
# sys.stdin = open('input.txt')
from collections import deque
def calls(n):
    visited = [0] * (max_num + 1)
    max_cnt = 0
    last_call = 0
    q = deque([(n, 0)])
    while q:
        now, cnt = q.popleft()
        if max_cnt < cnt:
            max_cnt = cnt
            last_call = now

        if max_cnt == cnt:
            last_call = max(last_call, now)

        for k in adj[now]:
            if visited[k] == 0:
                visited[k] = 1
                q.append((k, cnt + 1))
    return last_call

for t in range(1, 11):
    E, start = map(int, input().split())
    edge = []
    max_num = 0

    for i in input().split():
        max_num = max(int(i), max_num)
        edge.append(int(i))

    adj = [[] for _ in range(max_num + 1)]

    for i in range(E//2):
        adj[edge[2 * i]].append(edge[2 * i + 1])

    result = calls(start)
    print(f'#{t} {result}')