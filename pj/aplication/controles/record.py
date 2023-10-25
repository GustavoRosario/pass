from aplication.models import historical_record
from aplication.dto.historial import record 
import datetime as dt

def register(_record:record):
    historical = historical_record()
    historical.registration_date = dt.date.today()
    historical.registration_time = dt.datetime.now().strftime('%H:%M:%S')
    historical.turn = _record.turn
    historical.active = True
    historical.save()
