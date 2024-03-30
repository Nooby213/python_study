import sys

sys.stdin = open('input.txt')
from pprint import pprint as pp

T = int(input())  # 테스트 케이스
N = int(input())  # 사각형 갯수


class Box:
    def __init__(self, y1, x1, y2, x2, color):
        y1, x1, y2, x2, color = map(int, input().split())


def make_square(y1, x1, y2, x2, color):  # 사각형 만들기 함수
    blank = [[0] * 10 for _ in range(10)]
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            blank[y][x] = color
    # pp(blank)
    return blank