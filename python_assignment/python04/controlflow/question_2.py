# my_dict = {}
# my_dict['key'] = 3
# print(my_dict)   키 값에 직접 입력

'''
numbers = []
my_dict = {'a': 1}
numbers[0] = my_dict
없는 인덱스에 값 할당 할 수 없다.
'''

numbers = []
numbers += [1]
numbers.append(3)
numbers.extend([4, 5, 6])
numbers.insert(2, 100)
print(numbers)

# 같은 기능, 다른 코드, 어떨 때 어떻게
# 각 문자열을 모두 정수로 바꿔서 리스트에 담으시오.
numers_words = '1 2 3 4 5 6 7 8 9 10'

# 문자열을 순회하면서, 정수로 형변환이 가능하면 ...
    # 혹은 공백이 아니면
# 정수로 형변환해서 리스트에 담는다.
# 최종 결과물
numbers = []
# 문자열이 가진 각 요소를 모두 임시변수 char에 할당해서 순회

for char in numers_words:
    # print(char)
    if char != ' ' and char.isnumeric():
        numbers.append(int(char))
print(numbers)
cc = list(map(int, numers_words.split()))
print(cc)

numers_words = ['1 2 3 4 5', '6 7 8 9 10', '11 12 13 14 15']
numbers = []
for words in numers_words:
    conversion_list = list(map(int, words.split()))
    numbers.append(conversion_list)
print(numbers)

numbers = []
numbers = [list(map(int, words.split())) for words in numers_words]
print(numbers)
numbers = [[0] * 10 for _ in range(10)]
print(numbers)