from datetime import time

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here.

#管理员和用户的模型
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, username
         and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    # email
    email = models.EmailField(unique=True)

    objects = MyUserManager()

    # creation date
    created_at = models.DateTimeField('Creation Time', auto_now_add=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    is_admin = models.BooleanField(default=False)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class User_info(models.Model):
    sex_list={('f','female'),
              ('m','male')}

    email = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    First_Name = models.CharField(max_length=30,null = False)
    Last_Name = models.CharField(max_length=30,null = False)
    Chinese_Name = models.CharField(max_length=30,null=False)
    Sex = models.CharField(max_length=1,choices=sex_list,null = False)
    Nationality = models.CharField(max_length=30,null = False)
    # Date_Of_Birth = models.DateTimeField(null = False)
