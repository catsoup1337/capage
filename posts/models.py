from django.db import models


class Post(models.Model):
    position = models.CharField(max_length=200)
    text = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='/static/media/posts/', blank=True, null=True)

    def __str__(self):
        return self.position



class News(models.Model):
    title_news = models.CharField(max_length=200)
    prew_text = models.TextField(max_length=1000)
    core_text = models.TextField( blank=True, null=True)
    image_news = models.ImageField(upload_to='static/media/posts/', blank=True, null=True)

    def __str__(self):
        return self.title_news
