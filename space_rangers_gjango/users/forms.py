from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm

from users.models import User


class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username", "first_name", "last_name", "email", "gender", "avatar"
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            "username", "first_name", "last_name", "email", "gender", "avatar",
            "level"
        )


class ProfileForm(ModelForm):

    class Meta:
        model = User
        fields = (
            "username", "first_name", "last_name", "avatar"
        )
        labels = {
            "first_name": "Имя", "last_name": "Фамилия",
            "username": "Никнейм", "avatar": "Изображение"
        }
