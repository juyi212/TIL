import sys
sys.stdin=open('sample_input_sum.txt','r')

for test_case in range(1,11):
    T = int(input())
    a = list(map(int, input().split()))
    while T>0:
        b=max(a)
        a.remove(b)
        a.append(b-1)

        c=min(a)
        a.remove(c)
        a.append(c+1)
        T-=1
    print(f'#{test_case} {max(a)-min(a)}')








