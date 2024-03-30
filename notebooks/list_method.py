my_list =  [1, 2, 3]

# append
my_list.append(4)
print(my_list)

# extend
my_list.extend([7, 8, 9])
print(my_list)

# insert
my_list.insert(3, 'ssafy')
print(my_list)

my_list.remove(4)
print(my_list)

# pop .pop(i)   제거한 값 반환 return이 있다.

item1 = my_list.pop() # 마지막 값
print(item1)
itesm2 = my_list.pop(0)
print(itesm2)

print(my_list)
my_list.append([2,3,4])
print(my_list.pop(1))
my_list.remove('ssafy')
print(my_list)

# .clear() # 리스트의 모든 항목을 삭제

my_list.pop()

