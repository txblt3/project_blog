from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Post, FavoritePost
from django import forms
from category.models import Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple
        }

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_posted = timezone.now()
            post.save()
            form.save_m2m()  # Сохраняем многие-ко-многим поля
            return redirect('home')
    else:
        form = PostForm()
        print("eror")
    return render(request, 'posts.html', {'form': form})



def filter_by_category(request):
    category_id = request.GET.get('category')
    posts = Post.objects.all()
    category = None

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        posts = posts.filter(categories=category)

    categories = Category.objects.all()  # Получаем список всех категорий

    context = {
        'posts': posts,
        'category': category,
        'categories': categories,  # Передаем список категорий в контекст
    }

    return render(request, 'users/home.html', context=context)

def search_posts(request):
    query = request.GET.get('q')
    if query:
        # Используем __icontains для выполнения поиска без учета регистра
        posts = Post.objects.filter(content__icontains=query)
    else:
        posts = Post.objects.all()

    context = {
        'posts': posts,
        'query': query,
    }

    return render(request, 'users/home.html', context=context)


def add_to_favorites(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        card_in_favorites = False
        favorite, created = FavoritePost.objects.get_or_create(user=request.user, post=post)
        if created:
            card_in_favorites = True
            print("SUCCES")
        else:
            messages.error(request, 'Пост уже добавлен в избранное.')
    return redirect('post_details', post_id=post_id)

def post_details(request, post_id):
    if post_id:
        post = Post.objects.get(id=post_id)
        context = {
            'card' : post
        }
        return render(request, 'post_detail.html', context)

def favorite_posts(request):
    favorite_posts = FavoritePost.objects.filter(user=request.user)
    categories = Category.objects.all()


    context = {
        'favorite_posts': favorite_posts,
        'categories': categories,

    }
    return render(request, 'favorite_posts.html', context)