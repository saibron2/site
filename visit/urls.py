from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about_site', views.about_site, name='about_site'),
    path('about_klass', views.about_klass, name='about_klass'),
    path('tvort', views.tvort, name='tvort'),
    path('about_me', views.about_me, name='about_me')
]