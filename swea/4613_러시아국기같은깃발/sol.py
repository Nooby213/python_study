import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    # N * M, 3 ≤ N, M ≤ 50
    N, M = map(int, input().split())
    # W R B 연속 3줄
    flags = [list(input()) for _ in range(N)]
    cnt = 0
    # 첫 줄과 마지막 줄은 각각 흰색과 빨강색
    for i in 0, N - 1:
        for j in range(M):
            if i == 0 and flags[i][j] == 'W':
                cnt += 1
            if i == N - 1 and flags[i][j] == 'R':
                cnt += 1
    flag_lst = []

    for i in range(1, N - 1):
        # 나머지 깃발 색
        flag_cnt = {'W': 0, 'R': 0, 'B': 0}
        for j in range(M):
            flag_cnt[flags[i][j]] += 1
        flag_lst.append(flag_cnt)

    print(flag_lst)
    print(f'#{t} {N * M - cnt}')
