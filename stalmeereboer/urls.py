from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stalmeereboer-home'),
    path('about/', views.about, name='stalmeereboer-about'),
    path('ponies/', views.ponies, name='stalmeereboer-ponies'),
    path('news/', views.news, name='stalmeereboer-news'),
    path('contact/', views.contact, name='stalmeereboer-contact'),

]
