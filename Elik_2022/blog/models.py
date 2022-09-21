from django.db import models

# Create your models here.
class Comment(models.Model):
     author = models.CharField(max_length=100)
     body = models.TextField()
     cteated_on = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
     name = models.CharField(max_length=30)

class Post(models.Model):
     title = models.CharField(max_length=250)
     body = models.TextField()
     created_on = models.DateTimeField(auto_now_add=True)
     last_modified = models.DateTimeField(auto_now=True)
     categories = models.ManyToManyField('Category', related_name='posts')
     comment = models.ForeignKey('Comment', on_delete=models.CASCADE)