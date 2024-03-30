data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for info in data:
    for key in key_list:
        if info.get(key) != None:
            print(f'{key}은/는 {info.get(key)}입니다.')
        else:
            info.setdefault(key, 'unknown')
            print(f'{key}은/는 {info.get(key)}입니다.')
    print()