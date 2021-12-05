from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from clients.models import User, AdditionalInfo


class AddInfoInline(admin.TabularInline):
    model = AdditionalInfo


class CustomUserAdmin(UserAdmin):
    fields = 'id', 'username', 'password',  'is_superuser', 'is_staff', 'is_active', 'last_login', 'date_joined',\
             'phone', 'first_name', 'last_name', 'middle_name', 'type', 'gender', 'timezone', 'ok', 'instagram',\
             'telegram', 'whatsapp', 'viber', 'created_at', 'updated_at',
    readonly_fields = 'id', 'created_at', 'updated_at'
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'phone'),
        }),
    )
    fieldsets = None
    inlines = [
        AddInfoInline,
    ]


admin.site.register(User, CustomUserAdmin)
