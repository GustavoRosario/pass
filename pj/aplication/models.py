from django.db import models
import datetime as dt

# Create your models here.
class ma_categoria(models.Model):
     categoria_id = models.AutoField(primary_key=True)
     prefijo = models.CharField(max_length=10, blank=False)
     descripcion = models.CharField(max_length=50, blank=True)

     def __str__(self):
          return self.prefijo + ' - ' + self.descripcion
     
     class Meta:
        db_table = "trn_ma_categoria"

class control_secuencia(models.Model):
     categoria_id = models.IntegerField(default=0)
     secuencia_actual = models.IntegerField(default=0)
     fecha_actualizacion = models.DateField(null=False)
     hora_actualizacion = models.TimeField(null=True)

     def __str__(self):
          return self.secuencia_actual
     
     class Meta:
        db_table = "trn_control_secuencia"

class registro_historico(models.Model):
     id = models.AutoField(primary_key=True)
     fecha_registro = models.DateField()
     hora_registro = models.TimeField()
     turno  = models.CharField(max_length=10, blank=False)
     usuario_id = models.IntegerField(null=True)
     activo = models.BooleanField(default=True)
     
     def __str__(self):
          return self.turno
     
     class Meta:
        db_table = "trn_registro_historico"

class ma_estado(models.Model):
    estado_id = models.AutoField(primary_key=True)
    descripcion_estado = models.CharField(max_length=30)
    activo = models.BooleanField(default=True,null=True)

    def __str__(self):
          return self.descripcion_estado
     
    class Meta:
        db_table = "trn_ma_estado"

class turno_generado(models.Model):
    id_generado = models.AutoField(primary_key=True)
    turno = models.CharField(max_length=10, blank=False)
    estado_id = models.IntegerField()
    estacion_id = models.IntegerField()
    fecha_registro = models.DateField()
    hora_registro = models.TimeField()
    activo = models.BooleanField(default=True,null=True)
    
    class Meta:
       db_table = "trn_turno_generado"

class ma_estacion(models.Model):
    id_estacion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
       db_table = "trn_ma_estacion"

