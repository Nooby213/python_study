import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))

    loc = 0 # 현재 위치
    count = 0 # 충전 횟수

    while loc + K < N:
    # 현재 위치 + 최대 이동거리가 종점에 도착하지 않을 동안 반복
        for step in range(K, 0, -1):
        # 최대한 멀리있는 정류장에서 충전하는 것이 최소 충전 횟수
            if loc + step in stations:
                loc += step
                count += 1
                break
        else:
        # 종점에 도착8할 수 없는 경우 = step이 0이 되었는데 충전소가 나타나지 않은 경우
            count = 0
            break

    print(f'#{test_case} {count}')