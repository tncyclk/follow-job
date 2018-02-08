from django.urls import path
from .views import *

app_name = "follow"

urlpatterns = [
    path('index/', job_index, name="index"),
    path('create/', job_create, name="create"),
    path('<int:id>/', job_detail, name="detail"),
    path('<int:id>/update/', job_update, name="update"),
    path('<int:id>/delete/', job_delete, name="delete"),
    path('form/', form_view, name="form"),

]