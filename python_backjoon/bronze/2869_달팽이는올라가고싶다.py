# V미터 등반
# 낮에는 A 올라감, 밤에는 B 내려옴
# 며칠
# 1 ≤ B < A ≤ V ≤ 1,000,000,000
A, B, V = map(int, input().split())
day = 0
if V == A:
    day = 1
elif (V - A) % (A - B) == 0:
    day = (V - A) // (A - B) + 1
else:
    day = (V - A) // (A - B) + 2

print(day)
