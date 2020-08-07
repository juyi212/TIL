import sys
sys.stdin=open("input_search.txt","r")

T=int(input())
for test_case in range(1,T+1):
    n=int(input()) #길이
    arr=[list(map(int,input().split())) for _ in range(n)]
    total=[]
    count=0
    for x in range(n): #행
        for y in range(n): #열
            if arr[x][y] != 0:
                col_count=0
                for k in range(y,n):
                    if arr[x][k]:
                        col_count+=1
                    else:
                        break
                row_count=0
                for k in range(x,n):
                    if arr[k][y]:
                        row_count+=1
                    else:
                        break
                for k in range(x, x + row_count):
                    for l in range(y, y + col_count):
                        arr[k][l]=0
                count+=1
                total.append((row_count,col_count,row_count*col_count))
    for i in range(0,len(total)-1):
        min=i
        for j in range(i+1,len(total)):
            if total[min][2]>total[j][2]:
                min=j
            elif total[min][2]==total[j][2]:
                if total[min][0]>total[j][0]:
                    min=j
        total[i], total[min] = total[min], total[i]
    print(f'#{test_case} {count}',end=' ')
    for i in range(len(total)):
        for j in range(0,2):
            print(total[i][j],end=' ')
    print(end='\n')


