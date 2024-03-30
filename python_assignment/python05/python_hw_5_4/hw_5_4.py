# 아래 함수를 수정하시오.
# def find_min_max(list):
#     min = list[0]
#     max = list[0]
#     for i in range(len(list)):
#         if  min<= list[i]:
#             min = min
#         else:
#             min = list[i]

#         if max >= list[i]:
#             max = max
#         else:
#             max = list[i]
#     return (min, max)

def find_min_max(arr):
    # 2개 이상의 객체를 반환하도록 하려고하면, tuple로 묶어서 반환한다.
    return min(arr), max(arr)
result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
# print(type(result))
