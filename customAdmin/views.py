from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test

import mainApp.models as modelsmodule
from customAdmin.forms import form_construct




# Create your views here.
def check_post(request):
    if request.POST:
        return True
    else:
        raise Http404


@user_passes_test(lambda u: u.is_superuser, login_url='/log/admin/')
def index(request):
    output = {'content': []}
    for key, value in modelsmodule.__dict__.items():
        if not (key.startswith('__') or key == 'models'):
            try:
                our_queryset = value.objects.all()
                output['content'].append({'name': key, 'our_queryset': our_queryset})
            except:
                continue

    return render(request, 'customAdmin.html', output)


@user_passes_test(lambda u: u.is_superuser, login_url='/log/admin/')
def delitem(request):
    if request.user.is_authenticated and request.user.is_superuser:
        check_post(request)
        modelname = request.POST.get('model')
        our_object = get_object_or_404(modelsmodule.__dict__[modelname], id=request.POST.get('id'))
        our_object.delete()
        return redirect('/cadmin/')
    else:
        return render(request, 'authform.html')


@user_passes_test(lambda u: u.is_superuser, login_url='/log/admin/')
def show_form(request):
    modelname = request.POST.get('model')

    if request.POST.get('id'):
        our_object = get_object_or_404(modelsmodule.__dict__[modelname], id=request.POST.get('id'))
        form = form_construct(modelsmodule.__dict__[modelname])(instance=our_object)
    else:
        form = form_construct(modelsmodule.__dict__[modelname])
    return render(request, 'show_form.html', {'form': form, 'model': modelname, 'id': request.POST.get('id')})


@user_passes_test(lambda u: u.is_superuser, login_url='/log/admin/')
def save_form(request):
    modelname = request.POST.get('model')
    id = request.POST.get('id')

    if id == 'None' or id is None:
        form = form_construct(modelsmodule.__dict__[modelname])(request.POST)
    else:
        our_object = get_object_or_404(modelsmodule.__dict__[modelname], id=id)
        form = form_construct(modelsmodule.__dict__[modelname])(request.POST, instance=our_object)

    if form.is_valid():
        form.save()
        return redirect('/cadmin/')
    else:
        return render(request, 'show_form.html', {'form': form, 'model': modelname, 'id': id})

