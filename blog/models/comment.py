from django.db import models
from .user import User
from .article import Articulo


class Comment(models.Model):
    content = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'Comentario de {self.autor.username} en {self.articulo.titulo}'
    