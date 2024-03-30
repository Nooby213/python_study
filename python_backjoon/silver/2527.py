# 왼쪽 아래 x, y
# 오른쪽 위 p, q
# x < p, y < q
# 직사각형 a, 선분 b, 점 c, 없음 d
# 1사분면에 위치
for _ in range(4):
    squares = list(map(int, input().split()))
    x1, y1, p1, q1, x2, y2, p2, q2 = squares
    # 안 겹칠 때
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')

    # 점
    elif x1 == p2 or x2 == p1:  # x 꼭지점에서 만나고
        if q1 == y2 or q2 == y1:  # y 꼭지점에서 만나고
            print('c')
        else:  # y 선분을 공유한다
            print('b')

    # 선분 / 안 겹치는 경우를 걸러내서 점이 아니라면 선분이다
    elif q2 == y1:
        print('b')
    elif y2 == q1:
        print('b')
    # elif x2 == p1:
    #     print('b')
    # elif p2 == x1:
    #     print('b')

    # 직사각형
    else:
        print('a')
