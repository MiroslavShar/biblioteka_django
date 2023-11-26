"""
URL configuration for biblioteka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from polka import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_django),
    path('p/', views.new_task),
    path('time/', views.time_actual),
    path('surname/', views.surname),
    path('lista/', views.lista_zakupów),
    path('ilosc/<int:ilosc>/', views.napis),
    path('witaj/<str:imie>/', views.witaj_dyn),
    path('hello_w', views.hello_world),
    path('random', views.random_numb),
    path('random/<int:max_number>/', views.random_max),
    path('random/<int:min_numb>/<int:max_numb>/', views.random_min_max),
    path('hello/<str:name>/', views.hello_name),
    path('kalkulator/<int:numb1>/<str:znak>/<int:numb2>/', views.kalkulator),
    path('kalkulator2/<int:numb1>/<str:znak>/<int:numb2>/', views.kalkulator2),
    path('tabela/<int:numb1>/<int:numb2>/', views.tabela_mnożenia),
    path('dodaj_osobe/', views.dodaj_osobe),
    path('osoby/', views.wyswietlanie_osob),
    path('osoby/<int:id>/', views.osoba),
    path('addbook/', views.add_book),
    path('books/', views.look_book),
    path('bookid/<int:id>/', views.book_id),
    path('', views.index)
]
