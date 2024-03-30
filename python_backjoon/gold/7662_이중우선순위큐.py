from collections import deque

def to_put(n):
    start = 0
    end = len(q)

    while start <= end:
        mid = (start + end) // 2

        if q[mid] == n:
            q.insert(mid, n)
            break

        if q[mid] > n:
            end = mid - 1

        if q[mid] < n:
            start = mid + 1

        if start >= end:
            q.insert(mid, n)

T = int(input())
for _ in range(T):
    # 연산할 숫자 갯수, k ≤ 1,000,000
    k = int(input())
    # I는 삽입, D는 삭제 : 1 은 최대, -1 최소, 큐가 비어있으면 무시
    # 비어있으면 EMPTY, 최대, 최소 출력
    q = deque()
    for i in range(k):
        command, num = input().split()
        num = int(num)
        if command == 'I':
            if q:
                if num <= q[0]:
                    q.appendleft(num)
                elif num >= q[-1]:
                    q.append(num)
                else:
                    to_put(num)
            else:
                q.append(num)

        if command == 'D':
            if q:
                if num == -1:
                    q.popleft()
                else:
                    q.pop()
    if q:
        print(max(q), min(q))
    else:
        print('EMPTY')