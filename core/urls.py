
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('store/', views.store, name='store'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('privacidad', views.privacidad, name='privacidad'),
    path('cookies', views.cookies, name='cookies'),
    path('aviso', views.aviso, name='aviso'),
    
]
