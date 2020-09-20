import sys
from collections import deque

def bfs(r,c,fuel): #짧은 거리 찾는
    q=deque()
    q.append((r,c,0,fuel))
    visited=[]
    visited.append((r,c))
    while q:
        r,c,d,fuel=q.popleft()
        if fuel<0:
            return -1
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<N and matrix[nr][nc]!=1 and not (nr,nc) in visited:
                if matrix[nr][nc] > 1:
                    im = matrix[nr][nc]
                    q1.append((r, c, im))
                q.append((nr,nc,d+1,fuel-1))
                visited.append((nr,nc))
        if q1:
            break
    if not q1:
        return -1


    if len(q1) > 0:
        q1.sort()
    return q1[0][0], q1[0][1], q1[0][2]

def bfs_a(r,c,im,fuel): #이동 연료 찾는거
    q=deque()
    q.append((r,c,0,fuel))
    visited=[]
    visited.append((r,c))
    while q:
        r,c,d,fuel=q.popleft()
        if fuel<0:
            return -1
        if end_d[r][c]==im:
            fuel=fuel+(d*2)
            end_d[r][c]=0
            return r,c,d,fuel
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<N and matrix[nr][nc]!=1 and not (nr,nc) in visited:
                q.append((nr,nc,d+1,fuel-1))
                visited.append((nr,nc))
    return -1


N,M,fuel=map(int,sys.stdin.readline().split()) #matrix 크기, 승객 수, 연료
matrix=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
r,c=map(int,sys.stdin.readline().split()) # 처음 택시 출발공간

#고객 출발, 도착시점 # -1 씩 빼서 계산하기 !!!!!!
end_d=[[0]*N for _ in range(N)]
for i in range(M):
    point=list(map(int,sys.stdin.readline().split()))
    s,e=point[0],point[1]
    if point[0]==r and point[1]==c:
        matrix[point[0]-1][point[1]-1] = 0
        end_d[point[2] - 1][point[3] - 1] = 0
    else:
        matrix[point[0]-1][point[1]-1]=2+i
        end_d[point[2]-1][point[3]-1]=2+i

print(end_d)
print(matrix)

while True:
    q1=[]
    r,c,im,fuel=bfs(r-1,c-1,fuel)

    print(r,c,im,fuel)

    s_r,s_c,d,fuel=bfs_a(r,c,im,fuel)
    print(s_r, s_c,fuel)

    r,c=s_r,s_c
    print(fuel)


print(fuel)
# if min_m>m:
#     min_m=m
#     min_d=i
# elif min_m==m:
#     min_d=min(i,min_d)
# print(min_m)

# 가장 최소 거리의 인덱스를 어떻게 찾지?
# 찾아서 목적지로 향해야하는데

# else:
#     break
# if min_m==-1:
#     print(-1)
#     break


#
# fuel=fuel-min_m #손님 모시러 감
# if fuel<0:
#     break
# else:
#     fuel=bfs_a(customer_d[min_d][0]-1,customer_d[min_d][1]-1,fuel)
# if fuel>0:
#     r,c=customer_d[min_d][2],customer_d[min_d][3] #목적지
#     customer_d.pop(min_d)
#     if len(customer_d)==0:
#         print(fuel)
#         break
# else:
#     print(-1)
#     break

