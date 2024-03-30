import sys

input = sys.stdin.readline
N, X = map(int,input().split())
num_list = list(map(int,input().split()))
for i in num_list:
    if X > i:
        print(i,end=' ')