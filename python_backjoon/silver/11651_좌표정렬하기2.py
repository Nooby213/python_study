# y 순 > x 순 정렬
# 점의 개수 N, 1 ≤ N ≤ 100,000
N = int(input())
# xi, yi, (-100,000 ≤ xi, yi ≤ 100,000
spots = [tuple(map(int, input().split())) for _ in range(N)]
counting = [[] for _ in range(200005)]
for s in spots:
    counting[s[1] + 100000].append(s[0])
for c in range(200002):
    if len(counting[c]) >= 1:
        if len(counting[c]) == 1:
            print(counting[c][0], c - 100000)
        else:
            counting[c].sort()
            for i in range(len(counting[c])):
                print(counting[c][i], c - 100000)
