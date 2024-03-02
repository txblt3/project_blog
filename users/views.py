from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, forms
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from post.models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
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


