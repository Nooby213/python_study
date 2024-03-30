r = 31
M = 1234567891
# 문자열 길이 L, 1 ≤ L ≤ 50
L = int(input())
# 단어
word = input()
sum_of_word = 0
for i in range(L):
    sum_of_word += (ord(word[i]) - 96) * (r ** i)
else:
    print(sum_of_word % M)
