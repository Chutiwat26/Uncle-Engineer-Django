from django.shortcuts import render # render เป็นคำสั่งสำหรับสั่งให้อ่าน html
from django.http import HttpResponse # import เพื่อให้สามารถแสดงผลบนหน้าเว็บได้

# Create your views here.
#def Home(request):
 #   return HttpResponse('<h1>Hello World!</h1> <br> <p>My name is chutiwat</p>')

def Home(request):
    return render(request, 'company/home.html')
