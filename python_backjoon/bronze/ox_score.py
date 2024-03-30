N = int(input())
check_list = [input().upper() for _ in range(N)]
# print(check_list)
before = ''
for check in check_list:
    score = 0
    for c in range(len(check)):
        # print((c+1),len(check))
        if check[c] == 'O' and (c + 1) == len(check):
            before += check[c]
            for i in range(len(before)):
                score += (i + 1)
            before = ''
        elif check[c] == 'O':
            before += check[c]
            # print(before)
        elif check[c] == 'X':
            for i in range(len(before)):
                score += (i + 1)
            before = ''
    print(score)

'''
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
'''