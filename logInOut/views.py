from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import Http404

# Create your views here.
def login(request):
    if request.POST:
        if request.POST.get('redirect')=='':
            redirect_str='/'
        else:
            redirect_str=request.POST.get('redirect')
        user_login=request.POST.get('login')
        user_password=request.POST.get('password')
        user=auth.authenticate(username=user_login, password=user_password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            error='Неверное имя пользователя или пароль'
            login=user_login
            return render(request, 'authform.html', {'error': error, 'login':login, 'redirect':redirect_str})


    return render(request, 'authform.html')

def logout(request):
    if request.POST:
        auth.logout (request)
        return redirect(request.POST.get('redirect'))
    else:
        raise Http404
    raise Http404