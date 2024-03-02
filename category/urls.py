from django.urls import path
from .views import create_category, edit_category, delete_category, category_list

urlpatterns = [
    path('create/', create_category, name='create_category'),
    path('edit/<uuid:id>/', edit_category, name='edit_category'),
    path('delete/<uuid:id>/', delete_category, name='delete_category'),
    path('/', category_list, name='category_list'),
]