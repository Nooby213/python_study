# 아래 함수를 수정하시오.
def remove_duplicates(num_list):
    new_lst = []
    set_lst = set(num_list)
    new_lst = list(set_lst)
    return new_lst

# def remove_duplicates(list):
#     new_lst = []
#     set_lst = set(list)
#     new_lst = [*set_lst]
#     new_lst.sort()
#     return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
