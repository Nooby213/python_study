# 아래 함수를 수정하시오.
# def count_character(word, char):
#     num_char = 0
#     for ch in word:
#         if ch == char:
#             num_char += 1
#         else:
#             continue
#     return num_char

def count_character(word, char):
    return word.count(char)

result = count_character("Hello, World!", "o")
print(result)  # 2
