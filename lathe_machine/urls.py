from django.urls import path
from lathe_machine import views
urlpatterns=[
    path('',views.home,name='homepage'),
    path('customer/views.customer',views.customer,name='customer'),
]