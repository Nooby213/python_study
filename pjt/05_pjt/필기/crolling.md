- 웹 페이지에 있는 정보를 가져오는 방법
1. 데이터 다운로드 받기 (ex. 캐글)
2. API Server를 활용하여 정보를 받아오기
3. 사람이 검색하는 것처럼 자동으로 검색 후 결과를 수집하는 방법 : 크롤링

## 데이터 수집
- 웹 스크래핑 : 웹 페이지에서 데이터를 추출하는 기술
- 웹 크롤링 : 웹 페이지를 자동으로 탐색하고 데이터를 수집하는 기술
- Open API활용 : 공개된 API를 통해 데이터를 수집
- 데이터 공유 플랫폼 활용 : 다양한 사용자가 데이터를 공유하고 활용할 수 있는 온라인 플랫폼
  - 종류 : 캐글, data.wordl, 데이콘(Dacon), 공공데이터포털
---
## 웹 크롤링이란?
- 여러 웹 페이지를 돌아다니며 원하는 정보를 모으는 기술
- 웹 사이트들을 돌아다니며 필요한 데이터를 추출하여 활용할 수 있도록 자동화 하는 기술

### 웹 크롤링 프로세스
- 웹 페이지 다운로드
  - 해당 웹 페이지의 HTML, CSS, JavaScript 등의 코드를 가져오는 단계
- 페이지 파싱
  - 다운로드 받은 코드를 분석하고 필요한 데이터를 추출하는 단계
- 링크 추출 및 다른 페이지 탐색
  - 다른 링크를 추출하고, 다음 단계로 이동하여 원하는 데이터를 추출하는 단계
- 데이터 추출 및 저장
  - 분석 및 시각화에 사용하기 위해 데이터를 처리하고 저장하는 단계

#### 파이썬에서 크롤링 준비
1. requests : HTTP 요청을 보내고 응답을 받을 수 있는 모듈
2. BeautifulSoup : HTML 문서에서 원하는 데이터를 추출하는데 사용되는 파이썬 라이브러리
3. Selenium : 웹 애플리케이션을 테스트하고 자동화하기 위한 파이썬 라이브러리
  - 웹 페이지의 동적인 컨텐츠를 가져오기 위해 사용함 (검색 결과 등)
---
#### BeautifulSoup4 메서드 종류
```py
import requests
from bs4 import BeautifulSoup

reponse = requests.get(url)
result = reponse.text
soup = BeautifulSoup(result, 'html.parser')
```
- find()
  - 태그를 사용하여 요소를 검색. 첫 번째로 일치하는 요소를 반환
```py
findA = soup.find('title')
print(findA.text)
print(findA)
```
- find_all()
  - 태그를 사용하여 요소를 검색. 모든 일치하는 요소를 리스트로 반환
```py
a_tags = soup.find_all('a')
print(a_tags)
```
- select()
  - CSS 선택자를 사용하여 요소를 검색. 모든 일치하는 요소를 리스트로 반환
```py
a_select = soup.select('.text')
print(a_select)
```
- select_one()
  - CSS 선택자를 사용하여 요소를 검색. 첫 번째로 일치하는 요소를 반환
```py
a_select = soup.select_one('span')
print(a_select.text)
```
- find_parent() / find_next_sibling() / find_previous_sibling()
  - 태그를 사용하여 요소를 검색. 각각 일치하는 요소의 부모 / 다음 형제 요소 / 이전 형제 요소를 반환