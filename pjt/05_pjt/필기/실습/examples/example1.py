import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def translate_text(text, dest='ko'):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest)
    return translated_text.text

    
url = 'https://quotes.toscrape.com/tag/love/'

# 1. 다운로드 - url을 이용해서, HTML 이 담긴 자료를 받아와야 함
reponse = requests.get(url)

# html 문서를 text 형태로 확인
result = reponse.text
# print(reponse)

#  str이 출력된다.
# print(type(result))

# 문자열 파싱은 코드로 짜기 매우 복잡하다.
# 라이브러리를 쓰자
soup = BeautifulSoup(result, 'html.parser')
# print(soup)

# 1. find
# 첫 번째 태그를 가진 요소를 검색
findA = soup.find('title')
# print(findA.text)
# print(findA)

# 2. find_all
# 해당 태그를 가진 모든 요소를 검색
a_tags = soup.find_all('a')
# print(a_tags)

# 3. select
# CSS 선택자를 사용하여 요소를 검색
# span 태그로도 검색이 간으하지만
# 인용구라는 내용은 text class로 지정
# 따라서 class를 통한 검색이 더 좋다.
a_select = soup.select_one('.text')
print(a_select.text)

# 4. CSS 선택자로 여러개를 선택
# 모든 인용구를 검색
words = soup.select('.text')
for w in words:
    print(translate_text(w.text))