from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""
    GENDERS = (
        ("m", "Мужчина"),
        ("f", "Женщина"),
    )

    gender = models.CharField("Пол", max_length=1, choices=GENDERS, default="")
    cr = models.IntegerField("Деньги игрока", default=2000)
    username = models.CharField("Юзернейм", max_length=50, unique=True)
    email = models.EmailField('Email', max_length=254, unique=True)
    first_name = models.CharField('Имя', max_length=50, blank=True, null=True)
    last_name = models.CharField(
        'Фамилия', max_length=50, blank=True, null=True)
    avatar = models.ImageField(
        "Аватарка",
        null=True,
        blank=True,
        upload_to="avatar/",
        help_text="Загрузите аватарку"
    )
    level = models.IntegerField("Уровень", blank=True, null=True, default=1)
    next_level = models.IntegerField(
        "Очков для следущего уровня", blank=True, null=True, default=1000)
    is_level = models.IntegerField(
        "Очков на уровне", blank=True, null=True, default=1)

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name='Автор'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author',),
                name='unique_follow'
            ),
        )
