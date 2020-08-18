import random
import requests
from django.shortcuts import render

# Create your views here.
def lotto(request):
    url="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=924"
    response=requests.get(url).json()
    li=[]
    for i in range(1,7):
        li.append(response.get(f'drwtNo{i}'))
    
    bonus=response.get('bnusNo')
    count=0
    one,two,three,four,five=0,0,0,0,0
    # 1. numbers에 있는 값을 하나씩 뽑아서 winner에 있는지
    # 2. set을 이용해서 교집합
    for i in range(1,1001):
        numbers=list(random.sample(range(1,46),6))
        for j in numbers:
            if j in li:
                count+=1
        if count==6:
            one+=1
        elif count==5 and bonus in numbers:
            two+=1
        elif count==5:
            three+=1
        elif count==4:
            four+=1
        elif count==3:
            five+=1


    context={
        'a': li,
        'bonus':bonus,
        'one':one,
        'two':two,
        'three':three,
        'four':four,
        'five': five,
        'bang': 1000-(one+two+three+four+five)
    }
    return render(request,'lotto.html',context)