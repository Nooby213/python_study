import sys

sys.stdin = open('input.txt')


def is_contained(m):
    global cnt
    start = 0
    end = len(N_lst) - 1
    round = 0
    while start <= end:
        mid = (start + end) // 2
        if N_lst[mid] == m:
            cnt += 1
            return
        elif N_lst[mid] > m:
            end = mid - 1
            if round == 1:
                return
            round = 1

        elif N_lst[mid] < m:
            start = mid + 1
            if round == -1:
                return
            round = -1


T = int(input())
for t in range(1, T + 1):
    # N개의 수안에 M개의 수가 있는지
    # 1 <= N, M <= 500,000
    N, M = map(int, input().split())
    # 0 < ai <= 1,000,000
    N_lst = sorted(list(map(int, input().split())))
    M_lst = list(map(int, input().split()))
    cnt = 0
    for m in M_lst:
        is_contained(m)

    print(f'#{t} {cnt}')
