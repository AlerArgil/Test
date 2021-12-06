from django.urls import path

from clients import views

urlpatterns = [
    path('', views.UserList.as_view(), name='clients-list')
]
