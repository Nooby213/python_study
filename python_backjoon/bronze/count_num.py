import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int,input().split()))
count_num = int(input())
result = 0

for i in num_list:
    if i == count_num:
        result += 1

print(result)
