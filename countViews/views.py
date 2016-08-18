from countViews.models import Viewed, Likes

# Create your views here.
def check_views(request, modelname, id):
    ip = request.META['REMOTE_ADDR']
    key = modelname + id
    viewed = Viewed.objects.filter(ip=ip, material=key)
    if len(viewed) > 0:
        return False
    else:
        viewed = Viewed()
        viewed.ip = ip
        viewed.material = key
        viewed.save()
        return True


def check_likes(request, modelname, id):
    ip = request.META['REMOTE_ADDR']
    key = modelname + id
    liked = Likes.objects.filter(ip=ip, material=key)
    if len(liked) > 0:
        return False
    else:
        liked = Likes()
        liked.ip = ip
        liked.material = key
        liked.save()
        return True

