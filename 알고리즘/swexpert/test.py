from collections import deque

def check(r, c):
    global cnt

    nxt_check = []
    for k in range(8):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if matrix[nr][nc] == '.':
                nxt_check.append((nr, nc))
            else:   # 지뢰일 때
                break
    else:
        if nxt_check: # 주변에 지뢰가 없을 때 퍼져 나간다
            matrix[r][c] = 0
            cnt += 1
            spread(nxt_check)

def spread(nxt_check):
    q = deque(nxt_check)
    nxt_nxt = []
    while q:
        x, y= q.popleft()
        matrix[x][y] = 0 # 이미 전에 클릭이 된 것들이라 0으로 다 바꿔줘야함
        for k in range(8):
            nr, nc = x + dr[k], y + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if matrix[nr][nc] == '.':
                    nxt_nxt.append((nr, nc))
                else: # 지뢰일때는 멈춤
                    break

        else:
            if nxt_nxt:
                spread(nxt_nxt)



for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    dr, dc = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '.':
                check(i, j)
    else:
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == '.':
                    cnt += 1

    for i in matrix:
        print(*i)
    print(cnt)


'''
2
3
..*
..*
**.
5
..*..
..*..
.*..*
.*...
.*...

'''