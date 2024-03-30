N = int(input())
for i in range(N):
    H, W, C = map(int, input().split())
    floor = C % H
    if floor == 0:
        floor = H
        room_num = (C // H)
    else:
        room_num = (C // H) + 1
    if room_num < 10:
        room = f'{floor}0{room_num}'
    else:
        room = f'{floor}{room_num}'
    print(room)