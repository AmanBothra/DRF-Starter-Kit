from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .manager import CustomUserManager
from lib.models import BaseModel
from lib.utils import PathAndRename, file_size, image_file_extension_validator
from lib.constants import USER_TYPE


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	profile_picture = models.FileField(
		upload_to=PathAndRename('profile_picture/'),
		validators=[image_file_extension_validator],
		blank=True,
	)
	user_type = models.CharField(max_length=50, choices=USER_TYPE, default="admin")
	is_staff = models.BooleanField(default=False)
	is_verified = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)

	# Customize the User model with our custom manager
	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def __str__(self):
		return self.email

	class Meta:
		db_table = 'users'

	def get_full_name(self):
		return f'{self.first_name} {self.last_name}'
