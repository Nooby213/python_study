import sys

sys.stdin = open('input.txt')


# 사칙연산 표
# 정점에 연산자 있으면 자식 1, 2 숫자를 연산한다.
# 실수 연산으로 처리한다 / > //
def postorder(n):  # 후위 순회
    if node_lst[n] in '+-*/':  # 연산자라면
        # 왼쪽 자식 노드부터 탐색
        postorder(adj[n][0])
        postorder(adj[n][1])
        # 순회끝나면 연산(자식 노드 2개 다 숫자면)
        # 연산하고 그 자리에 결과값 넣어준다.
        if node_lst[n] == '+':
            node_lst[n] = int(node_lst[adj[n][0]]) + int(node_lst[adj[n][1]])
        elif node_lst[n] == '-':
            node_lst[n] = int(node_lst[adj[n][0]]) - int(node_lst[adj[n][1]])
        elif node_lst[n] == '*':
            node_lst[n] = int(node_lst[adj[n][0]]) * int(node_lst[adj[n][1]])
        elif node_lst[n] == '/':
            node_lst[n] = int(node_lst[adj[n][0]]) // int(node_lst[adj[n][1]])


for t in range(1, 11):
    # 1 <= N <= 1000
    N = int(input())
    adj = [[0, 0] for _ in range(N + 1)]
    node_lst = [0] * (N + 1)

    for _ in range(N):
        try:
            n, *etc = list(map(str, input().split()))
            node_lst[int(n)] = etc[0]   # 노드 번호의 값 받는다.
            # 자식 노드 adj
            adj[int(n)][0] = int(etc[1])
            adj[int(n)][1] = int(etc[2])
        except:
            continue

    postorder(1)
    print(f'#{t} {node_lst[1]}')
