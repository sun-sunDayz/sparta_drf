from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'user', 'description', 'product_image', 'created_at', 'updated_at', 'likey']

