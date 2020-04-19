from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request): # 인덱스페이지(Home)
    return render(request,'accounts/index.html')

def login(request): # Login 페이지 구현 : AuthenticationForm을 import했음 -> models.py, forms.py 안써도 됐다.
    # 이부분 Logic을 잘 이해할 것!
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user()) # login이 아닌 auth_login으로 한 이유 : 재귀로 쭉 도니까 이름을 다르게 import 해왔기 때문
            return redirect('articles:index')
    else: # 처음 들어오면 여기로 와서 accounts/login,html으로 들어가게 됨!!
        form = AuthenticationForm()
    context = {
        'form':form
        }
    return render(request,'accounts/login.html',context)

def logout(request): # Logout 기능
    auth_logout(request) # logout이 아닌 auth_logout으로 한 이유 : 재귀로 쭉 도니까 이름을 다르게 import 해왔기 때문
    return redirect('accounts:index')


def signup(request): # Signup 기능
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # UserCreationForm이라는 특별한 Form을 import 했음 -> models.py, forms.py 안써도 됐다.
        if form.is_valid():
            form.save() # 저장. 이 때 error 문구 뜨면 -> migrate 먼저 의심
            return render(request,'accounts/welcome.html')
    else: # 마찬가지로 처음 들어오면 여기로 와서 accounts/signup.html으로 들어가게 됨!!
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/signup.html',context)