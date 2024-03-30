# 나이와 이름이 가입한 순서대로
# 나이순으로 > 먼저 가입한 사람
# 1 ≤ N ≤ 100,000
N = int(input())
members = []
for i in range(N):
    age, name = map(str, input().split())
    members.append([i, int(age), name])

members.sort(key=lambda x: (x[1], x[0]))
for i in members:
    print(i[1], i[2])
