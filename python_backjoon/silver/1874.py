from collections import deque
N = int(input())
num_lst = deque([i for i in range(1, N+1)])
seq = [int(input()) for _ in range(N)]
stack = []
seq2 = []
result = []
len_result = 0
for i in range(N):
    if not stack:
        stack.append(num_lst.popleft())
        result.append('+')
        len_result += 1

    if stack[-1] < seq[i]:
        while seq[i] != stack[-1]:
            stack.append(num_lst.popleft())
            result.append('+')
            len_result += 1

    if stack[-1] == seq[i]:
        while stack and seq[i] == stack[-1]:
            seq2.append(stack.pop())
            result.append('-')
            len_result += 1

if seq == seq2:
    for i in range(len_result):
        print(result[i])
else:
    print('NO')