import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    # N 개의 숫자로 구성된 숫자열 Ai
    # M 개의 숫자로 구성된 숫자열 Bi
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    max_sum = 0
    if N == M:
        for i in range(N):
            max_sum += Ai[i] * Bi[i]
    elif N < M:
        for i in range(M - N + 1):
            temp_sum = 0
            for j in range(N):
                if i == 0:
                    max_sum += Ai[j] * Bi[j + i]
                else:
                    temp_sum += Ai[j] * Bi[j + i]
            if temp_sum > max_sum:
                max_sum = temp_sum

    elif N > M:
        for i in range(N - M + 1):
            temp_sum = 0
            for j in range(M):
                if i == 0:
                    max_sum += Ai[j + i] * Bi[j]
                else:
                    temp_sum += Ai[j + i] * Bi[j]
            if temp_sum > max_sum:
                max_sum = temp_sum

    print(f'#{t} {max_sum}')
