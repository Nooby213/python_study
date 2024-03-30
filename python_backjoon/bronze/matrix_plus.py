import sys
input = sys.stdin.readline
N, M = map(int,input().split())
matrix_1 = [list(map(int,input().split())) for _ in range(N)]
matrix_2 = [list(map(int,input().split())) for _ in range(N)]
new_matrix = []

for i in range(N):
    plus_mat = []
    for j in range(M):
        p = matrix_1[i][j] + matrix_2[i][j]
        plus_mat.append(p)
    new_matrix.append(plus_mat)

for k in range(N):
    for l in new_matrix[k]:
        print(l, end=' ')
    print()