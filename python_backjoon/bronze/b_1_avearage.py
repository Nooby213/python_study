import sys

input = sys.stdin.readline

# 최댓값 M
# (점수/최댓값) * 100

# 과목 갯수 N <= 1000
# 0 <= 성적 <= 100 중 하나는 0보다 크다.

N = int(input())
score = list(map(int, input().split()))
M = max(score)
new_score = []
for s in score:
    new_score.append((s / M) * 100)

print((sum(new_score)) / N)
