import sys

sys.stdin = open('input.txt')


# 사칙연산 표
# 정점에 연산자 있으면 자식 1, 2 숫자를 연산한다.
# 실수 연산으로 처리한다 / > //
def sol(n):
    if node_lst[n] in operator:
        if node_lst[n] == '+':
            node_lst[n] = int(sol(2 * n)) + int(sol(2 * n + 1))
            return node_lst[n]
        elif node_lst[n] == '-':
            node_lst[n] = int(sol(2 * n)) - int(sol(2 * n + 1))
            return node_lst[n]
        elif node_lst[n] == '*':
            node_lst[n] = int(sol(2 * n)) * int(sol(2 * n + 1))
            return node_lst[n]
        elif node_lst[n] == '/':
            node_lst[n] = int(sol(2 * n)) // int(sol(2 * n + 1))
            return node_lst[n]
    else:
        return int(node_lst[n])


for t in range(1, 11):
    # 1 <= N <= 1000
    N = int(input())
    node_lst = [0] * (N + 1)

    for _ in range(N):
        n, *etc = list(map(str, input().split()))
        node_lst[int(n)] = etc[0]   # 노드 번호의 값 받는다.

    operator = ['+', '-', '*', '/']
    sol(1)
    print(f'#{t} {node_lst[1]}')
