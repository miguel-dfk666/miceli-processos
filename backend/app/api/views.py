from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Processo, CustomUser
from .serializers import PostSerializer, CustomUserSerializer

class PostViewSet(ModelViewSet):
  queryset = Processo.objects.all()
  serializer_class = PostSerializer
  
class CustomUserCreateAPIView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer 

    def create(self, request, *args, **kwargs):
        # Lógica para criar um usuário
        pass

    def retrieve(self, request, *args, **kwargs):
        # Lógica para obter detalhes de um usuário por ID
        pass

    def update(self, request, *args, **kwargs):
        # Lógica para atualizar um usuário por ID
        pass

    def destroy(self, request, *args, **kwargs):
        # Lógica para excluir um usuário por ID
        pass
