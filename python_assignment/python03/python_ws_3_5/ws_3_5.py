number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]

def create_user(name, age):
    print(f'{name}님 환영합니다!')
    cus_infor = {}
    cus_infor['name'] = name
    cus_infor['age'] = age
    increase_user()
    return cus_infor
user_list = list(map(create_user, name, age))
many_user = list(map(lambda x : {'name': x['name'], 'age': x['age']}, user_list))
# print(many_user)

number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    return number_of_book

def rental_book(info):
    print(f'남은 책의 수 : {decrease_book(info["age"]//10)}')
    print(f'{info["name"]}님이 {info["age"]//10}권의 책을 대여하였습니다.')

# print(many_user[0])
# rental_book(many_user[0])
list(map(rental_book, many_user))