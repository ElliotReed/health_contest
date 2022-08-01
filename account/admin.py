from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserAccountCreationForm
from .models import UserAccount


class UserAccountAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
    )


admin.site.register(UserAccount)
