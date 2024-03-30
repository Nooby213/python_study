def bingo():
    global cnt
    for i in range(5):
        for j in range(5):
            call = num_lst[i][j]
            for k in range(5):
                for l in range(5):
                    if borad[k][l] == call:
                        borad[k][l] = 0
                        cnt += 1
            bng = 0
            cross = 0
            back_cross = 0
            for n in range(5):
                row = 0
                col = 0
                if borad[n][n] == 0:
                    cross += 1
                if borad[n][4 - n] == 0:
                    back_cross += 1

                for m in range(5):
                    if borad[n][m] == 0:
                        row += 1
                    if borad[m][n] == 0:
                        col += 1

                if cross == 5:
                    bng += 1
                if back_cross == 5:
                    bng += 1
                if row == 5:
                    bng += 1
                if col == 5:
                    bng += 1

            if bng >= 3:
                return
            else:
                bng = 0


borad = [list(map(int, input().split())) for _ in range(5)]
num_lst = [list(map(int, input().split())) for _ in range(5)]
cnt = 0

bingo()
print(cnt)