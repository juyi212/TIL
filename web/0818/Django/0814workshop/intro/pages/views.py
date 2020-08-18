from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def lotto(request):
    numbers=range(1,46)
    lotto=random.sample(numbers,6)
    lotto.sort()
    context={
        'lotto' : lotto,
    }
    return render(request, 'pages/lotto.html',context)


def dtl(request):
    my_sentence = 'Life is short , you need python'
    datetimenow=datetime.now()
    context={
        'my_sentence' : my_sentence,
        'datetimenow': datetimenow
    }
    return render(request,'pages/dtl.html', context)


def index(request):
    return render(request,'pages/index.html')