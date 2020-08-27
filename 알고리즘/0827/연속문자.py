
t=int(input())
for tc in range(1,t+1):
    string=list(input())
    check=[0,]

    while len(check)>0:
        check.pop()
        for i in range(len(string)):
            if len(check)==0:
                check.append(string[i])

            elif len(check)>0:
                if check[-1] == string[i]:
                    check.pop()
                else:
                    check.append(string[i])
        if len(check)!=0:
            break
    print(f'#{tc} {len(check)}')



'''
ABCCB
'''


