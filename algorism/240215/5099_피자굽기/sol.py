import sys

sys.stdin = open('input.txt')
from collections import deque

# N개의 피자 동시에 구움
# 치즈 양은 피자마다 다름
# 1~M번까지 M개의 패지를 순서대로 화덕에 넣음 / 꺼내는 시간 다를 수 있다.
# 1번 위치 넣거나 뺄 수 있다. 입출구 하나
# 한 바퀴 돌면 치즈는 c//2, 0이 되면 꺼낸다.

T = int(input())
for t in range(1, T + 1):
    # N개의 피자 구움, 피자 M개
    # 3 <= N <= 20
    # N <= M <= 100
    # 1 <= Ci <= 20
    N, M = map(int, input().split())
    cheese = deque(list(map(int, input().split())))  # 치즈양
    pan = deque([0] * N)  # 화덕
    stack = deque([0] * N) # 번호표

    # print(pizza)
    # print(cheese)
    # print(pan)
    num = 1
    while len(pan) != 1:  # 피자 다 구울 때까지
        pan[0] //= 2  # 치즈 녹임
        if pan[0] == 0:  # 치즈 다 녹았으면
            pan.popleft()
            if cheese:  # 피자 구울거 더 있으면
                pan.append(cheese.popleft())
                stack.popleft()
                stack.append(num)
            else:
                stack.popleft()
            # print(stack)
            # print(f'b{pan}')
            num += 1
        else:  # 화덕 돌린다
            pan.append(pan.popleft())
            # print(f'r{pan}')
            stack.append(stack.popleft())

    else:
        # print(stack)
        # print(pan)
        print(f'#{t} {stack[0]}')

