import sys

sys.stdin = open('input.txt')


def binary(start, end, t):
    if start > end:
        return -1  # 없으면 -1
    mid = (start + end) // 2

    if mid ** 3 == t:
        return mid  # 있으면 반환
    elif mid ** 3 < t:
        return binary(mid + 1, end, t)
    else:
        return binary(start, mid - 1, t)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    result = binary(1, int(N ** 0.5), N)  # 제곱근 >= 세제곱근
    if N == 1:
        result = 1
    print(f'#{t} {result}')
