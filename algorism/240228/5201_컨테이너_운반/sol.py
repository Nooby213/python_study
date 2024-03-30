import sys

sys.stdin = open('input.txt')

# 트럭당 컨테이너 한 개, 적재량 초과 x, 편도 운행

# 1 <= T <= 50
T = int(input())

for t in range(1, T + 1):
    # 1 <= N, M <= 100
    N, M = map(int, input().split())
    # N개의 컨테이너, 1 <= wi <= 50
    containers = list(map(int, input().split()))
    # M대의 트럭, 1 <= ti <= 50
    trucks = list(map(int, input().split()))
    # 옮긴 화물 무게
    weight = 0
    for truck in trucks:
        can_move = 0
        for container in containers:
            if truck >= container > can_move:
                can_move = container
        # 옮긴 컨테이너 제거
        if can_move != 0:
            weight += can_move
            containers.remove(can_move)
    print(f'#{t} {weight}')
