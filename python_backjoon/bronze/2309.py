# 7 난쟁이 합이 100
from itertools import combinations
# 함수만들어서 푸는법
def find_dwarf(i, temp_sum, alist):
    # 키의 합이 100이 넘거나 난쟁이 7명 넘어가면 되돌아감
    if temp_sum > 100 or i == 7:
        return

    for j in range(9):
        if visited[j] == 0:
            visited[j] = 1
            # 난쟁이가 7명 되고 키의 합이 100이 되었으면 출력 후 함수 정지
            if i + 1 == 7 and temp_sum + height[j] == 100:
                temp_lst = alist + [height[j]]
                temp_lst.sort()
                for a in temp_lst:
                    print(a)
                break
            find_dwarf(i + 1, temp_sum + height[j], alist + [height[j]])
            visited[j] = 0


height = [int(input()) for _ in range(9)]   # 9 명 난쟁이

visited = [0] * 9   # 방문표시

find_dwarf(0, 0, [])

# itertools 쓴 풀이법

# height.sort()

# comb = list(combinations(height, 7))
#
# for com in comb:
#     if sum(com) == 100:
#         for c in com:
#             print(c)
#         break