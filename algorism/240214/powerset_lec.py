def f(i, k, t):
    global cnt
    if i == k:
        ss = 0
        for j in range(k):
            if bit[j]:
                ss += A[j]
                # cnt += 1
            # if ss > t:
            #     # cnt += 1
            #     break
        if ss == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i + 1, k, t)
        # bit[i] = 1
        # f(i + 1, k)
        # bit[i] = 0
        # f(i + 1, k)

cnt = 0
N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N
f(0, N, 10)
print(cnt)