from django.contrib import admin

from departaments.models import Departament


class UsersInline(admin.TabularInline):
    model = Departament.users.through
    readonly_fields = 'binded_at',


class FamiliesInline(admin.TabularInline):
    model = Departament.families.through
    fk_name = 'parent'
    readonly_fields = 'level',


class DepartamentAdmin(admin.ModelAdmin):
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
