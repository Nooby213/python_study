import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    # 의상수 N, 0 ≤ n ≤ 30
    N = int(input())
    clothes = {}
    cnt = 1
    for _ in range(N):
        cloth, item = input().split()
        if clothes.get(item) != None:
            clothes[item] += 1
        else:
            clothes[item] = 1
    for k, v in clothes.items():
        cnt *= (v + 1)

    print(cnt - 1)
