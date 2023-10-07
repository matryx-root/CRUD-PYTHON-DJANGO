from django import forms
from django.db import models
from django.forms import SelectDateWidget

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.ciudad} - {self.pais}"

    class Meta:
        ordering = ['id']

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, default="Sin Especialidad") 

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.laboratorio} - {self.especialidad}"
    
    class Meta:
        ordering = ['id']



class YearSelectorWidget(SelectDateWidget):
    def create_select(self, *args, **kwargs):
        old_state = self.is_required
        self.is_required = False
        result = super().create_select(*args, **kwargs)
        self.is_required = old_state
        return result


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(default="2015-01-01")
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id} - {self.nombre}- {self.laboratorio}- {self.f_fabricacion}- {self.p_costo}- {self.p_venta}"
    class Meta:
        ordering = ['id']