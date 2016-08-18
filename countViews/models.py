from django.db import models

# Create your models here.
class Common(models.Model):
    ip = models.GenericIPAddressField()
    material = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Viewed(Common):
    pass


class Likes(Common):
    pass
