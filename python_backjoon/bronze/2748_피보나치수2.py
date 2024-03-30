fibo_lst = [0] * 91


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if fibo_lst[n]:
        return fibo_lst[n]
    else:
        fibo_lst[n] = fibo(n - 1) + fibo(n - 2)
        return fibo_lst[n]

# 1 <= N <= 90
N = int(input())
print(fibo(N))
print(fibo_lst)
