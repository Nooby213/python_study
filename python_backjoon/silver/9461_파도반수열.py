pado_lst = [0] * 100
pado_lst[0] = 1
pado_lst[1] = 1
pado_lst[2] = 1
pado_lst[3] = 2
pado_lst[4] = 2

def pado(n):
    if n < 5:
        return pado_lst[n]

    if pado_lst[n]:
        return pado_lst[n]

    pado_lst[n] = pado(n - 1) + pado(n - 5)

    return pado_lst[n]

T = int(input())
for _ in range(T):
    # 1 ≤ N ≤ 100
    N = int(input())
    print(pado(N-1))