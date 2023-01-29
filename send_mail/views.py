from audioop import reverse
import re
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home/index.html')

def send_gmail(request):
    if request.method=="POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name,subject,message)

        send_mail(
                'this is subject',
                'this is message ',
                'theaspire2021@gmail.com',
                ['puggibhaiya@gmail.com'],
                fail_silently=False
        )
        return redirect('home')
    else:
        return HttpResponse("Invalid Request!!")