# 아래 함수를 수정하시오.
def sort_tuple(num_tuple):
    new_tuple = ()
    num_list = list(map(int, num_tuple))
    num_list.sort()
    new_tuple = tuple(map(int,num_list))
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
