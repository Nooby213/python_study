# 아래 함수를 수정하시오.
def remove_duplicates_to_set(data):
    set_list = set(data)
    return set_list


# 가정 : arr에 1~9 까지의 정수만 요소로 삽입된다면, 
# def remove_duplicates_to_set(data):
#     # 기본 dict
#     # dict_comprehension
#     # count_dict = {1 : 0, 2 : 0, 3 : 0, 4 : 0}
#     count_dict = {i : 0 for i in range(1, 10)}
#     # 중복이 없다.
#     # 배열의 모든 요소를 순회한다.
#     # 이 때, 순회 대상이, 이전에 한 번도 나온적이 없다.
#         # 요소를 중심으로 해당 요소가 몇 번 나왔는지 셀 수 있어야함.
#         # 1이 1번 나왔으면 1 = 1
#         # 2가 3번 나왔으면 2 = 3
#         # dict = {1 : 1, 2 : 3}
#     for num in data:
#         count_dict[num] += 1 
#     result = [key for key, item in count_dict.items() if item >= 1]
#     return set(result)

# def remove_duplicates_to_set(data):
#     count_list = [0 for i in range(11)]
#     for index in data:
#         count_list[index] += 1
#     result = [num for num in range(len(count_list)) if count_list[num] >= 1]
#     return result

# def remove_duplicates_to_set(data):
#     # 최종 결과물
#     result = set()
#     duplicate_check_dict = {}
#     for num in data:
#         # 해당하는 키가 dict에 없다면
#         # if dicct.get(key) == None:
result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
