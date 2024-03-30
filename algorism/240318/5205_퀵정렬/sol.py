import sys

sys.stdin = open('input.txt')


def quick_sort(alist):
    if len(alist) == 0:
        return []
    if len(alist) == 1:
        return alist

    pivot = alist[0]
    start = 1
    end = len(alist)
    smaller = []
    same = []
    bigger = []
    for i in alist:
        if i < pivot:
            smaller.append(i)
        elif i > pivot:
            bigger.append(i)
        else:
            same.append(i)

    return quick_sort(smaller) + same + quick_sort(bigger)


T = int(input())

for t in range(1, T + 1):
    # 정수 갯수 N, 5 <= N <= 1,000,000
    N = int(input())
    # 0 <= ai <= 1,000,000
    lst = list(map(int, input().split()))

    print(f'#{t} {quick_sort(lst)[N // 2]}')
