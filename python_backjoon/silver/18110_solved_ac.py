# 사사오입 아니기 때문에 함수를 다시 만들거나 0.5 int한 후 값 결정
import sys

input = sys.stdin.readline  # 30 % 절사평균, 반올림


# 의견 수 n, 0 ≤ n ≤ 3 × 10^5
def round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)


n = int(input())
if n == 0:
    print(0)
else:
    opinions = sorted(list(int(input()) for _ in range(n)))
    op_average = round(0.15 * n)
    opav_lst = opinions[op_average:n - op_average]
    average = round((sum(opav_lst) / len(opav_lst)))
    print(average)
