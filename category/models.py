from django.db import models
import uuid


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,
                          verbose_name='ID')

    name = models.CharField(max_length=100, 
                            verbose_name='Название категории')

    description = models.TextField(blank=True)


    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'  
    
    def __str__(self):
        return self.name