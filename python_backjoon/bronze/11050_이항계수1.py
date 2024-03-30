# 1 <= N <= 10, 0 <= K <= N
N, K = map(int, input().split())
# 메모이제이션
fact_lst = [0] * (N + 1)


def factorial(i):
    if i == 0 or i == 1:
        return 1

    if fact_lst[i]:
        return fact_lst[i]

    fact_lst[i] = i * factorial(i - 1)
    return fact_lst[i]

def bino_coef(n, k):
    return int(factorial(n) / factorial(n - k) / factorial(k))


print(bino_coef(N, K))
