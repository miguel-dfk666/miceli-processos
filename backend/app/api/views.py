from rest_framework.viewsets import ModelViewSet
from ..models import Processo
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
  queryset = Processo.objects.all()
  serializer_class = PostSerializer