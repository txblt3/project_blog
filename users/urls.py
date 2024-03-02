from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

