from django.contrib import admin
from cars.models import Car, Brand, Register

# Aqui vamos importar os modelos que queremos que apareçam no site de administração Django

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')
    search_fields = ('name', 'email')

# Aqui vamos registrar o modelo Car com a classe CarAdmin
admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Register, RegisterAdmin)
