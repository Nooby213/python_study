import sys

sys.stdin = open('input.txt')


def to_do(v):
    if adj[v]:
        for nv in adj[v]:
            if visited[nv] == 0:
                visited[nv] = 1
                to_do(nv)
        else:
            if v not in to_do_list:
                to_do_list.append(v)
    else:
        if v not in to_do_list:
            to_do_list.append(v)


for t in range(1, 11):
    # 해야할 작업 V, 간선 E
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))
    adj = [[] for _ in range(V + 1)]
    # 부모 노드를 저장
    for i in range(E):
        adj[edge[2 * i + 1]].append(edge[2 * i])
    visited = [0] * (V + 1)
    to_do_list = []
    print(f'#{t}', end=' ')
    for i in range(1, V + 1):
        to_do(i)
    print(*to_do_list)
