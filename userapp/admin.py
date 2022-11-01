from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from .models import NormalUser

# Register your models here.


class NormarUserInline(admin.StackedInline):
    # model = NormalUser
    model = NormalUser
    can_delete = False
    verbose_name_plural = "Users"


class CustomNormalUserSet(UserAdmin):
    inlines = (NormarUserInline,)


admin.site.unregister(
    User,
)
admin.site.register(User, CustomNormalUserSet)


admin.site.register(NormalUser)
