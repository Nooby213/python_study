# 아래 함수를 수정하시오.
def get_keys_from_dict(info):
    info.keys()
    key_list = []
    for data in info:
        key_list.append(data)
    return key_list


my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']
