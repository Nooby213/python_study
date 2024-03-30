import sys
input = sys.stdin.readline
num_set = {i for i in range(1,31)}
check_set = set()
for _ in range(28):
    j = int(input())
    if j in num_set:
        check_set.add(j)
result = list(num_set - check_set)
result.sort()
for k in result:
    print(k)