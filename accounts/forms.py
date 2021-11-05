from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from cart.models import Account



User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email",)

class AccountForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('orders',)