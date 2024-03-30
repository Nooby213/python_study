'''
10 6 12 8 9 4 1 3
'''
code = list(map(int, input().split()))
# print(code)
a = 1
while code[0] - a > 0:
    code[0] -= a
    code.append(code.pop(0))
    # print(code)
    a = 1 + ((a) % 5)
else:
    if code[-1] != 0 and code[0] - a <= 0:
        code[0] = 0
        code.append(code.pop(0))
    print(f'#{1}',end=' ')
    print(*code)
