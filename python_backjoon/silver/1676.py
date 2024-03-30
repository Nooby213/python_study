N = int(input())
a = 1
for n in range(1, N + 1):
    a *= n
b = list(str(a))

cnt = 0
for i in range(len(b)-1, -1, -1):
    if b[i] != '0':
        print(cnt)
        break
    elif b[i] == '0':
        cnt += 1
