'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def solution(k):  # 할 일 : 노드 번호 출력
    print(k, end=' ')


def preorder(now):  # 조사 시작 노드번호부터 조사를 시작한다.
    # 노드 번호 0은 없음
    # 따라서, 노드 번호가 0이 아닌 경우만 조사할 수 있어야함
    if now != 0:
        # 전위 순회는, 조사 시작 노드 번호에 대해서 할 일을 수행
        solution(now)  # 현재 노드 번호에 대해 할 일 수행
        # 왼쪽 자식 순회
        preorder(tree[now][0])
        # 오른쪽 자식 순회
        preorder(tree[now][1])


def inorder(now):
    if now != 0:
        inorder(tree[now][0])
        solution(now)
        inorder(tree[now][1])


def postorder(now):
    if now != 0:
        postorder(tree[now][0])
        postorder(tree[now][1])
        solution(now)


V = int(input())
edge = list(map(int, input().split()))
E = len(edge)  # 간선 정보 길이
# print(edge)

# 인접 리스트
# adj = [[] for _ in range(V + 1)]    # 0번 노드는 없다.
# print(adj)

# for idx in range(E//2):
#     adj[edge[idx * 2]].append(edge[idx * 2 + 1])
# print(adj)

# tree[현재 노드 번호][0] > 현재 노드 번호의 왼쪽 자식 노드 번호
tree = [[0, 0] for _ in range(V + 1)]

for idx in range(E // 2):
    # 특정 위치에 값을 할당 하는 것.
    if tree[edge[idx * 2]][0] == 0:
        tree[edge[idx * 2]][0] = edge[idx * 2 + 1]
    else:
        tree[edge[idx * 2]][1] = edge[idx * 2 + 1]

# print(tree)

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()

'''
N = int(input())    # 1번 부터 N번까지인 정점
E = N - 1
arr = list(map(int, input().split()))
left = [0] * (N + 1)
right = [0] * (N + 1)
par = [0] * (N + 1)

for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]

    if left[p] == 0:
        left[p] = c

    else:
        right[p] = c

    par[c] = p

c = N
while par[c] != 0:
    c = par[c]

root = c
print(root)
'''
