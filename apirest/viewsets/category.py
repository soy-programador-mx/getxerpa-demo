from ..serializers.category import CategorySerializer
from ..models import Category
from rest_framework import viewsets, permissions

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer