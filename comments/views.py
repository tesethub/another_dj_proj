from django.shortcuts import render, get_object_or_404, redirect
from comments.models import Comments
import mainApp.models as mainappmodule
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_http_methods

# Create your views here.
def show_comments(modelname, subject):
    comments=Comments.objects.filter(subject_id=subject, subject_type=modelname).order_by('-added')
    return comments

@require_http_methods('POST')
@user_passes_test(lambda u: u.is_authenticated, login_url='/')
def add_comment(request):
    subject_type=request.POST['subject_type']

    new_record=Comments()
    new_record.author=request.user
    new_record.subject_id=request.POST['id']
    new_record.subject_type=subject_type
    new_record.content=request.POST['content']
    new_record.full_clean()
    new_record.save()
    return redirect('/')