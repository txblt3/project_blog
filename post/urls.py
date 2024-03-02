from django.urls import path
from post import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
]

