t=int(input())
result=[]
for _ in range(t):
    ip=list(input().split('.'))
    result+=[ip]
makeip=[0]*4
diffbite=[]

# 임의 ip & 서브넷 = 네트워크 주소????


for i in range(4):
    same=result[0][i]
    for ii in range(1,t):
        if same==result[ii][i] and not same in makeip:
            makeip[i]=result[ii][i]

        elif same!=result[ii][i]:
            f = format(int(result[0][i]), 'b')
            if not f in diffbite:
                diffbite += [f]
                b = format(int(result[ii][i]), 'b')
                if len(b)<8:
                    bb=b.zfill(8)
                    diffbite += [bb]
            else:
                need_idx=i
                b = format(int(result[ii][i]), 'b')
                if len(b) < 8:
                    bb = b.zfill(8)
                    diffbite += [bb]




print(makeip)
print(diffbite)

makenum=['0']*8
# for i in range(8):
#     for j in range(len(diffbite)):
#     if diffbite[0][i]==diffbite[1][i]==diffbite[2][i]:
#         makenum[i]=diffbite[0][i]
#     else:
#         m=8-i
#         break

print(makenum)
# m 네트워크 마스크를 만들어줘야함.
ip_num=int(''.join(makenum),2) # 최소 바이트값
makeip[need_idx]=ip_num
print(f'{makeip[0]}.{makeip[1]}.{makeip[2]}.{makeip[3]}')
nt_mask=[]
#
# if len(makeip)==4:
#     print('255.255.255.255')
# elif len(makeip)==3:




    # 각각의 바이트를 검색해주고 같다면 패스, 다르면 들어가서 탐색
    # m의 자리를 찾기위해 맨 처음 다른 바이트 안에 들어가 이진수로 바꿔주고
    # 이진수로 바꿔준 각 자리를 탐색해서 같으면 패스, 다르면 다른자리 앞이 m이 된다.
    # m의 자리는 0으로 주워져있음
    # m 다음에 오는 자리수에서 경우의 수가 나오고 이 경우의 수에서 가장 작은 값을 출력
    #(만약 다른 바이트가 2개면 최소를 구하기위해서는 처음 말고 두번째 바이트는 0이 될수도있는건가?)
    # 네트워크 마스크는 m의 자리 다음부터 0 (256.256.256.248)
