from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Rating, MenuItem, Category
from .serializers import RatingSerializer, CategorySerializer, MenuItemSerializer

class RatingsView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
    def get_permissions(self):
        if(self.request.method=='GET'):
            return []
        return [IsAuthenticated()]   

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer