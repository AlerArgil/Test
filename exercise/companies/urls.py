from django.urls import path

from companies import views

urlpatterns = [
    path('', views.CompanyList.as_view(), name='companies-list')
]
