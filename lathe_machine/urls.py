from django.urls import path
from lathe_machine import views
urlpatterns=[path('',views.home,name='homepage')]