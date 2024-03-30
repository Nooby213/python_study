N = int(input())
for i in range(N):
    stack = []
    for j in input():
        try:
            if j == '(':
                stack.append(j)
            else:
                stack.pop()
        except:
            print('NO')
            break
    else:
        if stack:
            print('NO')
        else:
            print('YES')