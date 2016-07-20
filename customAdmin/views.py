from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
import mainApp.models as modelsmodule
from django.forms import ModelForm


# Create your views here.
def check_post(request):
    if request.POST:
        return True
    else:
        raise Http404

def index (request):
    if request.user.is_authenticated and request.user.is_superuser:
        output={'content':[]}
        for key, value in modelsmodule.__dict__.items():
            if not (key.startswith('__') or key=='models'):
                try:
                    our_queryset=value.objects.all()
                    output['content'].append({'name':key, 'our_queryset': our_queryset})
                except:
                    continue

        return render(request, 'customAdmin.html', output)
    else:
        return render(request, 'authform.html')#TODO доделать перенаправление


def delitem(request):
    if request.user.is_authenticated and request.user.is_superuser:
        check_post(request)
        modelname=request.POST.get('model')
        our_object=get_object_or_404(modelsmodule.__dict__[modelname], id=request.POST.get('id'))
        our_object.delete()
        return redirect('/cadmin/')
    else:
        return render(request, 'authform.html')

def show_form(request):
    modelname=request.POST.get('model')
    class MyForm(ModelForm):
        class Meta:
            fields='__all__'
            model=modelsmodule.__dict__[modelname]

    if request.POST.get('id'):
        our_object=get_object_or_404(modelsmodule.__dict__[modelname], id=request.POST.get('id'))
        form=MyForm(instance=our_object)
    else:
        form=MyForm()
    return  render(request, 'show_form.html', {'form':form, 'model':modelname, 'id':request.POST.get('id')})

def save_form(request):
    modelname=request.POST.get('model')
    id=request.POST.get('id')
    class MyForm(ModelForm):
        class Meta:
            fields='__all__'
            model=modelsmodule.__dict__[modelname]

    if id=='None' or id is None:
        form=MyForm(request.POST)
    else:
        our_object=get_object_or_404(modelsmodule.__dict__[modelname], id=id)
        form=MyForm(request.POST, instance=our_object)

    if form.is_valid():
        form.save()
        return redirect('/cadmin/')
    else:
        return render(request, 'show_form.html', {'form':form, 'model':modelname, 'id':id})