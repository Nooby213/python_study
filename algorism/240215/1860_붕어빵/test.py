import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())  # N 명, M 초에 K 개 만듦
    wait = list(map(int, input().split()))
    wait.sort()
    bread = 0
    idx = 0  # 대기 중인 손님을 가리키는 인덱스
    possible = True  # 영업 가능 여부

    for time in range(wait[-1] + 1):  # 최대 도착 시간까지 시뮬레이션
        if time != 0 and time % M == 0:  # 시간마다 붕어빵나옴
            bread += K

        while idx < N and wait[idx] == time:  # 대기 중인 손님이 도착한 경우
            if bread == 0:  # 붕어빵이 없으면 영업 불가능
                possible = False
                break
            bread -= 1
            idx += 1

        if not possible:  # 영업 불가능하면 루프 종료
            break

    if possible:
        print(f'#{t} Possible')
    else:
        print(f'#{t} Impossible')
