from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    HengstListView,
    HengstDetailView,
    HengstCreateView,
    HengstUpdateView,
    HengstDeleteView
)
from . import views


urlpatterns = [
    path('', views.home, name='stalmeereboer-home'),
    path('about/', views.about, name='stalmeereboer-about'),
    path('ponies/', views.ponies, name='stalmeereboer-ponies'),
    path('news/', PostListView.as_view(), name='stalmeereboer-news'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('contact/', views.contact, name='stalmeereboer-contact'),
    path('hengsten/', HengstListView.as_view(), name='stalmeereboer-hengsten'),
    path('hengst/<int:pk>/', HengstDetailView.as_view(), name='hengst-detail'),
    path('hengst/new/', HengstCreateView.as_view(), name='hengst-create'),
    path('hengst/<int:pk>/update/', HengstUpdateView.as_view(), name='hengst-update'),
    path('hengst/<int:pk>/delete/', HengstDeleteView.as_view(), name='hengst-delete'),

]
