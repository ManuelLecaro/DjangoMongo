#from django.db import models
from djongo import models
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=500)
    last_update = models.DateField()

    class Meta:
        abstract = True


#Se crea la tabla Blog (documento), con title, content y la fecha de publicación y/o actualización
class Blog(models.Model):
    blog = models.EmbeddedModelField(
        model_container=Post,
    )
    recent_update = models.DateField()
    objects = models.DjongoManager()

#    def __str__(self):
#        return self.post


class Entry(models.Model):
    blog = models.EmbeddedModelField(
        model_container=Blog,
    )
    
    headline = models.CharField(max_length=255)
