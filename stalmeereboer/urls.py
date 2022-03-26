from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stalmeereboer-home'),
    path('hengsten/', views.hengsten, name='stalmeereboer-hengsten'),

]
