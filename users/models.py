from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token

from base.models import TimeStampedModel

from .managers import AccountManager


class Account(AbstractBaseUser, TimeStampedModel, PermissionsMixin):

    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(_("Email Address"), unique=True)

    is_staff = models.BooleanField(
        _("Staff Status"),
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )

    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text="Designates whether this user should be treated as "
        "active. Unselect this instead of deleting accounts.",
    )

    USERNAME_FIELD = "email"
    objects = AccountManager()

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")
        db_table = "accounts"

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
