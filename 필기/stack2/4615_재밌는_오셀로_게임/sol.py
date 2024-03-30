import sys
sys.stdin = open('input.txt')

def dfs_b(i, j):
    for

def dfs_w(i, j):

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())    # N * N 오셀로판, M 번 게임
    borad = [[0] * N for _ in range(N)]
    # print(borad)

    turn = [list(map(int, input().split())) for _ in range(M)]
    print(turn)
    for i in range(N):
        borad[turn[i][0]][turn[i][1]] = turn[i][2]

        if turn[i][2] == 1: # 검은색 차례일 때
            dfs_b(i, j)

        elif turn[i][2] == 2:   # 흰색 차례일 때
            dfs_w(i, j)