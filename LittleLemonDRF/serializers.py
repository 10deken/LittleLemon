from rest_framework import serializers
from .models import Rating, Category, MenuItem, Order, OrderItems
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = Rating
        fields = ['user', 'menuitem_id', 'rating']
        validators = [
            UniqueTogetherValidator(
                queryset=Rating.objects.all(),
                fields = ['user', 'menuitem_id']
            )
        ]
        extra_kwargs = {
            'rating': {'min_value': 0, 'max_value': 5}
        }
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']    
    
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'category', 'featured']