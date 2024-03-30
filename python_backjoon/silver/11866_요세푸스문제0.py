# 1 ~ N 원으로 앉아있다.
# 순서대로 K번째 사람 제거
# 1 ≤ K ≤ N ≤ 1,000
from collections import deque


def rotate():
    for i in range(1, K + 1):
        if i % K:
            num_lst.append(num_lst.popleft())
        else:
            return num_lst.popleft()


N, K = map(int, input().split())
num_lst = deque([i for i in range(1, N + 1)])
before = 0
print('<', end='')
for i in range(N):
    num = rotate()
    if i == N - 1:
        print(num,end='')
    else:
        print(f'{num},', end=' ')

print('>')
