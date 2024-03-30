import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split()) # N 명, M 초에 K 개 만듦
    wait = list(map(int, input().split()))
    wait.sort()
    latest = wait[-1]
    # wait = deque(list(map(int, input().split())))
    wait = deque(wait)
    bread = 0
    # print(wait)

    for n in range(latest + 1):  # 제일 늦게 온 손님 올 때까지 굽는다
        if n != 0 and n % M == 0:   # 시간마다 붕어빵나옴
            bread += K
            # print(bread)
        if n in wait:   # 손님이 시간에 있으면
            while n in wait and bread >= 0: # 그 시간 손님 다 오거나 빵 없을때까지 나눠줌
                bread -= 1
                wait.popleft()
        if bread < 0:   # 빵 없으면 영업종료
            print(f'#{t} Impossible')
            break
    else:   # 다 나눠줬으면 성공
        print(f'#{t} Possible')
