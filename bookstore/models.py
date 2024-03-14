from django.db import models

class Books(models.Model):
    
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True)
    pages = models.IntegerField(default=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True )

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        return f'/media/{self.image}'

