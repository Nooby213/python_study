a = 1
b = 2


def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c) # 10 2 500

    local(500)
    print(a, b, c) # 10 2 3


enclosed()
print(a, b) # 1 2
my_list = [1, 2, 3]
# 글로벌 변수 정의
global_var = 100
# 함수 정의
def local():
    my_list[0] = 100
    print(my_list)
    # 글로벌 스코프의 변수 함수 내에서 출력
    # print(global_var)
    # 글로벌 변수의 값을 로컬에서 변경 할 수 없다.
    # global_var += 3
    # global_var = 3
    # print(global_var)
local()

global_var = 100
def loca(parm):
    parm += 3
    return parm
global_var = loca(global_var)
print(global_var)

#global 키워드만 사용 x
global_var = 100
def loca():
    global global_var
    global_var += 3
print(global_var)