from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, forms
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from post.models import Post
from category.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    category_id = request.GET.get('category')
    posts = Post.objects.all()
    categories = Category.objects.all()

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        posts = posts.filter(categories=category)
    else:
        category = None


    """ Формируем страницу """
    context = {
        'categories': categories,
        'posts': posts
    }
    return render(request, 'users/home.html', context=context)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


