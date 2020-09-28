r,c=map(int,input().split()) #세, 가
p,q=map(int,input().split()) #개미 위치
t=int(input())

tx,ty=t%(r*2),t%(c*2) #풀필요한 반복되는 시간을 줄여주기, 순환되는 시간이 있음