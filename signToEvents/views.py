from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.decorators.http import require_http_methods

from mainApp.models import Registration, Event
from signToEvents.forms import MyForm



# Create your views here.
def registrate(request, id):
    subject = get_object_or_404(Event, id=id)
    form = None
    if not subject.need_registration:
        raise Http404
    if request.user.is_authenticated():
        check_registered = Registration.objects.filter(subject__id=id, site_user=request.user)
        if len(check_registered) > 0:
            message = 'На это событие вы уж регистрировались'
        else:
            registration = Registration()
            registration.site_user = request.user
            registration.subject = get_object_or_404(Event, id=id)
            registration.confirmed = True
            registration.email = request.user.email
            registration.name = request.user.username
            registration.save()
            message = 'Вы благополучно зарегистрировалися'
    else:
        # message='Укажите свое имя и электронную почту'
        # form=MyForm()
        # form.subject=id
        message = "К сожалению, регистрация по ссылке временно недоступна"

    return render(request, 'registration/index.html', {'message': message, 'form': form})


@require_http_methods(['POST'])
def reg_by_link(request):
    id = request.POST.get('subject')
    form = MyForm(request.POST)
    form.subject = id
    if not form.is_valid():
        return render(request, 'registration/index.html', {'form': form})
    rec = form.save(commit=False)
    rec.subject = get_object_or_404(Event, id=id)
    check_registered = Registration.objects.filter(subject__id=id, email=form.fields['email'])
    if len(check_registered) > 0:
        message = 'На это событие вы уж регистрировались'
        return render(request, 'registration/index.html', {'message': message, 'form': None})

    rec.save()
    message = 'Для завершения регистации перейдите по ссылке которая была выслана на указанный адрес'
    return render(request, 'registration/index.html', {'message': message, 'form': None})


def confirm(request, sequence):
    registration = get_object_or_404(Registration, link=sequence)
    registration.confirmed = True
    registration.save()
    message = 'Регистрация благополучно завершена'
    return render(request, 'registration/index.html', {'message': message})