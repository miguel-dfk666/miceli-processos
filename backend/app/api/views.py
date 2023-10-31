import logging
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from ..models import CustomUser, Processo
from .serializers import CustomLoginUserSerializer, CustomUserSerializer, PostSerializer
from rest_framework_simplejwt.settings import api_settings
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

# Crie um objeto logger
logger = logging.getLogger(__name__)

class PostViewSet(ModelViewSet):
    queryset = Processo.objects.all()
    serializer_class = PostSerializer

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer 

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValidationError as error:
            # Log de detalhes do erro de validação
            logger.error('Erro de validação durante o registro/fazer login: %s', error)
            return Response({'error': error.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Log de outras exceções não tratadas
            logger.error('Erro interno do servidor: %s', str(e))
            return Response({'error': 'Erro interno do servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomUserLoginViewSet(viewsets.ViewSet):
    serializer_class = CustomLoginUserSerializer
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username_or_email = serializer.validated_data.get('username_or_email')
        password = serializer.validated_data.get('password')

        user = CustomUser.objects.filter(Q(email=username_or_email)| Q(username=username_or_email)).first()

        if user and user.check_password(password):
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler  = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)