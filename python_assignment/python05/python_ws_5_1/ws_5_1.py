# 아래 함수를 수정하시오.
# def reverse_string(word):
#     word_list = list(word)
#     word_list.reverse()
#     word_reverse = ''.join(word_list)
#     return word_reverse

# 순회를 뒤에서부터 앞으로 반대순
# 그래서 대체적으로 sequence 순회시에는
# ranege를 사용해서 index 기준 순회를
# range로 원래 word가 가진 각 요소를 출력
# def reverse_string(word):
#     result = ''
#     for index in range(len(word)):
#         print(index, word[index])

#     for index in range(len(word)-1, -1, -1):
#         return f'{word[index], end=""}'

# def reverse_string(word):
#     return word[::-1]

def reverse_string(word):
    word_reverse =''
    for c in word:
        word_reverse = c + word_reverse
    return word_reverse

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH

# a = "Hello, World!"
# print(a[::-1])
