from email.policy import default
import django
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# Create your models here.


class NormalUser(models.Model):
    # id field
    id = models.AutoField(primary_key=True)
    # user foregin key (one to one field)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    # client identity
    client_identity_id = models.IntegerField(
        validators=[
            MinValueValidator(10_000_000),
            MaxValueValidator(99_999_999),
        ],
        unique=True,
    )
    # client current balance
    current_balance = models.IntegerField(
        validators=[
            MinValueValidator(0_000_000_000_000),
            MaxValueValidator(9_999_999_999_999),
        ]
    )
    user_pin = models.IntegerField(
        validators=[
            MinValueValidator(0_000),
            MaxValueValidator(9_999),
        ],
        default=0000,
    )
    # transaction = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    # notification = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
