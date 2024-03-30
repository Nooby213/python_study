import sys

sys.stdin = open('input.txt')


def enq(n):  # 최소 힙
    global last
    last += 1
    node_lst[last] = n  # 완전 이진 트리, 마지막에 새노드 추가
    c = last
    p = c // 2
    while p > 0 and node_lst[p] > node_lst[c]:  # 부모가 있을 때
        node_lst[p], node_lst[c] = node_lst[c], node_lst[p]
        # 자리 바꿔줬으면, 자식, 부모 노드도 바꾼다.
        c = p
        p //= 2



def sol(x):
    c = node_lst.index(x)  # 자기 자리
    p = c // 2  # 부모 노드
    sum_p = 0

    while p > 0:  # 부모가 있을 때까지
        sum_p += node_lst[p]
        p //= 2  # 계속 올라감
    else:
        return sum_p


T = int(input())

for t in range(1, T + 1):
    N = int(input())  # 1 <= N <= 1000000
    num_lst = list(map(int, input().split()))
    node_lst = [0] * (N + 1)  # 노드 값 저장 리스트
    last = 0

    for num in num_lst:  # 리스트 순회하면서 노드 생성
        enq(num)

    # 출력 : 마지막 노드의 조상 노드들의 합
    result = sol(node_lst[-1])
    print(f'#{t} {result}')
