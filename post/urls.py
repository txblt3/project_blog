from django.urls import path
from post import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('search/', views.search_posts, name='search_posts'),   
    path('post-details/<uuid:post_id>/', views.post_details, name='post_details'),
    path('add-to-favorites/<uuid:post_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorite/', views.favorite_posts, name='favorite_posts'),
]

