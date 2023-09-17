from django.contrib import messages
from django.shortcuts import redirect, render

from home.models import accounts, events
from django.db import connection


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    context = {}
    if request.method == 'POST':
        try:
            userInfo = accounts.objects.get(email=request.POST.get('email'))
            if (request.POST.get('password') == (userInfo.password)):
                request.session['email'] = userInfo.email
                return redirect('userindex')
            else:
                messages.error(request, 'Password incorrect...!')
        except accounts.DoesNotExist as e:
            messages.error(request, 'No user found for this email....!')

    return render(request, 'login.html', context)

def registration(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('username') and request.POST.get('password') and request.POST.get('email') and request.POST.get('contact'):
            saveRecord = accounts()

            saveRecord.fname = request.POST.get('fname')
            saveRecord.lname = request.POST.get('lname')
            saveRecord.username = request.POST.get('username')
            saveRecord.password = request.POST.get('password')
            saveRecord.email = request.POST.get('email')
            saveRecord.contact = request.POST.get('contact')

            saveRecord.save()
            messages.success(request,"added successfully !!")
            return render(request, 'home.html', context)
            # return HttpResponse("added successfully !!")

    else:
        return render(request, 'registration.html', context)


def createevent(request):
    if request.method == 'POST':
        if request.POST.get('event_type') and request.POST.get('capacity') and request.POST.get('pricing'):
            saveRecord = events()

            saveRecord.event_type = request.POST.get('event_type')
            saveRecord.capacity = request.POST.get('capacity')
            saveRecord.pricing = request.POST.get('pricing')

            saveRecord.save()
            messages.success(request,"added successfully !!")
            return render(request, 'home.html')

    else:
        return render(request, 'createevent.html')
    
def events(request):
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM home_events ORDER BY id DESC;')
    allPosts = cursor.fetchall()
    cursor.close()
    return render(request, 'events.html', {'allPosts': allPosts})