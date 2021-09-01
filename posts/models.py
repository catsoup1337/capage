# from django.contrib.auth import get_user_model
# from django.db import models

# User = get_user_model()


# class Post(models.Model):
#     text = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE,
#                                related_name='posts')
#     image = models.ImageField(upload_to='posts/', blank=True, null=True)


from django.db import models
 
 
class Post(models.Model):
    position = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.position