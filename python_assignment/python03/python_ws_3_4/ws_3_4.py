number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people

def create_user(name, age, address):
    print(f'{name}님 환영합니다!')
    cus_infor = {}
    cus_infor['name'] = name
    cus_infor['age'] = age
    cus_infor['address'] = address
    increase_user()
    return cus_infor

# result1 = create_user('김시습', 20, '서울')
# result2 = create_user('허균', 16, '강릉')
# result3 = create_user('남영로', 52, '조선')
# result4 = create_user('임제', 52, '나주')
# result5 = create_user('박지원', 60, '한성부')


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

print(list(map(create_user, name, age, address)))