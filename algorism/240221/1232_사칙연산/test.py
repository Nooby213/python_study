import sys

sys.stdin = open('input.txt')


# 사칙연산 표
# 정점에 연산자 있으면 자식 1, 2 숫자를 연산한다.
# 실수 연산으로 처리한다 / > //
def sol(n):
    if node_lst[n] not in operator:  # 잎 노드에 도달한 경우
        return int(node_lst[n])  # 이미 정수로 변환된 값 반환

    if node_lst[n] == '+':
        return int(sol(2 * n)) + int(sol(2 * n + 1))
    elif node_lst[n] == '-':
        return int(sol(2 * n)) - int(sol(2 * n + 1))
    elif node_lst[n] == '*':
        return int(sol(2 * n)) * int(sol(2 * n + 1))
    elif node_lst[n] == '/':
        return int(sol(2 * n)) // int(sol(2 * n + 1))


for t in range(1, 11):
    # 1 <= N <= 1000
    N = int(input())
    node_lst = [0] * (N + 1)

    for _ in range(N):
        n, *etc = list(map(str, input().split()))
        node_lst[int(n)] = etc[0]   # 노드 번호의 값 받는다.

    operator = ['+', '-', '*', '/']
    result = sol(1)  # 수정: 반환된 결과를 변수에 저장
    print(f'#{t} {result}')
