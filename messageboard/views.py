from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from . import models
# Create your views here.


def index(request):
    messages = models.Message.objects.all()
    return render(request, 'index.html', {'messages': messages})


def create(request):
    return render(request, 'create.html')


def save(request):
    username = request.POST.get("username")
    title = request.POST.get("title")
    content = request.POST.get("content")
    publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = models.Message(title=title, content=content, username=username, publish=publish)
    message.save()

    return HttpResponseRedirect('/messageboard/index/')