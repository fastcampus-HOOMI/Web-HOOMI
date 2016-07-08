from django.conf.urls import url

from django.http.response import HttpResponse


def login(request):
    return HttpResponse("this is login")

urlpatterns = [
        url(r'^login$', login, name="login"),
]
