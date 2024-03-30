import sys

input = sys.stdin.readline
from collections import deque


# R (뒤집기 함수), 순서를 뒤집는다.
# D (버리기 함수), 첫 번째 수를 버린다, 빈 배열에 사용시 에러.
def D():
    if R_cnt % 2:
        num_lst.pop()
    else:
        num_lst.popleft()


T = int(input())
for t in range(T):
    # 1 <= P <= 100,000
    P = input().rstrip()
    # 배열에 들어있는 수의 개수 N, 0 ≤ N ≤ 100,000
    N = int(input())
    # 1 ≤ xi ≤ 100
    R_cnt = 0
    num_lst = deque()
    num = ''

    for i in input():
        if i.isdecimal():
            num += i
        elif (i == ',' or i == ']') and num != '':
            num_lst.append(int(num))
            num = ''

    for f in P:
        if f == 'R':
            R_cnt += 1
        if f == 'D':
            if num_lst:
                D()

            else:
                print('error')
                break

    else:
        if R_cnt % 2 and num_lst:
            print('[', end='')
            print(*list(num_lst)[::-1], sep=',', end='')
            print(']')

        else:
            print('[', end='')
            print(*list(num_lst), sep=',', end='')
            print(']')
