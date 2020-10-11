import sys


def check(x, y, dep):
    global cnt

    if matrix[y][x] == 1:
        for k in range(5, 0, -1):
            if recheck(x, y, k):
                change(x, y, k, 0)
                if x + 1 < 10:
                    check(x + 1, y, dep+1)
                else:
                    if y + 1 < 10:
                        check((x+1) % 10, y + 1, dep+1)
                    else:  # 마지막 종료조건인데, 색종이가 잘 붙어있는지 확인해줘야함
                        print('넘어오나')
                        for n in range(len(matrix)):
                            for m in range(len(matrix)):
                                if matrix[n][m] == 1:
                                    return
                        cnt = dep
                        print(cnt)
                change(x, y, k, 1)

    else:
        print(y, x)
        if x+1 < 10:
            check(x+1, y, dep)
        else:
            if y+1 < 10:
                check((x+1) % 10, y+1, dep)
            else:   # 마지막 종료조건인데, 색종이가 잘 붙어있는지 확인해줘야함
                for n in range(len(matrix)):
                    for m in range(len(matrix)):
                        if matrix[n][m] == 1:
                            return


def recheck(x, y, k):
    for i in range(k):
        for j in range(k):
            if matrix[y+i][x+j] != 1:
                print('>????')
                return 0
    return 1


def change(x, y, k, value):
    for i in range(y, y+k):
        for j in range(x, x+k):
            matrix[i][j] = value


matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
print(matrix)
num = [0, 5, 5, 5, 5, 5]
cnt = 0
check(0, 0, 0)
print(cnt)
# 시작점을 찾으면 덮을 공간을 for 문으로 5 4 3 2 1 체크하고 remove하고