from collections import deque

def bfs(r,c,d):
    q=deque()
    q.append((r,c,0))
    visited=[]
    visited.append((r,c))
    while q:
        r,c,d=q.popleft()
        if r ==s_r and c ==s_c:
            return d
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<N and matrix[nr][nc]!=1 and not (nr,nc) in visited:
                q.append((nr,nc,d+1))
                visited.append((nr,nc))

N,M,fuel=map(int,input().split()) #matrix 크기, 승객 수, 연료
matrix=[list(map(int,input().split())) for _ in range(N)]
r,c=map(int,input().split()) # 처음 택시 출발공간
customer_d=[list(map(int,input().split())) for _ in range(M)] #고객 출발, 도착시점 # -1 씩 빼서 계산하기 !!!!!!
print(customer_d)

dis=[]
for i in range(len(customer_d)):
    s_r,s_c=customer_d[i][0]-1,customer_d[i][1]-1
    m=bfs(r-1,c-1,0) # 처음 택시 출발
    dis.append(m)
go=dis.index(min(dis))
print(go) # 처음 최단 거리

#연료랑 출발지점에서 도착하는 지점 거리 잡기

#     e_r,e_c=customer_d[i][2]-1,customer_d[i][3]-1


#BFS ???????