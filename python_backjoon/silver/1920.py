N = int(input())
N_lst = list(map(int, input().split()))
N_lst.sort()  # 숫자 크기 순으로 정렬
M = int(input())
M_lst = list(map(int, input().split()))


def binary(alist, start, end, target):  # 이진탐색
    if start >= end and alist[end] == target:  # 중간 값 하나만 남을때
        return print(1)
    elif start >= end and alist[end] != target:
        return print(0)

    middle = (start + end) // 2  # 가운데 인덱스 기준
    if alist[middle] == target:
        return print(1)

    elif alist[middle] > target:
        binary(alist, start, middle - 1, target)

    elif alist[middle] < target:
        binary(alist, middle + 1, end, target)


for m in range(M):
    binary(N_lst, 0, N - 1, M_lst[m])

# for m in range(M):
#     if M_lst[m] in N_lst:
#         print(1)
#     else:
#         print(0)
