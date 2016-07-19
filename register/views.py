from django.shortcuts import render, redirect
from register.forms import RegistrationForm

# Create your views here.


def register(request):
    if request.POST:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'reg_form.html', {'form':form})
    else:
        return render(request, 'reg_form.html', {'form':RegistrationForm()})