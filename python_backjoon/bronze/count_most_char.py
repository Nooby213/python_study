# 통과 방법
word = input().upper()
word_copy = set(word)

count_c = 0
mm = ''
mc = ''

for i in word_copy:
    if word.count(i) > count_c:
        count_c = word.count(i)
        mm = i
    elif word.count(i) == count_c:
        mc = i

if word.count(mc) == count_c:
    print('?')
else:
    print(mm)

# 시간 초과
    
import sys
input = sys.stdin.readline
word = input().upper()
word_dict = {}
# print(word_dict)


most_count = 0

for c in word:
    i = word.count(c)
    word_dict[c] = i
    if i > most_count:
        most_count = i

del word_dict['\n']

num_list = []
for key, value in word_dict.items():
    if value == most_count:
        num_list.append(key)

if len(num_list) > 1:
    print('?')
else:
    print(num_list[0])
