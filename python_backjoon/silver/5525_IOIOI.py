def match():
    i = 0
    cnt = 0
    char = 'I'
    while i < M:
        while i < M and char == S[i]:
            cnt += 1
            i += 1
            if char == 'I':
                char = 'O'
            else:
                char = 'I'
        else:
            for k in range(0, cnt - N, 2):
                can[i - 1 - k] = cnt - k
            cnt = 0
            char = 'I'
        if i < M and char != S[i]:
            i += 1

# 1 ≤ N ≤ 1,000,000
N = int(input())
# 2N+1 ≤ M ≤ 1,000,000
M = int(input())
# 문자열
S = input()

word = 'IO' * N + 'I'
len_word = 2 * N + 1
can = [0] * M
match_cnt = 0

match()
for i in can:
    if i >= 2 * N + 1:
        match_cnt += 1

print(match_cnt)