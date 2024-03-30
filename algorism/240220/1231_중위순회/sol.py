import sys

sys.stdin = open('input.txt')


def inorder(now):  # 중위 순회
    if now:
        inorder(adj[now][0])
        print(node_lst[now], end='')
        inorder(adj[now][1])


for t in range(1, 11):
    N = int(input())
    node_lst = [0] * (N + 1)
    adj = [[0, 0] for _ in range(N + 1)]

    for _ in range(N):  # 정보 받아오기 (자식 노드, 노드의 알파벳)
        info = list(input().split())
        node_lst[int(info[0])] = info[1]
        if len(info) == 3:
            adj[int(info[0])] = [int(info[2]), 0]

        elif len(info) == 4:
            adj[int(info[0])] = [int(info[2]), int(info[3])]

    print(f'#{t} ',end='')
    inorder(1)
    print()
