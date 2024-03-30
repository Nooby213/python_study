# 리스트를 다루는 연습
# 수업시간에 다루지 않은 메서드 라는 개념

def some_func(parm1, parm2):
    # 함수가 하는 일을 작성하는 영역
    result = parm1 + parm2

# 함수를 호출한다.
some_func('가', '나')
# 함수를 호출한 결과를 어떤 변수에 할당해보자.
answer = some_func(1, 2)
# return 값이 없다 -> 파이썬이 알아서 값이 없음을 나타내는 None을 반환한다.
print(answer) # None -> 값이 없음을 나타내기 위한 데이터 타입

# list란 sequence 형태의 데이터다.
# 순서가 있는 값이고, 정렬 되어 있음을 보장하지는 않는다.
#내부 요소를 오름차순으로 정렬하고 싶다.
numbers = [4, 3, 2, 1]
# method 메서드 : 누군가가 가지고 있는 함수
# 리스트가 가지고 있는 sort 메서드 (함수)
result = numbers.sort() # 사용 방법은 함수와 완전히 동일하다.
# print(sorted(numbers, reverse= True))
print()
print(numbers.sort())
print(numbers)
a = '2수육먹고 1싶다.'
b = list(a.split())
c = a
b.sort()
sorted(a)
print(sorted(a))
print(b)
print(c)
# sorted 함수와 sort 메서드의 차이
# list.sort() 메서드는 정렬 대상인 주어(리스트)가 정해져있다.
# 반면 sorted 함수를 '누구를' 정렬할 것인지 저해 줘야한다. -> 순회가능 한 인자를 넘긴다.
# built in function 내장 함수 : 파이썬이 기본적으로 가지고 있는 함수

def some_func(parm1, parm2):
    # 함수가 하는 일을 작성하는 영역
    result = parm1 * parm2
    return result

def other_func(parm1, parm2):
    result = parm1 + parm2
    print(result, '함수 내부에서 실행')
    return result
answer = other_func(2, 3)
print(answer, '함수 외부에서 실행')
def another_func(*args, name):
    pass
another_func(1,2,3,4,5,name='코')