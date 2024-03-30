# 아래 함수를 수정하시오.
# def add_item_to_dict(data, key, value):
#     new_dict = data.copy()
#     add_dict = {key : value}
#     new_dict.update(add_dict)
#     return new_dict

def add_item_to_dict(data, key, value):
    data.update({key : value})
    return data

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
