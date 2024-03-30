N = int(input())    # 자연수 N
i = 9 * len(str(N))

while i > 0:
    if N - i > 0:
        M = str(N - i)

        new_N = int(M)

        for m in M:
            new_N += int(m)

        if new_N == N:
            print(int(M))
            break
        i -= 1
    else:
        i -= 1
else:
    print(0)

