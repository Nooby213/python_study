# 아래 함수를 수정하시오.
# def capitalize_words(word):
#     return word.title()

def capitalize_words(word):
    # 최종 결과물 : title 화 된 문자열
    result = ''
    temp =''
    # word가 가진 요소 모두 순회
    # 조사 조건:
        # 첫 번째 글자거나, 글자가 공백 다음에 나타나면
        # 첫 번째 글자임을 알 수 있는 방법
        # index가 0이면 첫번째 글자임
        # index와 요소 자체 둘다 필요한 상황
        # range의 원목적 : 범위를 상정 -> 범위를 내가 자유롭게 작성가능
            # range로 범위 산정한 경우 : index만 나오므로
            # 요소를 보려면 word[index] 형식으로 작성해야한다.
        # enumerate의 목전 : 순회가능 요소의 각 요소와 index를 함께 반환
        # for index, char in enumerate(word):
            # print(index, char)
    for index in range(len(word)):
        print(word[index])
        # 현재 순회중인 index번호가 0이라면
        if index == 0 or temp == ' ':
            # index번째 요소를 대문자로 바꿔서 result에 더하기
            result += word[index].upper()
        # 그 외 : 원본 그대로 일단 저장
        # elif: word[index-1] == ' ':
            result += word[index].upper()
        else:
            result += word[index]
        temp = word[index] # 지금 조사했던 단어를 ㄱ록해놓고 다음 조사 시작
    return result
result = capitalize_words("hello, world!")
print(result)
