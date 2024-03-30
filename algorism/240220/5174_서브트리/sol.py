import sys

sys.stdin = open('input.txt')


# 이진 트리
# 부모가 없는 노드는 루트 노드
def find_subtree(now):
    global cnt
    if now:
        find_subtree(adj[now][0])
        cnt += 1
        find_subtree(adj[now][1])


T = int(input())  # tc
for t in range(1, T + 1):
    # E : 간선 개수, N을 루트로 하는 서브 트리에 속한 노드의 개수
    # 1<=E<=1000, 1<=N<=E+1
    E, N = map(int, input().split())
    adj = [[0, 0] for _ in range(E + 2)]  # 노드 번호는 1 ~ E + 1 번까지 존재
    edges = list(map(int, input().split()))

    for i in range(E):  # 노드를 만든다.
        if adj[edges[2 * i]][0] == 0:
            adj[edges[2 * i]][0] = edges[2 * i + 1]

        else:
            adj[edges[2 * i]][1] = edges[2 * i + 1]
    # print(adj)

    cnt = 0
    find_subtree(N)
    print(f'#{t} {cnt}')
