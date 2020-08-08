N=int(input())
p=[]
for i in range(N):
    arr=list(map(int,input().split()))
    p.append(arr)

rank=[1]*N

for i in range(N):
    for j in range(N-i):
        if i == N-1:
            break
        if p[i][0]>p[i+j][0]:
            if p[i][1]>p[i+j][1]:
                rank[i+j]+=1
        if p[i][1]<p[i+j][1]:
            if p[i][1]<p[i+j][1]:
                rank[i]+=1

rankin=''
for i in range(len(rank)):
    rankin+=f'{rank[i]}'

print(rankin)

#for r in range(0,N):
#     for rr in range(r+1,N):
#         if w[r]<w[rr]:
#             w[r],w[rr]=w[rr],w[r]

# for r in range(0, N):
#     for rr in range(r + 1, N):
#         if h[r] < h[rr]:
#             h[r], h[rr][1] = h[rr][1], h[r][1]
        # elif (z[max][0] < z[rr][0] and z[max][1] > z[rr][1]) or (z[max][0] > z[rr][0] and z[max][1] < z[rr][1]):
        #     c[r]+=1
        # else:
        #     c[rr] = len(z)






#     li.append(count)
#     count += 1
# elif (z[max][0]<z[rr][0] and z[max][1]>z[rr][1]) or (z[max][0]> z[rr][0] and z[max][1]>z[rr][1]):
#     li.append(count)
# else:
#     li.append(N)


