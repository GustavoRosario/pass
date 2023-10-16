from django.db import models
import datetime as dt

# Create your models here.
class ma_categoria(models.Model):
     categoria_id = models.AutoField(primary_key=True)
     prefijo = models.CharField(default='')
     descripcion = models.CharField(default = '')

     def __str__(self):
          return self.prefijo + ' - ' + self.descripcion

class control_solicitud(models.Model):
     categoria_id = models.IntegerField(default=0)
     secuencia_actual = models.IntegerField(default=0)
     fecha_actualizacion = models.DateField(null=False)
     
     def __str__(self):
          return self.nombre

class registro_historico(models.Model):
     id = models.AutoField(primary_key=True)
     fecha_registro = models.DateField()
     hora_registro = models.TimeField()
     turno  = models.CharField()
     usuario_id = models.IntegerField(null=True)
     activo = models.BooleanField(default=True)
     
     def __str__(self):
          return self.turno
