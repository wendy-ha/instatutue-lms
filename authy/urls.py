from django.urls import path
from authy.views import UserProfile
from django.contrib.auth import views as authViews

urlpatterns = [
   	path('login/', authViews.LoginView.as_view(template_name='registration/login.html'), name='login'),
   	path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),

]