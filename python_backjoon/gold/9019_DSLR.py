import sys
input = sys.stdin.readline
# sys.stdin = open('intput.txt')
from collections import deque


def D(n):
    return (n * 2) % 10000


def S(n):
    if n - 1 < 0:
        return 9999
    return n - 1


def L(n):
    return (n % 1000) * 10 + (n // 1000)


def R(n):
    return (n % 10) * 1000 + (n // 10)


def bfs(n):
    command = ''
    q = deque([(n, command)])
    while q:
        n, command = q.popleft()
        if n == target:
            return command

        d = D(n)
        s = S(n)
        l = L(n)
        r = R(n)

        if not check[d]:
            q.append((d, command + 'D'))
            check[d] = True
        if not check[s]:
            q.append((s, command + 'S'))
            check[s] = True
        if not check[l]:
            q.append((l, command + 'L'))
            check[l] = True
        if not check[r]:
            q.append((r, command + 'R'))
            check[r] = True


T = int(input())
for t in range(T):
    num, target = map(int, input().split())
    check = [False] * 10000
    check[num] = True
    print(bfs(num))
