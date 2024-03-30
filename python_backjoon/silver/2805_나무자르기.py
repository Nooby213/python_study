import sys
input = sys.stdin.readline
# 절단기 H, 0 <= H
# 나무 수 N, 1 ≤ N ≤ 1,000,000, # 필요한 나무 M, 1 ≤ M ≤ 2,000,000,000
N, M = map(int, input().split())
# 0 <= Ai < 1,000,000,000
trees = list(map(int, input().split()))

start = 0
end = max(trees)

H = 0
while start <= end:
    mid = (start + end) // 2
    cut = 0

    for tree in trees:
        if tree > mid:
            cut += tree - mid
            if cut > M:
                break

    if cut >= M:
        H = mid
        start = mid + 1
        if cut == M:
            break
    else:
        end = mid - 1

print(H)