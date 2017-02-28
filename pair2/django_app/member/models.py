from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class MyUser(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True)
    nickname = models.CharField(max_length=20)
    following = models.ManyToManyField(
        'self',
        blank=True,
        null=True,
        symmetrical=False

    )
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    object = MyUserManager()

    def get_short_name(self):
        return '{}'.format(self.username)

    def get_full_name(self):
        return '{} ({})'.format(
            self.username,
            self.nickname,
        )

    def follow(self, user):
        self.following.add(user)

    def unfollow(self, user):
        self.following.remove(user)

    def followers(self, user):
        self.myuser_set.all()
