from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views
from post.views import filter_by_category


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('filterByCategory', filter_by_category, name='filterByCategory'),
]

