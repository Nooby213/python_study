import sys

sys.stdin = open('input.txt')
from collections import deque

#           위       우상     우      우하    하       좌하      좌       좌상
delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def dfs(i, j):
    global N
    # score = [0 * (N + 1) for _ in range(N)]
    board[i][j] = -1
    if board[i][j] == 'o' and score[i][j] == 0:
        score[i][j] += 1
    if score[i][j] == 5:
        return 'YES'

    for k in range(8):
        ni = i + delta[k][0]
        nj = j + delta[k][1]

        if ni >= 0 and ni < N and nj >= 0 and nj < N and board[ni][nj] != -1:
            if board[ni][nj] == 'o' and score[ni][nj] == 0:
                score[ni][nj] = score[i][j] + 1
            dfs(ni, nj)

    return 'NO'

# def bfs():
#     global N
#     score = [[0] * N for _ in range(N)]
#     q = deque([(0, 0)])
#
#     if board[0][0] == 'o':
#         score[0][0] += 1
#
#     while q:
#         i, j = q.popleft()
#         board[i][j] = -1
#         for k in range(8):
#             ni = i + delta[k][0]
#             nj = j + delta[k][1]
#             if ni >= 0 and ni < N and nj >= 0 and nj < N and board[ni][nj] != -1:
#                 q.append((ni, nj))
#                 if board[ni][nj] == 'o':
#                     score[ni][nj] = score[i][j] + 1

    return score

T = int(input())

for t in range(1, T + 1):
    N = int(input())  # N * N 바둑판
    board = []
    score = [[0] * N for _ in range(N)]
    for i in range(N):
        board.append(list(input()))
    result = dfs(0, 0)
    # result = bfs()
    # for i in result:
    #     if 5 in i:
    #         print(f'#{t} YES')
    #         break
    # if
    # else:
    #     print(f'#{t} NO')
    print(result)
    # for i in range(N):
    #     if 5 in result[i]:
    #         print(f'#{t} YES')
    #         break
    # else:
    #     print(f'#{t} NO')