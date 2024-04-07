N, K = map(int, input().split())
strK = str(K)
cnt = 0
for i in range(N + 1):
    if i < 10:
        h = '0' + str(i)
    else:
        h = str(i)
    for j in range(60):
        if j < 10:
            m = '0' + str(j)
        else:
            m = str(j)
        for l in range(60):
            if l < 10:
                s = '0' + str(l)
            else:
                s = str(l)
            if (strK in h) or (strK in m) or (strK in s):
                cnt += 1
print(cnt)
