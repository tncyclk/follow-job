from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.http import Http404
from .models import Job
from .models import Project
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages


# Create your views here.

def form_view(request):
    form = LoginForm(request.POST or None, request.FILES or None)
    context = {
        'form': form,
    }

    return render(request, 'follow/form.html', context)


def home_view(request):
    if request.user.is_authenticated:

        context = {
            'isim': 'Tuncay',
        }
    else:
        context = {
            'isim': 'django',
        }
    return render(request, 'home.html', context)


def job_index(request):
    job = Job.objects.all()
    subject = Job.objects.order_by('subject')
    tracker = Job.objects.order_by('tracker')
    print("---->> "+str(subject))
    context = {
        'job': job,
        'subject': subject,
        'tracker': tracker,
    }
    return render(request, 'follow/index.html', context)

def job_create(request):
    return HttpResponse('<b>create</b>')

def job_detail(request):
    return HttpResponse('<b>detail</b>')

def job_update(request):
    return HttpResponse('<b>update</b>')

def job_delete(request):
    return HttpResponse('<b>delete</b>')

#kullanıcı login
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = request.POST['username']
        #print("kullanıcı adı: " + str(username))
        password = request.POST['password']
        #print("parola: " + str(password))
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            #print("kullanıcı login oldu")
            return redirect('home')
    return render(request, 'follow/form.html', {'form': form, 'title': 'Giriş Yap'})

#kullanıcı logout
def logout_view(request):
    logout(request)
    return redirect('home')