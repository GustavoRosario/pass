from aplication.models import ma_categoria as cat,control_secuencia as cso
from aplication.models import turno_generado
import datetime as dt


def generar(categoria_id:int):
    secuencia:str
    SECUENCIA_INICIAL:int = 1
    prefijo = get_prefijo(categoria_id)
    sec =  get_secuencia(categoria_id)
    fecha_sys = dt.date.today()
    fecha_actualizacion = get_fecha_actualizacion(categoria_id)
    secuencia = prefijo + '-' + str(sec)
    
    if(fecha_sys == fecha_actualizacion):
        update_secuencia(categoria_id,sec)
        update_fecha_secuencia(categoria_id)
    elif(fecha_sys != fecha_actualizacion):
        secuencia = prefijo + '-' + str(SECUENCIA_INICIAL)
        update_secuencia(categoria_id,SECUENCIA_INICIAL)
        update_fecha_secuencia(categoria_id)

    return secuencia

def registrar(_turno:turno_generado):
    EN_COLA:int = 1
    ESTACION_ID:int = 1
    turno = turno_generado()
    turno.fecha_registro = dt.date.today()
    turno.estado_id = EN_COLA
    turno.estacion_id = ESTACION_ID
    turno.fecha_registro = dt.date.today()
    turno.hora_registro = dt.datetime.now().strftime('%H:%M:%S')
    turno.turno = _turno.turno
    turno.activo = True
    turno.save()

def get_prefijo(_categoria_id:int):
    query = cat.objects.get(categoria_id = _categoria_id)
    result =  query.prefijo
    return result
 
def get_secuencia(_categoria_id:int):
        query = cso.objects.get(categoria_id = _categoria_id)
        secuencia =  query.secuencia_actual
        result = next_turn(secuencia)
        return result

def get_fecha_actualizacion(_categoria_id:int):
        query = cso.objects.get(categoria_id = _categoria_id)
        fecha =  query.fecha_actualizacion
        return fecha

def update_fecha_secuencia(_categoria_id:int,):
     query = cso.objects.get(categoria_id = _categoria_id)
     query.fecha_actualizacion = dt.datetime.today() 
     query.hora_actualizacion  = dt.datetime.now().strftime('%H:%M:%S')
     query.save()
    
def update_secuencia(_categoria_id:int,nueva_secuencia:int):
     query = cso.objects.get(categoria_id = _categoria_id)
     query.secuencia_actual = nueva_secuencia
     query.save()

def next_turn(sec:int):
    x:int = 1
    x = x + sec
    return x
