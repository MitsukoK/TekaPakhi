from operator import mod
from django.db import models


class BankingType(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)  # type: ignore
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class BankingMethod(models.Model):
    """Banking Method for all systems

    Foregin Keys:
        * Mobile Banking
        * Bank
        * Mobile Rechanre
        * Gift Card

    Fields:
        * id
        * name (foregin Key)
        * logo (img)
        * type (mb, b, mr, gc)
    """

    auto_increment_id = models.AutoField(primary_key=True)  # type: ignore
    name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to="logos")
    types = models.ForeignKey(BankingType, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name + " | " + self.types.name  # type: ignore
