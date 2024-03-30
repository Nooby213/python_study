# from itertools import permutations
# a = range(1, 11)
# b = list(permutations(a, 3))
# c = list(map(lambda x: sum(x) == 10, permutations(a)))
# print(c)
from itertools import combinations

a = range(1, 11)
target_sum = 10

# 부분집합 중 합이 10인 것 찾기
c = list(filter(lambda subset: sum(subset) == target_sum, [subset for r in range(len(a) + 1) for subset in combinations(a, r)]))

print(c)
