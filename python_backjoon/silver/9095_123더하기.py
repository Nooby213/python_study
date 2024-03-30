import sys
input = sys.stdin.readline
# 1, 2, 3 으로 N을 구성하는 방법
num_lst = [0] * 12
num_lst[1] = 1
num_lst[2] = 2
num_lst[3] = 4


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if num_lst[n] == 0:
        num_lst[n] = f(n - 1) + f(n - 2) + f(n - 3)
    return num_lst[n]


T = int(input())
for t in range(T):
    # 1 <= N < 11
    N = int(input())
    print(f(N))
