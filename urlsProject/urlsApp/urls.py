from django.contrib import admin
from django.urls import path
from urlsApp import views
urlpatterns = [
    path('hyd/', views.hydjobsInfo),
    path('pune/', views.punejobsInfo),
    path('mum/', views.mumbaijobsInfo),
    path('noida/', views.noidajobsInfo),

]

