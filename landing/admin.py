from django.contrib import admin
from landing.models import Company, Fabric, ProductCategory, Product, Service, Zvonki, Questions, Status


class CompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]  # выводит все поля

    class Meta:
        model = Company


admin.site.register(Company, CompanyAdmin)
admin.site.register(Fabric)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Service)
admin.site.register(Zvonki)
admin.site.register(Questions)
admin.site.register(Status)
