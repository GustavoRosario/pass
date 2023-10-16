from aplication.models import registro_historico
from aplication.dto.historial import historial 
import datetime as dt

def registrar(_historial:historial):
    historico = registro_historico()
    historico.fecha_registro = dt.date.today()
    historico.hora_registro = dt.datetime.now().strftime('%H:%M:%S')
    historico.turno = _historial.turno
    historico.activo = True
    historico.save()
