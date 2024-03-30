import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
sorted_X = sorted(list(set(X)))
X_dict = {sorted_X[i]: i for i in range(len(sorted_X))}
for i in X:
    print(X_dict[i], end=" ")
