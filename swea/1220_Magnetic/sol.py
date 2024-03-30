import sys

sys.stdin = open('input.txt')


for t in range(1, 11):
    N = int(input())
    # N 1, S 2, 위가 N, 아래가 S
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        stack = []
        for j in range(N):
            if board[j][i] == 1:
                stack.append(board[j][i])
            elif board[j][i] == 2:
                if stack and stack[-1] == 1:
                    result += 1
                stack.append(board[j][i])

    print(f'#{t} {result}')
