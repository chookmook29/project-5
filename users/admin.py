# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username"]
    fieldsets = (
        (("User"), {"fields": ("username", "email")}),
        (("Personal"), {"fields": ("first_name", "last_name")}),
        (("Contributions"), {"fields": ("contributions",)}),
        (("Comments amount"), {"fields": ("amount_comments",)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
