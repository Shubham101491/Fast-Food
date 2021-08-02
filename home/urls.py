from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('news/', views.news, name='news'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('order/', views.order, name='order'),
]