from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto



class LaboratorioAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nombre', 'ciudad', 'pais')






class DirectorGeneralAdmin(admin.ModelAdmin):
    
    
    list_display = ('id', 'nombre', 'laboratorio_nombre', 'especialidad')

    def laboratorio_nombre(self, obj):
        return obj.laboratorio.nombre

    laboratorio_nombre.short_description = 'Laboratorio'
    






class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio_nombre2', 'get_f_fabricacion', 'p_costo', 'p_venta')

    def laboratorio_nombre2(self, obj):
        return obj.laboratorio.nombre

    laboratorio_nombre2.short_description = 'Laboratorio'

    def get_f_fabricacion(self, obj):
        return obj.f_fabricacion.year

    get_f_fabricacion.short_description = 'Año de Fabricación'



admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
