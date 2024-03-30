# 3 6 9 게임
# 1 ~ N 숫자, 10 ≤ N ≤ 1,000
# 박수 -
N = int(input())
for i in range(1, N + 1):
    str_i = str(i)
    if '3' in str_i or '6' in str_i or '9' in str_i:
        for j in str_i:
            if j in '369':
                print('-', end='')
        else:
            print(' ', end='')
    else:
        print(i, end=' ')
