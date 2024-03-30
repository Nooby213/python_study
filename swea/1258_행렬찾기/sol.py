import sys

sys.stdin = open('input.txt')
di = [1, 0]
dj = [0, 1]


def dfs(i, j, case_num):
    global max_i
    global max_j
    max_i = max(i, max_i)
    max_j = max(j, max_j)

    if cases[i][j] != 0:
        cases[i][j] = 0

    for k in range(2):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and cases[ni][nj] != 0:
            dfs(ni, nj, case_num)


T = int(input())

for t in range(1, T + 1):
    # N * N 1 <= N <= 100
    N = int(input())
    # 그룹 1. n <= 10 이고 sub matrix의 개수 5개 이하
    # 그룹 2. n <= 40 이고 5 < sub matrix <= 10
    # 그룹 3. 40 < n <=80 이고 5 < sub matrix <= 10
    # 그룹 4. 40 < n <=80 이고 10 < sub matrix <= 15
    # 그룹 5. 80 < n<=100 이고 15 < sub matrix <= 20
    # 빈 통 0, 화학 물질 1 ~ 9
    cases = [list(map(int, input().split())) for _ in range(N)]
    matrix = [[] for _ in range(20)]
    case_num = 0
    for i in range(N):
        for j in range(N):
            max_i = 0
            max_j = 0
            if cases[i][j] != 0:
                matrix[case_num].append(i + 1)
                matrix[case_num].append(j + 1)
                dfs(i, j, case_num)
                matrix[case_num][0] = max_i + 1 - i
                matrix[case_num][1] = max_j + 1 - j
                matrix[case_num].append(matrix[case_num][0] * matrix[case_num][1])
                case_num += 1

    for i in range(19, -1, -1):
        if len(matrix[i]) == 0:
            matrix.pop()
    matrix.sort(key=lambda x: (x[2], x[0]))

    print(f'#{t} {len(matrix)}', end=' ')
    for mat in matrix:
        print(f'{mat[0]} {mat[1]}', end=' ')
    print()
