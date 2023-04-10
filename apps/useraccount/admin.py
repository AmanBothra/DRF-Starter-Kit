from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm


@register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "user_type", "is_active")
    list_filter = (
        "email",
        "user_type",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal Details",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "user_type",
                    "profile_picture",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_verified")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
