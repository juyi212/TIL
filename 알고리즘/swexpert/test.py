
def check(r, c, cnt, const):
    global total

    if total <= cnt:
        total = cnt

    for dr, dc in ([1, 0],[-1, 0],[0, 1],[0, -1]):
        nr, nc = r + dr, c+dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if matrix[r][c] > matrix[nr][nc]:   # 그냥 적을 때
                visited[nr][nc] = True
                check(nr, nc, cnt+1, const)
                visited[nr][nc] = False

            elif matrix[r][c] <= matrix[nr][nc] and not const: # 공사할 공간 설렉
                for i in range(1, K+1): # 빼보면서 작은 구간이 있으면 공사한다.
                    matrix[nr][nc] -= i
                    const = True
                    if matrix[r][c] > matrix[nr][nc]:
                        visited[nr][nc] = True
                        check(nr, nc, cnt+1, const)
                        visited[nr][nc] = False
                    const = False
                    matrix[nr][nc] += i



for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_num = max(map(max, matrix))
    max_li = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == max_num:
                max_li.append((i, j))
    total = -1

    for r, c in max_li:
        visited = [[False]*N for _ in range(N)]
        visited[r][c] = True
        check(r, c, 1, False)
    print(f'#{tc} {total}')

'''

10        
5 1       
9 3 2 3 2 
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2       
1 2 1     
2 1 2
1 2 1

'''