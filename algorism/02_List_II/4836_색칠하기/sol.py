import sys
sys.stdin = open('input.txt')
from pprint import pprint as pp

def make_square(y1, x1, y2, x2, color): # 사각형 만들기 함수
    square = [[0]*10 for _ in range(10)]
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1): # 해당 범위에 색을 칠한다.
            square[y][x] = color
    # pp(blank)
    return square

T = int(input())  # 테스트 케이스

for t in range(1, T + 1):
    N = int(input())  # 사각형 갯수
    color_list = [] # 리스트는 순서대로 저장되기 때문에
    box_list = [] # 박스 리스트 저장소
    for n in range(N):  # N개만큼 박스를 만든다.
        y1, x1, y2, x2, color = map(int, input().split())
        color_list.append(color)    #색을 저장한다.
        box_list.append(make_square(y1, x1, y2, x2, color)) # 박스 저장
    # pp(box_list)

    pur_dict = {}   # 보라색 위치를 저장하는 딕셔너리
    for i in range(10):
        for j in range(10): # 10 * 10 좌표에 박스를 놓는다
            for n in range(N):
                for k in range(N):
                    if n == k:
                        break
                    elif color_list[n] != color_list[k]:  # 박스 색이 다르다면 보라색
                        if box_list[n][i][j] != 0 and box_list[k][i][j] != 0:
                            pur_dict[f'{i}{j}'] = 0


    print(f'#{t} {len(pur_dict)}')






