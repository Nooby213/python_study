import json

# JSON 파일 경로
json_file_path = "C:/Users/SSAFY/Desktop/관프7/07_pjt/버전2_영화/movies/fixtures/movies/movies.json"

# JSON 파일을 읽어옵니다.
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 각 날짜를 변환합니다.
for item in data:
    if 'fields' in item and 'release_date' in item['fields']:
        old_date = item['fields']['release_date']
        new_date = old_date.split('T')[0]  # 'T'를 기준으로 문자열을 분리하여 시간 부분을 제거합니다.
        item['fields']['release_date'] = new_date

# 변경된 데이터를 다시 JSON 파일에 저장합니다.
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
