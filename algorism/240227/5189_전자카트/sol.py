import sys

sys.stdin = open('input.txt')


def find_mini(i, temp_sum):
    global mini
    if temp_sum > mini:
        return

    if all(visited):
        temp_sum += office[i][0]
        if temp_sum < mini:
            mini = temp_sum
        return

    if i == N - 1:
        temp_sum += office[i][0]
        if temp_sum < mini:
            mini = temp_sum
        return



    for j in range(1, N):
        if visited[j] == 0 and office[i][j] != 0:
            visited[j] = 1
            find_mini(j, temp_sum + office[i][j])
            visited[j] = 0


T = int(input())
for t in range(1, T + 1):
    # N * N, 3 <= N <= 10
    N = int(input())
    # 1 <= office[i][j] <= 100
    office = [list(map(int, input().split())) for _ in range(N)]
    mini = 200 * N
    visited = [0] * N
    visited[0] = 1
    find_mini(0, 0)
    print(f'#{t} {mini}')
