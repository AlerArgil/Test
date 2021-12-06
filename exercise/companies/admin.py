from django.contrib import admin

from companies.models import Company


class CompanyAdmin(admin.ModelAdmin):
    """
    Company admin class
    """
    fields = 'id', 'full_name', 'cut_name', 'inn', 'kpp', 'created_at', 'updated_at'
    readonly_fields = 'id', 'created_at', 'updated_at'


admin.site.register(Company, CompanyAdmin)
