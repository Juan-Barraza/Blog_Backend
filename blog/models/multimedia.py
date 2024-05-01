from django.db import models
from .article import Articulo


class Multimedia(models.Model): 
    archivo = models.FileField(upload_to='multimedia/')
    description = models.CharField(max_length=50)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'Multimedia de {self.articulo.title}'
    