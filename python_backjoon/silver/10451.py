# import sys
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    per_lst = [[]] + temp
    visited = [0] * (N + 1)
    cnt = 0

    for i in range(1, N + 1):   # temp의 길이만큼 순회
        stack = []  # 스택
        j = 0   # j값 초기화

        # 순열 사이클이기 때문에 방문한 적 없다면 처음 도는 순열 사이클이다.
        if visited[i] == 0:
            cnt += 1
            stack.append(i)
            visited[i] = 1  # 방문 기록
            # j가 다시 처음 위치로 돌아올 때까지 방문기록을 남기며 순열 사이클을 돈다.
            while j != i:
                j = stack.pop()
                visited[j] = 1
                j = per_lst[j]
                stack.append(j)
    print(cnt)

# for t in range(T):
#     N = int(input())
#
#     temp = list(map(int, input().split()))
#     per_lst = [[]] + temp
#     case_lst = []
#
#     for i in range(1, N + 1):
#         alist = []
#         j = i
#         while j not in alist:
#             alist.append(j)
#             j = per_lst[j]
#
#         alist.sort()
#
#         if alist not in case_lst:
#             case_lst.append(alist)
#
#     print(len(case_lst))

