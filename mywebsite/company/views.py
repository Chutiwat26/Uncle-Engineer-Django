from django.shortcuts import render
from django.http import HttpResponse # import เพื่อให้สามารถแสดงผลบนหน้าเว็บได้

# Create your views here.
def Home(request):
    return HttpResponse('<h1>Hello World!</h1> <br> <p>My name is chutiwat</p>')