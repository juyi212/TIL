# 0917_practice

## 1. user create

/accounts/signup/

![image-20200917173501439](C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20200917173501439.png)

```python

def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method=='POST':
        form =UserCreationForm(request.POST) #form
        if form.is_valid():
            user=form.save()
            # 이 때 유저는 인증된 유저 
            auth_login(request,user)
            return redirect('accounts:index')
    else:
        form=UserCreationForm()
    context={
        'form':form,
    }
    return render(request,'accounts/signup.html',context)
```



## 2. login

![image-20200917173633634](C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20200917173633634.png)

```python
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid(): #검증되면 로그인 해야 함.
            auth_login(request,form.get_user()) #유저정보가 업데이트됨
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form =AuthenticationForm()
    context={
        'form':form,
    }
    return render(request,'accounts/login.html',context)
```



## 3. Logout

![image-20200917173746425](C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20200917173746425.png)

```python
@require_POST 
def logout(request):
    if request.user.is_authenticated: #login_required 를 require_post랑 같이 스지 못하는 이유는 ? typora 참고
        auth_logout(request)
    return redirect('accounts:index')
```



## 4. user update

![image-20200917173824465](C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20200917173824465.png)

```python
@login_required
def update(request):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user) #update에 관한 무언가를 받을 수 있는 폼을 생성해준다.
    context={
        'form':form,
    }
    return render(request,'accounts/update.html',context)
```



## 5. user delete

```python
@require_POST
def delete(request):
    if request.user.is_authenticated: #D
        request.user.delete()
    return redirect('accounts:index')
```

