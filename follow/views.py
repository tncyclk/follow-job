from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.http import Http404
from .models import Job
from .models import Project
from django.db.models import Count
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
from django.urls import reverse


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
    jobs = Job.objects.all()
    return render(request, 'follow/index.html', {'jobs': jobs})

def project_index(request):
    projects = Project.objects.all()
    return render(request, 'follow/project.html', {'projects': projects})

def job_create(request):
    return HttpResponse('<b>create</b>')

def job_detail(request, slug):
    jobs = get_object_or_404(Job, slug=slug)
    # print("id: "+str(id))

    context = {
        'jobs': jobs,
    }
    return render(request, 'follow/detail.html', context)

def project_detail(request, slug):
    projects = get_object_or_404(Project, slug=slug)
    print("proje adı: "+str(projects))
    bug_count = Job.objects.filter(project_name=projects, tracker='BUG').count()
    print(bug_count)
    feature_count = Job.objects.filter(project_name=projects, tracker='FEATURE').count()
    test_count = Job.objects.filter(project_name=projects, tracker='TEST').count()
    research_count = Job.objects.filter(project_name=projects, tracker='RESEARCH').count()
    support_count = Job.objects.filter(project_name=projects, tracker='SUPPORT').count()
    context = {
        'bug_count': bug_count,
        'feature_count': feature_count,
        'test_count': test_count,
        'research_count': research_count,
        'support_count': support_count,
        'project_name': projects,
    }
    print(str(context))
    return render(request, 'follow/projectdetail.html', context)
    # return reverse('followprojectdetail.html', kwargs={'slug': self.slug})


def job_update(request):
    return HttpResponse('<b>update</b>')

def job_delete(request):
    return HttpResponse('<b>delete</b>')



#kullanıcı login
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
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