import sys
sys.stdin = open('input.txt')

# 1 ~ N
# 완전 이진 트리
# 루트 값, N//2번 노드 값 출력
def inorder(now):  # 중위 순회
    global cnt
    if now:
        inorder(adj[now][0])
        cnt += 1
        node_lst[now] = cnt
        inorder(adj[now][1])


T = int(input())
for t in range(1, T + 1):
    N = int(input())    # 노드 개수 N

    adj = [[0, 0]]  # 인접리스트
    node_lst = [0] * (N + 1)    # 노드 번호에 입력된 숫자

    i = 1
    while i <= N:   # 노드의 자식 노드 저장하는 adj 만듦
        if 2 * i <= N and 2 * i + 1 <= N:
            adj.append([2 * i, 2 * i + 1])
        elif 2 * i <= N:
            adj.append([2 * i, 0])
        else:
            adj.append([0, 0])
        i += 1

    cnt = 0

    inorder(1)
    print(f'#{t} {node_lst[1]} {node_lst[N//2]}')
