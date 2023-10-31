from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import Q

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo de email é obrigatório.')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        
        # Verifica se o email ou o username já estão em uso
        if self.filter(Q(email=email) | Q(username=username)).exists():
            raise ValueError('Email ou nome de usuário já em uso.')
        
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Processo(models.Model):
    data_processo = models.DateField(default=timezone.now)
    numero_processo = models.CharField(max_length=30, null=True)
    advogado_nome = models.CharField(max_length=100, null=True)
    advogado_oab= models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                regex=r'^\d{4,6}/\w+$',
                message='O número da OAB deve estar no formato correto (UFXXXX). Exemplo: AB1234.',
            ),
        ],
        unique=True,
        null=True
    )
    classe_processo = models.CharField(max_length=100, null=True)
    assunto_principal = models.CharField(max_lenght=255, null=True)
    data_recebimento = models.DateField(default=timezone.now)
    vara = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        self.data_atualizacao = timezone.now()
        super(Processo, self).save(*args, **kwargs)

    def __str__(self):
        return self.numero_processo