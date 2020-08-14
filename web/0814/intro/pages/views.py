import random
from django.shortcuts import render

# Create your views here.

def lotto(request):
    number=list(range(1,50))
    ran_number=random.sample(number,6)
    context={
        'ran_number': ran_number,
    }
    return render(request, 'lotto.html', context)