# 아래 함수를 수정하시오.
def even_elements(num_list):
    even_num = []
    i = 0
    while len(num_list) > i:
        if num_list[i] % 2: # == 1
            num_list.pop(i)
        else:
            i += 1
    even_num.extend(num_list)
    return num_list




my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = even_elements(my_list)
print(result)
