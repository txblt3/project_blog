from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from category.models import Category
import uuid



class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,
                          verbose_name='ID')

    title = models.CharField(max_length=100)

    content = models.TextField()

    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    categories = models.ManyToManyField(Category,
                                        related_name='posts')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'id': self.id})