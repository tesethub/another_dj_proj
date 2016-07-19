from django.shortcuts import render
from countViews.models import Viewed

# Create your views here.
def views(request, modelname, id ):
    ip=request.META['REMOTE_ADDR']
    key=modelname+id
    viewed=Viewed.objects.filter(ip=ip, material=key)
    if len(viewed)>0:
        return False
    else:
        viewed=Viewed()
        viewed.ip=ip
        viewed.material=key
        viewed.save()
        return True

