N = int(input())  # 컴퓨터 개수
M = int(input())  # 간선 수

cnt = 0
def dfs(start):
    global cnt
    visited[start] = True
    cnt += 1
    # print(start,cnt)
    for i in com_con[start]:
        if not visited[i]:
            dfs(i)


com_lst = [list(map(int, input().split())) for _ in range(M)]   # 이어지는 컴퓨터리스트
visited = [False for _ in range(N + 1)] # 방문 기록
com_con = [[] for _ in range(N + 1)]    # 각 컴퓨터에 연결된 컴퓨터 리스트

for c, d in com_lst:
    com_con[c].append(d)
    com_con[d].append(c)
# print(com_con)
# print(com_lst)
# print(visited)
dfs(1)
# print(visited)
print(cnt - 1)