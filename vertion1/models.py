from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

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

    user_email = models.EmailField(unique=True)

    photo = models.ImageField(upload_to='user_photo/')
    First_Name = models.CharField(max_length=30,null = False,default = 'null')
    Last_Name = models.CharField(max_length=30,null = False,default = 'null')
    Chinese_Name = models.CharField(max_length=30,null=False,default = 'null')
    Sex = models.CharField(max_length=1,choices=sex_list,null = False,default = 'null')
    Nationality = models.CharField(max_length=30,null = False,default = 'null')
    Month = models.CharField(max_length=30,null = False,default = 'null')
    Day =  models.CharField(max_length=30,null = False,default = 'null')
    Year = models.CharField(max_length=30,null = False,default = 'null')
    Place_Of_Birth = models.CharField(max_length = 30,null = False,default = 'null')
    Mather_Tongue = models.CharField(max_length=30, null=False,default = 'null')
    Religion = models.CharField(max_length=30, null=False,default = 'null')
    Health_Condition = models.CharField(max_length=100, null=False,default = 'null')
    Name_Of_Institution = models.CharField(max_length=30, null=False,default = 'null')
    Highest_Education = models.CharField(max_length=30, null=False,default = 'null')
    Email = models.EmailField(null=False,default = 'null')
    Phone_Number = models.CharField(max_length=30, null=False,default = 'null')
    Emergency_Name = models.CharField(max_length=30, null=False,default = 'null')
    Emergency_Relationship = models.CharField(max_length=30, null=False,default = 'null')
    Emergency_Phone = models.CharField(max_length=30, null=False,default = 'null')
    Emergency_email = models.CharField(max_length=30, null=True)
    Name_Of_Sponsor = models.CharField(max_length=30, null=False,default = 'null')
    Sponsor_Relationship = models.CharField(max_length=30, null=False,default = 'null')
    Sponsor_Phone = models.CharField(max_length=30, null=False,default = 'null')
    Sponsor_Email = models.CharField(max_length=30, null=True)
    Mail_Recipient = models.CharField(max_length=30, null=False,default = 'null')
    Mail_Phone = models.CharField(max_length=30, null=False,default = 'null')
    Mail_Address = models.CharField(max_length=30, null=False,default = 'null')
    Mail_City = models.CharField(max_length=30, null=False,default = 'null')
    Mail_Country = models.CharField(max_length=30, null=False,default = 'null')
    Mail_Postcode = models.CharField(max_length=30, null=False,default = 'null')
    Passport_Number = models.CharField(max_length=30, null=False, default='null')
    Date_Of_Expriy = models.CharField(max_length=30, null=False, default='null')
    Passport_Information_Page = models.ImageField("user_passport/")

    submit_status = models.CharField(max_length=30, null=False,default = 'null')

