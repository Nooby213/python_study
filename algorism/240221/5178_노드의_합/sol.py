import sys

sys.stdin = open('input.txt')


# 완전 이진 트리 리프 노드에 1000 이하의 자연수 저장
# 왼쪽부터 늘어나는 완전 이진 트리

# 리프 노드 제외한 노드에는 부모노드 = 자식1 + 자식2
def enq(c, num):
    p = c // 2
    while p > 0:
        node_lst[p] += num
        p //= 2


T = int(input())
for t in range(1, T + 1):
    # 노드 개수 N, 리프 노드 M, L번 노드 값 출력
    N, M, L = map(int, input().split())
    node_lst = [0] * (N + 1)  # 노드 값 저장리스트

    for i in range(M):  # 리프 노드 값들 입력
        m, num = map(int, input().split())
        node_lst[m] = num
        enq(m, num)

    # 출력 : 지정한 노드 번호에 저장된 값을 출력
    print(f'#{t} {node_lst[L]}')
