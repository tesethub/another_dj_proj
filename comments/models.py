from django.db import models
from django.contrib.auth.models import User as SiteUser
from mainApp.models import *

COMMENTABLE_TYPES=(("Event", "Event"),("Article", "Article"))

# Create your models here.
class Comments(models.Model):
    content=models.TextField(verbose_name='Текст комментария', max_length=1024)
    added=models.DateTimeField(verbose_name='Текст комментария', auto_now_add=True)
    author=models.ForeignKey(SiteUser)
    subject_type=models.CharField(choices=COMMENTABLE_TYPES, max_length=20)
    subject_id=models.PositiveIntegerField(default=0)


