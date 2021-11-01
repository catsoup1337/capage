from django.db import models


class Post(models.Model):
    position = models.CharField(max_length=200)
    text = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.position


class News(models.Model):
    title_news = models.CharField(max_length=200)
    prew_text = models.TextField()
    core_text = models.TextField()
    image_news = models.ImageField(upload_to='news_pic/', blank=True, null=True)

    def __str__(self):
        return self.title_news