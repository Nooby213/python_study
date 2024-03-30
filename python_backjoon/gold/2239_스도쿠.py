import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy
def square(i, j):
    square_set = set()
    for k in range(i, i + 3):
        for m in range(j, j + 3):
            if sdoku[k][m]:
                square_set.add(sdoku[k][m])
    return square_set

def row(i, j):
    row_set = set()
    for k in range(9):
        if sdoku[i][k]:
            row_set.add(sdoku[i][k])

def can(i, j):
    num_set = {i for i in range(1, 10)} - square(i, j) - row(i, j)
    used = [1] * 10
    for k in num_set:
        used[k] = 0

    for k in range(i, i + 3):
        for m in range(j, j + 3):
            if sdoku[k][m] == 0:
                sdoku[k][m] = used

def solve(i, j):
    if i == 8 and j == 8:
        for row in sol_sdoku:
            print(''.join(row))
            return


sdoku = [[int(i) for i in input().rstrip()] for _ in range(9)]
sol_sdoku = deepcopy(sdoku)
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        can(i, j)

print(sdoku)