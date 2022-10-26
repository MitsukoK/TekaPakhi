from django.contrib import admin
from .models import BankingMethod, BankingType

# Register your models here.

admin.site.register(BankingType)
admin.site.register(BankingMethod)
