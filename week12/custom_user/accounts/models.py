from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string


# Create your models here.
class UserManager(BaseUserManager):
    def _create(self, email: str, password: str, **extra_fields) -> 'User':
        if not email:
            raise ValueError('Filed email cannot be empty')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email: str, password: str, **extra_fields) -> 'User':
        extra_fields.setdefault('is_stuff', False)
        return self._create(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields) -> 'User':
        extra_fields.setdefault('is_stuff', True)
        return self._create(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=40, blank=True)
    is_active = models.BooleanField(default=False)
    is_stuff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=20, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name',)

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_stuff

    def has_parm(self, perm, obj=None):
        return self.is_stuff

    def create_activation_code(self):
        code = get_random_string(15)
        self.activation_code = code
        self.save()
