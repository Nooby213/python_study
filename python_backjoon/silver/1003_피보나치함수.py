fibo_lst = [[0] * 2 for _ in range(41)]
fibo_lst[0][0], fibo_lst[0][1] = 1, 0
fibo_lst[1][0], fibo_lst[1][1] = 0, 1


def fibonacci(n):
    if n == 0:
        return fibo_lst[0][0], fibo_lst[0][1]
    elif n == 1:
        return fibo_lst[1][0], fibo_lst[1][1]

    elif fibo_lst[n][0] != 0 and fibo_lst[n][1] != 0:
        return fibo_lst[n][0], fibo_lst[n][1]
    else:
        a, b = fibonacci(n - 1)
        c, d = fibonacci(n - 2)
        fibo_lst[n][0] = a + c
        fibo_lst[n][1] = b + d
        return fibo_lst[n][0], fibo_lst[n][1]


T = int(input())
for t in range(T):
    N = int(input())
    fibonacci(N)
    print(fibo_lst[N][0], fibo_lst[N][1])
