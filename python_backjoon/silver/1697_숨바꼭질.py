from collections import deque


def find():
    visited = [0] * 100002
    q = deque([N])
    while q:
        now = q.popleft()
        if now == K:
            print(visited[now])

        for next in (now - 1, now + 1, now * 2):
            if 0 <= next <= 100001 and visited[next] == 0:
                visited[next] = visited[now] + 1
                q.append(next)


# 수빈 N, 0 ≤ N ≤ 100,000
# 동생 K, 0 ≤ K ≤ 100,000
# 걸으면 +1 / -1, 순간이동 2*
N, K = map(int, input().split())

# 같은 위치라면
if N == K:
    print(0)

# 0에서 동생이 수빈이보다 멀리 있을 때
elif N < K:
    find()

# 0에서 동생이 수빈이보다 가까이 있을 때
elif N > K:
    print(N - K)
