from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('detail/<int:pk>/<slug:slug>/<int:year>/<int:month>/<int:day>/', views.detail, name='detail'),
path('contact/', views.contact, name='contact'),
path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
   path('search/', views.search, name='search'),
]