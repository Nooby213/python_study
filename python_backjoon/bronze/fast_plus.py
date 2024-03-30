import sys

input = sys.stdin.readline
N = int(input())
num_list = [list(map(int,input().split())) for _ in range(N)]
for i in num_list:
    print(i[0] + i[1])