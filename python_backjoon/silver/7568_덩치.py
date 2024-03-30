# x kg, y cm , (x, y)
# 사람 수 N, 2 ≤ N ≤ 50
N = int(input())
# 10 ≤ x, y ≤ 200
students = [tuple(map(int, input().split())) for _ in range(N)]
for i in range(N):
    rate = 1
    for j in range(N):
        x, y = students[i]
        p, q = students[j]
        if x < p and y < q:
            rate += 1
    else:
        print(rate, end=' ')