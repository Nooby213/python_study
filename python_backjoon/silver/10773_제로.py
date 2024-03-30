import sys
input = sys.stdin.readline
# 잘못되면 0, 2^31-1
# 1 ≤ K ≤ 100,000
K = int(input())
stack = []
for i in range(K):
    call = int(input())
    if call:
        stack.append(call)
    elif stack and call == 0:
        stack.pop()
print(sum(stack))