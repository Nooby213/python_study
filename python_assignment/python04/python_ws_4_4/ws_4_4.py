import requests
import pprint as pprint

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
# print(response)

# 변환 데이터 출력
# print(parsed_data)
# 변환 데이터의 타입
# print(type(parsed_data))

# 특정 데이터 출력
dummy_data = []
for i in range(10):
    data_dict = {}
    data_dict['name'] = parsed_data[i]['name']
    data_dict['lat'] = parsed_data[i]['address']['geo']['lat']
    data_dict['lng'] = parsed_data[i]['address']['geo']['lng']
    data_dict['company_name'] = parsed_data[i]['company']['name']
    dummy_data.append(data_dict)
# pprint.pprint(dummy_data)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

# user_name = []
# for user in dummy_data:
#     user_name.append(user['name'])

def create_user():
    censored_user_list = {}
    for user in dummy_data:
        user_name = []
        user_name.append(user['name'])
        if censored_user_lists(user['company_name'], user['name']):
            censored_user_list[f'{user["company_name"]}'] = user_name
        else:
            pass
    print(censored_user_list)


def censored_user_lists(user_company, user_name):
    if user_company in black_list:
        print(f'{user_company} 소속의 {user_name} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True
        
create_user()


# user_list = []
# user_name_list = []
# def create_user():
#     censored_user_list = {}
#     for user in dummy_data:
#         censored_user_list[f'{user["company"]}'] = user['name']
#         user_name_list.append(censored_user_list[f'{user["company"]}'])
#         user_list.append(censored_user_list)
#     censorship()

# def censorship():
#     for user_com in black_list:
#         for new_user in user_list:
#             if user_com == new_user['company']:
#                 print(f'{new_user["company"]}소속의 {new_user["name"]} 은/는 등록할 수 없습니다.')
#                 return False
#             else:
#                 print('이상 없습니다.')
#                 return True
# create_user()
# censorship
