number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    user_infor = {'name' : name, 'age' : age, 'address' : address}
    increase_user()
    return f'{name}님 환영합니다! \n{user_infor}'

result = create_user('홍길동', 30, '서울')
print(result)
print(f'현재 가입된 유저 수 : {number_of_people}')