import sys

sys.stdin = open('input.txt')


# 연속으로 당근 크기가 커진 경우 그 개수 최대 출력 값

def connected_carrot(n):
    temp_num = 1
    for j in range(n + 1, N):
        if carrots[j] <= carrots[j - 1]:
            break
        elif carrots[j] > carrots[j - 1]:
            temp_num += 1
    return temp_num


T = int(input())

for t in range(1, T + 1):
    # N개 수확, 5 <= N <= 1000
    N = int(input())
    # 당근 크기 C, 1 <= C <= 10
    carrots = list(map(int, input().split()))
    # 최소 길이는 1
    result = 1
    for i in range(N):
        temp_result = connected_carrot(i)
        if temp_result > result:
            result = temp_result

    print(f'#{t} {result}')
