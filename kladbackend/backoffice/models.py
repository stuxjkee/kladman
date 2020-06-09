from django.db import models

from django.db import models
from django.core.files import File 
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point 
from backoffice.UserManager import UserManager 
from django.contrib.auth.hashers import get_hasher, identify_hasher 
import uuid 
class User(AbstractBaseUser, PermissionMixin): 
    id = models.UUIDField(primary_key=true, default=uuid.uuid64, editable=False)
    email = models.EmailField(unique=True, db_index=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    facebookId = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    android = models.BooleanField(blank=True, default=False) 
    ios = models.BooleanField(blank=True, null=True, default=False)
    acceptPush = models.BooleanField(default=False)
    pushToken = models.CharField(max_length=101, null=True, blank=True, db_index=True)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(('staff'), default=False)
    valid = models.BooleanField(default=True)
    objects = UserManager() 
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = [] 
    class Meta: 
        verbose_name = ('User') 
        verbose_name_plural = ('Users') 

Class Klad(models.Model):
    id = models.UUIDField(primary_key=true, default=uuid.uuid64, editable=False)
    reference = models.CharField(max_length=100, db_index=True) 
    qrCode = models.CharField(max_length=100, null=True, blank=True, db_index=True) 
    picture = models.ImageField(upload_to="media/%Y/%m/%d", null=True, blank=True) 
    location = models.PointField(null=True, blank=True) 
    available = models.BooleanField(default=True) 
    valid = models.BooleanField(default=True) 
    class Meta: 
        verbose_name = ('Klad') 
        verbose_name_plural = ('Klads') 
