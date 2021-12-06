from django.urls import path

from departaments import views

urlpatterns = [
    path('/', views.DepartamentList.as_view(), name='departaments-list')
]