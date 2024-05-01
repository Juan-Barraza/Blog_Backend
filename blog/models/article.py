from django.db import models
from .category import Category
from .user import User


class Articulo(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def __str__(self) :
        return self.title
    