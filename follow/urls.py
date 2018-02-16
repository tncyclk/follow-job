from django.urls import path
from .views import *

app_name = "follow"

urlpatterns = [
    path('index/', job_index, name="index"),
    path('create/', job_create, name="create"),
    path('<slug>/', job_detail, name="detail"),
    path('<slug>/update/', job_update, name="update"),
    path('<slug>/delete/', job_delete, name="delete"),
    path('form', form_view, name="form"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('project', project_index, name="project"),
    path('<slug>', project_detail, name="project_detail"),

]
