def milo(i,j)


t=int(input())
for tc in range(1,t+1):
    n=int(input())
    matrix=[list(map(int,input().rstrip())) for _ in range(n)]
    visited=[[0]*n for _ in range(n)]
    num=0
    for i in range(n-1,0,-1):
        for j in range(n):
            if matrix[i][j]==2:
                print(f'#{tc} {milo(i,j)}')
                break