from ..serializers.keyword import KeywordSerializer
from ..models import Keyword
from rest_framework import viewsets, permissions

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = KeywordSerializer