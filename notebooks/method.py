# find
my_str = 'banana'

print(my_str.find('n'))  # 첫 번째 위치
print(my_str.find('z'))  # -1

# index

print(my_str.index('n'))
# print(my_str.index('z'))   # ValueError: substring not found

# isalpha
string1= 'HeΕλληνικάlloㄱㄴㄷㅇ'
string2 = '123ㄱㄴoeㄴㅇ'
print(string1.isalpha())
print(string2.isalpha())

# isupper(). islower()

str1 = 'HELLOddd'
str2 = 'hello'
print(str1.isupper())
print(str2.islower())

# replace(old, new[,count]) 에서 [, count] 는 3번째 인자는 선택인자다. 표기법에 의한 문법
# 프로그래밍 언어의 종류가 다양해서 문법을 표기하는 방법이 달라지기 때문에 통일시킴
# 베커스 나우르
text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text)

# .strip([chars])
text = '              Hello, wordl!    '
new_text = text.strip()
print(new_text)


# .split(sep=None, maxsplit=-1)   지정한 문자를 구분자로 문자열을 분리하여 리스트로 반환
text = 'hello world'
words = text.split()
print(words)

# 'separator'.join(iterable) # itrable 요소들을 원래의 문자열을 구분자로 이용하여 하나의 문자열로 연결
words = ['hello', 'world']
text = ' '.join(words)
print(text)

text = 'hElLo, WorLd!'
new_text1 = text.capitalize()
new_text2 = text.title()
new_text3 = text.upper()
new_text4 = text.swapcase()
print(new_text1)
print(new_text2)
print(new_text3)
print(new_text4)