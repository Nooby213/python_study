import sys
sys.stdin = open('input.txt')

# N * N 배열 3<= N <=10
# 가로 세로 하나씩

# 첫 째줄이 0, 1, 2 돌면서 두번 째줄 세번째줄
T = int(input())

def min_sum(alist, i, lst_sum):
    global mini
    lst_sum += alist[i][j]

    # if visited[i][j] == False:  # 이용한 행이나 열이 아니라면

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    mini = 100 # 10보다 작은 자연수가 10*10 이 최대인 2차원 배열에 주어지기 때문에
    visited = [[False] * N for _ in range(N)] # 방문기록
    # print(visited)
