from django.db import models
from accounts.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(null=False, blank=False)
    product_image = models.ImageField(upload_to='product_pics/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likey = models.ManyToManyField(User, related_name='likey', blank=True)
    
    def __str__(self):
        return self.name
    
    