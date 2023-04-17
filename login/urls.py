from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    # path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.userlogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('welcome/(?<nickname>)', views.welcome, name='welcome'),
    path('cancel/', views.cancel, name='cancel'),
]
