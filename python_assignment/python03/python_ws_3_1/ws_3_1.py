number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1

# def increase_user(parm):
#     parm += 1
#     return parm

increase_user()
print(f'현재 가입 된 유저 수 : {number_of_people}')

# number_of_people = increase_user(number_of_people)
# print(f'현재 가입 된 유저 수 : {number_of_people}')