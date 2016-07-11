from django.db import models
from django.contrib.auth.models import User as SiteUser


class CommonArticle(models.Model):
    "Общие свойства статьи и события"
    title=models.CharField(verbose_name='Заголовок', max_length=255)
    content=models.TextField(verbose_name='Текст')
    added=models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    active=models.BooleanField(verbose_name='Видимость', default=True)
    likes=models.SmallIntegerField(verbose_name='Кол-во лайков', default=0)
    views=models.SmallIntegerField(verbose_name='Кол-во просмотров', default=0)
    author=models.ForeignKey(SiteUser)
    class Meta:
        abstract=True



class Article (CommonArticle):
    subject=models.ForeignKey('Event', blank=True)


class Event (CommonArticle):
    date_of_start=models.DateField(verbose_name='Дата начала')
    date_of_finish=models.DateField(verbose_name='Дата завершения', blank=True)
    time_of_start=models.TimeField(verbose_name='Время начала')
    time_of_finish=models.TimeField(verbose_name='Время завершения', blank=True)
    place=models.ForeignKey('Place', blank=True)
    category=models.ManyToManyField('Categories')


class Place(models.Model):
    title=models.CharField(verbose_name='Название', max_length=255)
    adress=models.TextField(verbose_name='Название', max_length=255)


class Categories(models.Model):
    title=models.CharField(verbose_name='Название категории', max_length=50, unique=True)

class Registration (models.Model):
    "Возможность регистрации на события как через УЗ сайта так и через ссылку по имейл"
    #TODO возможно лучше вынести в отдельное приложение
    subject=models.ForeignKey('Event')
    site_user=models.ForeignKey(SiteUser, blank=True)
    name=models.CharField(verbose_name='Имя для регистации через имейл', max_length=100, blank=True)
    email=models.EmailField(verbose_name='Адрес для регистации через имейл', blank=True)
    link=models.URLField(verbose_name='Ссылка для регистрации', blank=True)
    confirmed=models.BooleanField(verbose_name='Подтверждение регистрации', default=False)