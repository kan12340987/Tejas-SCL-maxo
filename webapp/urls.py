from django.urls import path
from . import views
from Users import views as Users_views

urlpatterns = [
    path('', views.home, name='Users-home'),
    path('about/', views.about, name='Users-about'),
    path('notebook/', views.notebook, name = 'Users-Notebook'),  
    path('home/',views.landingpage, name= 'Users-Homepage'),  
    path('dashboard/', Users_views.dashboard, name='Users-dashboard'),
    path('profile/', Users_views.profile, name='Users-profile'),
]