import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_data(keyword):
    url = f'https://namu.wiki/w/{keyword}'
    # print(soup.select_one('.b-VTlnIA[data-v-65081f62]').text)
    # url = f'https://www.google.com/search?q={keyword}'
    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)
    # 열린 페이지 소스들을 받아온다.
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 눈으로 보기 좋게 출력
    # print(soup.prettify())

    # 파일로 저장하여 왁인
    with open("soup.txt", "w", encoding="utf-8") as file:
        file.write(soup.prettify())

    # 검색 결과 개수
    # result-stats id 를 사용
    result_stats = soup.select_one("#result-stats")
    # print(result_stats.text)

    # 각 게시물을 가져오자
    # 공통적으로 div태그 + g클래스
    g_list = soup.select('div.BFgp7eXo')
    for g in g_list:
        # print(g.text)
        content = g.select_one("div.dkYV+6r2")
        if content is not None:
            print('제목 = ', content)
    g_one = soup.select_one('div.BFgp7eXo')
    print(g_one.text)

keyword = 'BTS'
get_data(keyword)