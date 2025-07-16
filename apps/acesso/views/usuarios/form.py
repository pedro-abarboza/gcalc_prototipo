from django.forms import ModelForm
from apps.acesso.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UsernameField



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)
        field_classes = {"username": UsernameField}