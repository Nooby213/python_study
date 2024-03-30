import sys

sys.stdin = open('input.txt')
for t in range(1, 11):
    T = int(input())
    # case_list = [[0] * 100 for _ in range(100)]
    sum_set = set()
    # print(case_list)

    case_list = list(list(map(int, input().split())) for _ in range(100))
    # print(case_list)

    for j in range(100): # 행의 합
        sum_set.add(sum(case_list[j]))
    # print(max(sum_set))

    for k in range(100): # 열의 합
        sum_row = 0
        for l in range(100):
            sum_row += case_list[l][k]
        sum_set.add(sum_row)
    # print(max(sum_set))

    sum_cross = 0
    sum_back_cross = 0
    for m in range(100): # 대각선
        sum_cross += case_list[m][m]   # 왼쪽부터 오른쪽
        sum_back_cross += case_list[m][99 - m]   # 오른쪽 부터 왼쪽
        sum_set.add(sum_cross)
        sum_set.add(sum_back_cross)



    print(f'#{T} {max(sum_set)}')