from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from apps.accounts.models import Account


# Register your models here.


@admin.register(Account)
class AccountAdmin(UserAdmin):
    model = Account
    list_display = ('email','username', 'last_login', 'date_joined', 'is_active')
    list_filter = ('email','username', 'last_login', 'date_joined', 'is_active')
    readonly_fields = ('last_login', 'date_joined',"slug")

    fieldsets = (
        ('Configurações', {"fields": ("email", "password","email_notify")}),
        ('Ganhos', {"fields": ("tab_coins","tab_cash")}),
        ("Permissões", {"fields": ("is_superuser", "is_staff",
                                   "is_active", "groups", "user_permissions")}),
        ("Datas importantes", {"fields": ("date_joined", "last_login")}),
        ("Imutáveis", {"fields": ("slug",)})

    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )

    search_fields = ('email', 'first_name', 'last_name', 'username')
    ordering = ('-date_joined',)