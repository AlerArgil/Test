from django.contrib import admin

from departaments.models import Departament


class UsersInline(admin.TabularInline):
    """
    Inline for creating Users and Departaments relation
    """
    model = Departament.users.through
    readonly_fields = 'binded_at',


class FamiliesInline(admin.TabularInline):
    """
    Inline for creating Families relation
    """
    model = Departament.families.through
    fk_name = 'parent'
    readonly_fields = 'level',


class DepartamentAdmin(admin.ModelAdmin):
    """
    Departament admin class
    """
    fields = 'id', 'name', 'company'
    readonly_fields = 'id',
    list_display = 'id', 'clients_count',
    inlines = [
        UsersInline,
        FamiliesInline
    ]

    def clients_count(self, instance):
        return instance.users.count()


admin.site.register(Departament, DepartamentAdmin)
