def f1(n,g,K,m): #n 고려할 직원 번호, g 직원 수, K 선반 높이, m은 n-1번까지 만들어진 탑의 높이
    global minV


    if n==g:
        if m>=K and minV>m-K:
            minV=m-K
    elif m>=K and minV <= m-K: #고려할 직원이 남아 있지만 탑의 높이가 기존보다 높은 경우
        return # 더 갈 이유가 x 그 이전에서 다른 선택하자
    else:
        f1(n+1,g,K,m)# n번 탑에 참여하지 않음 (이전 직원까지의 높이 m이 그대로 유지)
        f1(n+1,g,K,m+H[n]) #n-1까지의 높이 m + H[n] n번 직원의 높이 더해줌


def f(n,g,K): # n 고려할 직원 번호, g 직원 수
    global minV
    if n==g: # 모든 직원에 대해 고려
        s=0
        print(A)
        for i in range(g):
            if A[i]: # 참여하는 경우
                s+=H[i]  # 키를 더한다
        if s>=K and s-K< minV: #키의 합이 선반 이상이고, 차이가 최소면
            minV=s-K

    else:
        A[n]=0 # n번 직원 미참여
        f(n+1,g,K) # n+1 번 직원 결정하러 이동
        A[n] = 1  # n번 직원 참여
        f(n + 1, g,K)

t=int(input())
for tc in range(1,t+1):
    N,K=map(int,input().split()) # N은 직원수, K 선반 높이
    H=list(map(int,input().split()))
    A=[0]*N #탑에 포함되었는지 표시하기 위함
    minV=10000000
    f(0,N,K)
    # f1(0,N,K,0)
    print(minV)