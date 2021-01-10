from django.urls import path
from . import views
from Users import views as Users_views
from discussion_Forum import views as diss_views

urlpatterns = [
    path('', views.home, name='Users-home'),
    path('about/', views.about, name='Users-about'),
    path('notebook/', views.notebook, name = 'Users-Notebook'),  
    path('textbook/', views.textbook, name = 'Users-Textbook'), 
    path('questionpapers/', views.questionpapers, name = 'Users-Papers'),        
    path('home/',views.landingpage, name= 'Users-Homepage'),  
    path('dashboard/', Users_views.dashboard, name='Users-dashboard'),
    path('profile/', Users_views.profile, name='Users-profile'),
    path('logout/',Users_views.logOut, name='Users-logout'),
    path('contact/',diss_views.home, name='contact'),
    path('forum_home/',diss_views.home, name='forum_home'),

    path('test/', views.search, name='test-search'),

]