from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', views.home, name='home'),
path('detail/<int:pk>/<slug:slug>/<int:year>/<int:month>/<int:day>/', views.detail, name='detail'),
path('contact/', views.contact, name='contact'),
path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
   path('search/', views.search, name='search'),
]

#if settings.DEBUG:
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
