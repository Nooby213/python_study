import sys

input = sys.stdin.readline
# 포켓몬 개수 N, 문제 개수 M, 1 <= M <= N <= 100,000
# 2 <= ai <= 20
N, M = map(int, input().split())
pokemons = [input().rstrip() for _ in range(N)]

for i in range(M):
    find = input().rstrip()
    if find.isdecimal():
        print(pokemons[int(find) - 1])
    else:
        print(pokemons.index(find) + 1)
