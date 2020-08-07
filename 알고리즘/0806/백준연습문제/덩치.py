N=int(input())
z=[]
for i in range(N):
    x=list(map(int,input().split()))
    z.append(x)
grade=[0]*N

for r in range(0,N-1):
    if z[r][0] <= z[r+1][0] and z[r][1] <= z[r+1][1]:
        max_v=z[r+1]
        max_k = r+1



    #     li[max_k]=count
    # elif (z[r][0]<z[r+1][0] and z[r][1]>z[r+1][1]) or (z[r][0]> z[r+1][0] and z[r][1]>z[r+1][1]):
    #     li[r] = count+1
    # else:
    #     li[r] = count




for r in range(0,N-1):
    max=r
    for rr in range(r+1,N):
        if z[max][0]<z[rr][0] and z[max][1]<z[rr][1]:
            max=rr
    z[r], z[max] = z[max], z[r]
print(z)




#     li.append(count)
#     count += 1
# elif (z[max][0]<z[rr][0] and z[max][1]>z[rr][1]) or (z[max][0]> z[rr][0] and z[max][1]>z[rr][1]):
#     li.append(count)
# else:
#     li.append(N)


