import sys

sys.stdin = open('input.txt')

# A : 0 > B : 99
# 일방 통행
def dfs(v): # 99 도착하면 1로 표시
    global fnd
    if v == 99:
        fnd = 1
        return
    for i in road[v]:
        dfs(i)

for t in range(1, 11):

    road = [[] for _ in range(100)]  # 도로
    ts, E = map(int, input().split())  # ts 테스트케이스, E 도로 갯수
    adj = list(map(int, input().split()))
    # print(adj)

    for i in range(E): # 도로 연결
        road[adj[2 * i]].append(adj[2 * i + 1])
    # print(road)

    fnd = 0
    dfs(0)
    print(f'#{ts} {fnd}')
