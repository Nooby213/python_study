import sys
input = sys.stdin.readline
from heapq import heappush, heappop

T = int(input())
for _ in range(T):
    # k 번 연산, k ≤ 1,000,000
    k = int(input())
    # I는 삽입, D는 삭제 : 1 은 최대, -1 최소, 큐가 비어있으면 무시
    # 비어있으면 EMPTY, 최대, 최소 출력
    min_q = []
    max_q = []
    check = [1] * k
    for i in range(k):
        command, num = input().split()
        num = int(num)
        if command == 'I':
            heappush(min_q, (num, i))
            heappush(max_q, (-num, i))

        if command == 'D':
            if num == -1 and min_q:
                check[heappop(min_q)[1]] = 0

            elif num == 1 and max_q:
                check[heappop(max_q)[1]] = 0

            while min_q and check[min_q[0][1]] == 0:
                heappop(min_q)
            while max_q and check[max_q[0][1]] == 0:
                heappop(max_q)

    if min_q and max_q:
        print(-heappop(max_q)[0], heappop(min_q)[0])
    else:
        print('EMPTY')
