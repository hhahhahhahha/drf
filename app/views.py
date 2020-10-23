from rest_framework.viewsets import ModelViewSet
from .serializers import SnippetSerializer
from .models import Snippet

class SnipptModelviewsets(ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
