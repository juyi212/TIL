from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'articles/index.html')

def catch(request):
    name=request.GET.get('name')

    context={
        'name':name
    }
    return render(request,'catch.html',context)