from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, email, name, password):
        if not email:
            raise ValueError('Email must not be blank')
        
        user = self.model(
            email = self.normalize_email(email),
            name = name
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email=email, 
            name=name,
            password=password
        )
        user.is_superuser = True
        user.save()

        return user

class Account (AbstractBaseUser):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40, unique=True)
    profile_image = models.ImageField(verbose_name='profile image', upload_to = "uploads/users/profile_images", null=True, blank=True)
    is_superuser = models.BooleanField(verbose_name='is superuser' ,default = False)
    is_staff = models.BooleanField(verbose_name='is staff', default=True)
    is_admin = models.BooleanField(verbose_name='is admin', default=True)
    is_active = models.BooleanField(verbose_name= 'is active', default=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
