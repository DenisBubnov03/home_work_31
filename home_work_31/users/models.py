from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from home_work_31 import settings
from users.validators import CheckBirthDate


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRoles:
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    choices = (
        (MEMBER, 'Пользователь'),
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
    )


class User(AbstractUser):
    age = models.PositiveSmallIntegerField(blank=True, null=True, editable=False)
    location = models.ManyToManyField(Location)
    role = models.CharField(
        choices=UserRoles.choices,
        default=UserRoles.MEMBER,
        max_length=10
    )
    birth_date = models.DateField()
    email = models.EmailField(
        verbose_name="email address",
        blank=True,
        validators=[RegexValidator(
            regex="|".join(settings.LOCK_DOMAIN_EMAIL),
            inverse_match=True,
            message='Регистрация с указанного домена запрещена!'
        )]
    )

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        self.age = relativedelta(date.today(), self.birth_date).years
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
