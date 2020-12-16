from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Users-home'),
    path('about/', views.about, name='Users-about'),
    path('notebook/', views.notebook, name = 'Users-Notebook'),  
    path('home/',views.landingpage, name= 'Users-Homepage'),  
]