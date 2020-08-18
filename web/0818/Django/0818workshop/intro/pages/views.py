from django.shortcuts import render
import random

# Create your views here.
def dinner(request,dinner,people):
    context={
        'dinner':dinner,
        'people':people,
    }
    return render(request, 'dinner.html', context)
