from django.urls import path
from restapp import views

urlpatterns=[
    path("",views.display)
]