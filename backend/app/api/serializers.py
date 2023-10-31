from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from app.models import Processo, CustomUser
from django.db.models import Q

class CustomLoginUserSerializer(serializers.ModelSerializer):
   username_or_email = serializers.CharField(required=True)
   password = serializers.CharField(required=True, write_only=True)
   class Meta:
        model = CustomUser
        fields = ['username_or_email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
       }

   def validate(self, data):
      username_or_email = data.get('username_or_email')
      password = data.get('password')

      if username_or_email and password:
         user = CustomUser.objects.filter(Q(email=username_or_email) | Q(username_or_email)).first()

         if user and user.check_password(password):
            return user
         else: 
            raise serializers.ValidationError("Credenciais inválidas")
      else:
         raise serializers.ValidationError("Necessário fornecer um nome de usuário ou email e senha")

class CustomUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("As senhas não coincidem.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return CustomUser.objects.create_user(**validated_data)

class PostSerializer(ModelSerializer):
  class Meta:
    model = Processo
    fields = (
        'data_processo',
        'numero_processo',
        'advogado_nome',
        'advogado_oab',
        'classe_processo',
        'assunto_principal',
        'data_recebimento',
        'vara',
    )