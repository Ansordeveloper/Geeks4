from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from users.forms import CustomUserCreationFoorm, CustomUserChangeFoorm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationFoorm
    form = CustomUserChangeFoorm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("is_staff","is_active","is_superuser")
    ordering = ("email",)
    search_fields = ("email",)
    fieldsets = (
        ("Оснавная информация", {"fields": ("email","password")}),
        ("Права пользователя", {"fields": ("is_staff", "is_active", "groups", "user_permissions")})
    )

    add_fieldsets = (
        ("Создание пользователя", {
        "classes":("wide",),
        "fields":(
            "email", "password", "password2", "is_staff", "is_active", "groups", "user_permissions"
        )
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)