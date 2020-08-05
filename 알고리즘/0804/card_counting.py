import sys
sys.stdin=open('sample_input.txt','r')

def countingsort(a,b):
    c=[0]*11
    for i in range(len(b)):
        c[a[i]]+=1 #카운팅

    # for j in range(len(b)):
    #     count_max=c[0]
    #     if j>count_max:
    #         count_max=j
    #         print(c.index(count_max))
    # if count_max==1:
    #     print()

    for j in range(1,len(c)):
        c[j]+=c[j-1] #누적

    for z in range(len(b)): #정렬
        b[c[a[z]]-1]=a[z]
        c[a[z]] -= 1


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = input()
    li=[]
    for i in a:
        li.append(int(i))

    b=[0]*len(li)
    print(countingsort(li,b))
