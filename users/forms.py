from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Account


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("name", "email",)


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ("name", "email",)
