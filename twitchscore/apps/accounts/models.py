from django.db import models
from django.contrib.auth.models import UserManager as DjangoUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from twitchscore.apps.summoners.models import Summoner


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    email = models.EmailField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=255, unique=True)
    summoners = models.ManyToManyField(Summoner)

    is_active = models.BooleanField('Active?', default=False)
    is_staff = models.BooleanField('Have admin access?', default=False)
    date_joined = models.DateTimeField('When joined?', default=timezone.now)

    objects = DjangoUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['email']

    def __str__(self):
        return self.username + ' (%s)' % self.email