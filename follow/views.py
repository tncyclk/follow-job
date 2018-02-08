from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.http import Http404
from .models import Job
from .forms import LoginForm
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
    return render(request, 'follow/home.html', context)


def job_index(request):
    return HttpResponse('<b>index</b>')

def job_create(request):
    return HttpResponse('<b>create</b>')

def job_detail(request):
    return HttpResponse('<b>detail</b>')

def job_update(request):
    return HttpResponse('<b>update</b>')

def job_delete(request):
    return HttpResponse('<b>delete</b>')