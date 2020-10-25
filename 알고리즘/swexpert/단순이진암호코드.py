import sys
sys.stdin = open('input3.txt', 'r')

check = {
    '3211' : 0,
    '2221' : 1,
    '2122' : 2,
    '1411' : 3,
    '1132' : 4,
    '1231' : 5,
    '1114' : 6,
    '1312' : 7,
    '1213' : 8,
    '3112' : 9,
}
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())    #세로, 가로
    matrix = [list(map(int, input())) for _ in range(N)]
    # 암호가 있는 인덱스를 찾는 것이 중요
    # 맨뒤에는 1이 무조건 있다.

    for i in range(N):
        for j in range(M-1, -1, -1):
            if matrix[i][j] == 1:
                li = matrix[i][j-55:j+1]
                break

    total = []
    # 각각의 자리를 7개씩 나누고 0,1 몇개인지 숫자 세고 어느 암호와 맞는지 체크 해야함
    for i in range(0, len(li), 7):
        new = [0]*4
        for j in range(i, i+7):
            if li[j] == 0:
                if new[0] >= 0 and new[1] == 0:
                    new[0] += 1
                elif new[2] >= 0 and new[3] == 0:
                    new[2] += 1
            elif li[j] == 1:
                if new[0] != 0 and new[1] >= 0 and new[2] == 0:
                    new[1] += 1
                elif new[2] != 0 and new[3] >= 0:
                    new[3] += 1
        code = ''
        for k in new:
            code += str(k)
        total.append(check[code])

    result = 0
    for i in range(0, len(total), 2):   # 홀
        result += total[i]
    result = result * 3
    for j in range(1, len(total), 2):   # 짝
        result += total[j]
    if result % 10 == 0:
        print(f'#{tc} {sum(total)}')
    else:
        print(f'#{tc} {0}')
