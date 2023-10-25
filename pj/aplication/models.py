from django.db import models

# Create your models here.
class ma_category(models.Model):
     category_id = models.AutoField(primary_key=True)
     prefix = models.CharField(max_length=10, blank=False)
     description = models.CharField(max_length=50, blank=True)
 
     def __str__(self):
          return self.prefijo + ' - ' + self.descripcion
     
     class Meta:
        db_table = "trn_ma_category"

class sequence_control(models.Model):
     category_id = models.IntegerField(default=0)
     current_sequence = models.IntegerField(default=0)
     date_update = models.DateField(null=False)
     update_time = models.TimeField(null=True)

     def __str__(self):
          return self.current_sequence
     
     class Meta:
        db_table = "trn_sequence_control"

class historical_record(models.Model):
     id = models.AutoField(primary_key=True)
     registration_date = models.DateField()
     registration_time = models.TimeField()
     turn  = models.CharField(max_length=10, blank=False)
     user_id = models.IntegerField(null=True)
     active = models.BooleanField(default=True)
     
     def __str__(self):
          return self.turn
     
     class Meta:
        db_table = "trn_historical_record"

class ma_state(models.Model):
    state_id = models.AutoField(primary_key=True)
    description_status = models.CharField(max_length=30)
    active = models.BooleanField(default=True,null=True)

    def __str__(self):
          return self.description_status
     
    class Meta:
        db_table = "trn_ma_state"

class generated_turn(models.Model):
    id_generated = models.AutoField(primary_key=True)
    turn = models.CharField(max_length=10, blank=False)
    state_id = models.IntegerField()
    station_id = models.IntegerField()
    registration_date = models.DateField()
    registration_time = models.TimeField()
    active = models.BooleanField(default=True,null=True)
    
    def __str__(self):
          return self.turn

    class Meta:
       db_table = "trn_generated_turn"

class ma_station(models.Model):
    id_station = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20)
    active = models.BooleanField(default=True,null=False)

    def __str__(self):
       return self.description

    class Meta:
       db_table = "trn_ma_station"

