import sys

sys.stdin = open('input.txt')

max_lst = []
def turn(n, m):
    global max_num

    if m == M:
        max_num = max(int(''.join(n)), max_num)
        return

    for i in range(num_len):
        for j in range(i+1, num_len):
            if n[i] != n[j]:
                n[i], n[j] = n[j], n[i]
                turn(n, m + 1)
                n[i], n[j] = n[j], n[i]


T = int(input())
# T = 1
for t in range(1, T + 1):
    # N 자리수 1 <= N <= 6, 교환 횟수 M번 1 <= M <= 10
    N, M = map(int, input().split())
    max_num = -1
    num = list(str(N))
    num_len = len(num)
    turn(num, 0)
    print(f'#{t} {max_num}')


