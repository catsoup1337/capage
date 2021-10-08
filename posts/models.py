from django.db import models
 
 
class Post(models.Model):
    position = models.CharField(max_length=200)
    text = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.position